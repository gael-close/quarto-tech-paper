---
title: Quarto Tech Paper Example
subtitle: My Subtitle
author:
  - name: John Smith
date: today
abstract: |
  This landing page is a placeholder. It embeds the full PDF of the paper,
  links to supplementary notebooks, and a link to source code.
  One could also embed video, images, and other media.
page-layout: full
lightbox: true

format:
  html:
    toc: true
    toc-depth: 3
    toc-location: right
    toc-title: "Contents"
    standalone: true
    embed-resources: true
---


<!-- ── Pills buttons ──────────────────────────────────────────────────────── -->

::: {.d-flex .gap-2 .flex-wrap .mb-4}
[📄 Full Paper](https://doi.org){.btn .btn-outline-primary .btn-sm role="button"}
[📹 Video Demo](https://www.youtube.com){.btn .btn-outline-primary .btn-sm role="button"}
[🔗 GitHub](https://github.com){.btn .btn-outline-primary .btn-sm role="button"}
:::



# Core method {#sec-core-method}

![](figs/abstract.png){width=50%}

# Key results {#sec-results}

Possibly in a dense grid layout.


::: {.column-page layout-ncol=3}
![](https://dummyimage.com/400x200?text=A){group="my-gallery"}

![](https://dummyimage.com/400x200?text=B){group="my-gallery"}

![](https://dummyimage.com/400x200?text=C){group="my-gallery"}
:::

# Full paper {#sec-paper}

```{=html}
<div style="max-width: 1000px;">
  <iframe
    src="{{< meta title >}}.pdf"
    style="width: 100%; height: 1000px; border: 1px solid #e5e7eb; border-radius: 0.5rem;"
    allowfullscreen>
  </iframe>
</div>
```

# Supplementary {#sec-supplementary}

Follow the [IEEE guidelines for preparing supplementary materials](https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/prepare-supplementary-materials/).

* [Notebook 01](supplementary/01-notebook.html) is a Python notebook showing ...
* [Notebook 02](supplementary/02-notebook.html) is a Python notebook showing ...
* `Video.mp4` is a video showing ...

Zip archive: xxx MB.

# Citation {#sec-citation}

```bibtex
@article{doe2026dummy,
  title   = {A Dummy Article for Demonstration Purposes},
  author  = {Doe, John and Smith, Jane},
  journal = {Journal of LaTeX Examples},
  volume  = {42},
  number  = {3},
  pages   = {101--115},
  year    = {2026},
  doi     = {10.1039/dummyurl},
  url     = {https://example.com}
}
```
