
# A Quarto Tech Paper Example




## Introduction

The project structure is based on: https://github.com/gael-close/quarto-tech-paper.



## Installation



**Install all dependencies:**
```bash
# Install ALL dependencies (conda packages + Python packages + local package)
pixi install
```


To verify the installation:

```bash
pixi list
pixi run check-import
pixi run pytest -s
```







## Publishing

### Google Drive


1. **First-time setup:**
   - Create Google Drive API credentials ([instructions](https://console.cloud.google.com/))
   - Place `client_secrets.json` in `~/.config/pixi_gdrive/`
   - Run `pixi run pub-gdrive` - browser auth will open once

2. **Set file ID in `.env`:**
   ```
   GOOGLE_FID=your_google_drive_file_id
   ```

3. **Publish:**
   ```bash
   
   ```

See [scripts/README.md](scripts/README.md) for detailed setup instructions.

### Website Distribution

Build a landing page with embedded PDF and supplementary materials:

```bash
pixi run dist
```

The output in `dist/` can be deployed to GitHub/GitLab Pages. Example workflow files are in `optional/`.

Customize the landing page in [site/index.qmd](site/index.qmd).