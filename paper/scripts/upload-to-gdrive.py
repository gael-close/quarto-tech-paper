#!/usr/bin/env python3
"""Upload file to Google Drive using PyDrive2.

Usage:
    python upload_to_gdrive.py <local_file_path> <target_file_id>
"""
import os
import sys
from pathlib import Path
from platformdirs import user_config_dir
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive


def main():
    # 1. Define a hidden, cross-platform path for your app
    # This creates a hidden folder named "pixi_gdrive" in the system config directory
    app_name = "pixi_gdrive"
    config_dir = Path(user_config_dir(app_name))
    config_dir.mkdir(parents=True, exist_ok=True)  # Ensure the folder exists

    # 2. Put the credentials file inside that hidden directory
    credentials_path = config_dir / "my_credentials.txt"

    # 3. Pass the absolute string path to PyDrive2
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile(str(credentials_path))

    if gauth.credentials is None:
        # Triggers the browser auth on the very first run
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        gauth.Refresh()
    else:
        gauth.Authorize()

    gauth.SaveCredentialsFile(str(credentials_path))
    drive = GoogleDrive(gauth)

    # 4. Accept arguments from Pixi task
    if len(sys.argv) != 3:
        print("Usage: python upload_to_gdrive.py <local_file_path> <target_file_id>")
        sys.exit(1)

    local_file_path = sys.argv[1]
    target_file_id = sys.argv[2]

    # 5. Overwrite the file using its ID
    file_obj = drive.CreateFile({"id": target_file_id})
    file_obj.SetContentFile(local_file_path)
    file_obj.Upload()

    print(f"Successfully updated File ID: {target_file_id}")


if __name__ == "__main__":
    main()
