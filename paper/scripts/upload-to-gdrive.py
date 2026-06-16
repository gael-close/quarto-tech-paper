#!/usr/bin/env uv run
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "pydantic-settings>=2.0.0",
#     "pyprojroot>=0.3.0",
#     "typer",
# ]
# ///

import subprocess
import sys
import os
from pyprojroot import here
import typer

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Pydantic automatically looks for an environment variable named RCLONE_DRIVE_TOKEN
    RCLONE_DRIVE_TOKEN: str 
    GOOGLE_FID: str | None = None
    GOOGLE_ID: str | None = None

    # Tell Pydantic to read from a local .env file if the OS variable isn't set
    model_config = SettingsConfigDict(env_file=here(".env"), extra="ignore")

    @property
    def google_id(self) -> str:
        return self.GOOGLE_ID or self.GOOGLE_FID

settings = Settings()


def update_or_upload_standalone(local_file_path, folder_id):
    """
    Uploads/updates a file inside Google Drive using a direct Folder ID (FID)
    and an embedded OAuth token. Zero pre-configuration required.
    """
    # Validation checks
    if not os.path.exists(local_file_path):
        print(f"❌ Error: Local file '{local_file_path}' not found.")
        return False
        
    file_name = os.path.basename(local_file_path)
    
    # 2. Inject configuration fields explicitly on-the-fly.
    # Passing the exact token means rclone bypasses all configuration prompts.
    on_the_fly_remote = f':drive,root_folder_id="{folder_id}",token=\'{settings.RCLONE_DRIVE_TOKEN}\':'
    
    print(f"🔄 Headless sync started for '{file_name}' to Folder ID: {folder_id}...")

    # 3. Assemble command targeting the precise destination name
    command = [
        "rclone", "copyto",
        local_file_path,
        f"{on_the_fly_remote}{file_name}",
        "--drive-acknowledge-abuse",
        "-v"
    ]
    
    try:
        # Run rclone headlessly and capture real-time output
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                print(output.strip())
                
        rc = process.poll()
        if rc == 0:
            print(f"✅ Success! Version updated seamlessly without pre-configuration.")
            return True
        else:
            print(f"❌ Rclone processing failed with exit code {rc}.")
            return False
            
    except FileNotFoundError:
        print("❌ Error: 'rclone' binary must be installed on this machine's system PATH.")
        return False

app = typer.Typer()

@app.command()
def main(
    name: str = typer.Option(..., "--name", help="Path to local file to upload"),
    id: str = typer.Option(settings.google_id, "--id", help="Google Drive Folder ID")
):
    if not id:
        print("❌ Error: Google Drive Folder ID must be provided via --id option or env variables (GOOGLE_ID/GOOGLE_FID).")
        raise typer.Exit(code=1)
    update_or_upload_standalone(local_file_path=name, folder_id=id)

if __name__ == "__main__":
    app()