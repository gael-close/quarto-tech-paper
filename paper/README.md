# A Quarto Tech Paper Example

See the full documentation at <https://github.com/gael-close/quarto-tech-paper>.

## Quick start

```bash
pixi install
cp .env.example .env   # edit: SHORT_TITLE, GOOGLE_FID, RCLONE_DRIVE_TOKEN
pixi run setup         # install Quarto extensions + apply title
```

## Common tasks

```bash
pixi run render-paper                    # render paper.qmd → dist/<TITLE>.pdf
NB=01-notebook.ipynb pixi run notebook   # execute notebook → dist/supplementary/
NB=02-notebook.py pixi run notebook-marimo
pixi run render-site                     # build landing page → dist/index.html
pixi run pub-gdrive                      # upload PDF to Google Drive
```

## Publishing

- **Google Drive** — requires `rclone` on `PATH` and `RCLONE_DRIVE_TOKEN` in `.env`.
  Obtain a token once with `rclone authorize "drive"`.
- **GitLab Pages** — `dist/` is deployed automatically via [`.gitlab-ci.yml`](.gitlab-ci.yml).
  Customize the landing page in [docs/index.md](docs/index.md).
