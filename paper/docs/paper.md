---
title: Quarto Tech Paper Example
subtitle: A minimum example using the quarto-tech-memo extension
abstract: |-
  This is an minimum technical memo containing the usual elements of technical writing: 
  figure, table, equation, citation, bibliography, code snippet, and appendix.
  The document is rendered to PDF by Quarto with a custom extension which provides several styles.
  A memo style (inspired from Tufte handout style) for brief report,
  a 2-column paper style for scientific article, and a A3 poster style.
  The PDF is rendered with the modern Typst engine, which is built into Quarto.
keywords: Quarto, technical writing, memo, paper, poster
author:
  - name: First Author
    email: first@email.ch
    orcid: 0000-0000-0000-0001
    affiliation:
      - ref: 1
  - name: Second Author
    email: second@email.ch
    orcid: 0000-0000-0000-0002
    affiliation:
      - ref: 2
  - name: Third Author
    email: third@email.ch
    orcid: 0000-0000-0000-0003
    affiliation:
      - ref: 1
    corresponding: true
affiliations:
  - id: 1
    name: Magic Technologies SA
    city: Morges
    country: Switzerland
  - id: 2
    name: Another Corporate Inc
    city: Palo Alto
    country: USA
bibliography: biblio.bib
format:
  memo1-typst: default
  page-html:
    shift-heading-level-by: 1
    pandoc-args:
      - "--lua-filter=_extensions/page/custom.lua"
  reveal-revealjs: default
url: https://github.com/gael-close/quarto-tech-memo
---

# Overview

## Minimum example
This minimum example contains all standard elements of a technical writing
to illustrate the formatting styles provided by the [quarto-tech-memo extension](https://github.com/gael-close/quarto-tech-memo).
Let's start with some math: $e^{\pi i} + 1 = 0$ is an inline equation, 
[In memo style, margin notes are supported, 
including small **inline** image.
![](figs/small-fig.png){width=3cm} 
They shouldn't be used in 2-column paper style.]{.aside}
Eq. @eq-field is a numbered equation.
Here is some physical quantities using unicode: $B_\mathrm{noise}=15$\ μT/√Hz.
Note the "Narrow No-Break Space (NNBSP)" unicode `202F`. 

$$
\nabla \times \mathbf{B} = \mu_0 \mathbf{J} + \mu_0 \varepsilon_0 \frac{\partial \mathbf{E}}{\partial t} 
$$ {#eq-field}

<!-- Uncomment to populate with more dummy text 
{{< lipsum 1 >}}



::: {.wideblock}
![A figure extending into the right margin.](https://dummyimage.com/300x100){#fig-placeholder} 
:::
-->

## Figures and tables

Citations are included in IEEE style such as @close2022.
@fig-placeholder shows a numbered figure.
@tbl-placeholder is a numbered table.


![Figure caption.](figs/data-plot.png){#fig-placeholder width=3in }

| Parameter             | Symbol          | Typ | Unit |
| :-------------------- | --------------- | --- | ---- |
| Hall sensitivity      | $S_\mathrm{H}$  | 0.2 | V/T  |
| Effective nr. of bits | $\mathrm{ENOB}$ | 12  | -    |

: Example of engineering table {#tbl-placeholder}


{{< colbreak >}}

## Code snippet and callouts | Subtitle on the second line 

A title spanning two lines is often used in slide decks
to emphasize a full sentence.

Syntax highlighting is supported in code snippet too.
Callout boxes are available with appropriate icons or colors.

```python
def f(x, square=True):
    # Python code snippet
    return (x**2) if square else x
```

::: {.callout-note title="Markdown syntax"}
The manuscript is written in [Markdown](https://quarto.org/docs/authoring/markdown-basics.html), 
a plain-text **easy syntax**.
:::

## Dummy section

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec semper leo nec quam aliquam consectetur.

<!-- 
{{< lipsum 1 >}} 
-->

::: {.ignore}

# IGNORED 

## README

Adjust the following command to compile and publish.

```bash
quarto-tech-memo xxx.md
rclone copyto xxx.pdf "remote:.../Published Name.pdf"
```

Published file: [[Published Name.pdf|local]] | [Online](URL)


See this specific example to publish to Gdrive from Obsidian: [[2503 My Terminal Snippets#^md2memo]].

:::

