---
title: Formatting Technical Paper with Quarto
subtitle: A minimum example using the quarto-tech-memo extension
abstract: |
 This is an minimum technical memo containing the usual elements of technical writing: 
 figure, table, equation, citation, bibliography, code snippet, and appendix.
 The document is rendered to PDF by Quarto with a custom extension which provides several styles.
 A memo style (inspired from Tufte handout style) for brief report,
 a 2-column paper style for scientific article, and a A3 poster style.
 The PDF is rendered with the modern Typst engine, which is built into Quarto.
keywords: Quarto, technical writing, memo, paper, poster
author:
  - name: First Author
    email: firstc@email.ch
    orcid: 0000-0000-0000-0001
    affiliation: [{ref: 1}]
  - name: Second Author
    email: second@email.ch
    orcid: 0000-0000-0000-0002
    affiliation: [{ref: 2}]
  - name: Third Author
    email: third@email.ch
    orcid: 0000-0000-0000-0003
    affiliation: [{ref: 1}]
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
url: https://github.com/gael-close/quarto-tech-memo
---

## Overview 

### Minimum example
This minimum example contains all standard elements of a technical writing
to illustrate the formatting styles provided by the [quarto-tech-memo extension](https://github.com/gael-close/quarto-tech-memo).
Let's start with some math: $e^{\pi i} + 1 = 0$ is an inline equation, 
[In memo style, margin notes are supported, 
including small **inline** image.
![figs/small-fig.png](figs/small-fig.png){width=3cm} 
They shouldn't be used in 2-column paper style.]{.aside}
Eq. @eq-field is a numbered equation.
Here is a physical quantity with unit: 1 μT (1 microtesla),
note the thin non-breaking space.
In IEEE legacy PDF, one need to use the math mode
or the SI unit package to render the greek letters.

$$
\nabla \times \mathbf{B} = \mu_0 \mathbf{J} + \mu_0 \varepsilon_0 \frac{\partial \mathbf{E}}{\partial t} 
$$ {#eq-field}

<!-- Uncomment to populate with more dummy text 
{{< lipsum 1 >}}
![Figure caption.](https://dummyimage.com/300x100){#fig-placeholder} 
-->

### Figures and tables

Citations are included in IEEE style such as @close2022.
@fig-joint-plot shows a numbered figure.
@tbl-placeholder is a numbered table.


{{< embed ../notebooks/01-notebook.ipynb#fig-joint-plot >}}

| Parameter             | Symbol          | Typ | Unit |
| :-------------------- | --------------- | --- | ---- |
| Hall sensitivity      | $S_\mathrm{H}$  | 0.2 | V/T  |
| Effective nr. of bits | $\mathrm{ENOB}$ | 12  | -    |

: Example of engineering table {#tbl-placeholder}


{{< colbreak >}}

### Code snippet and callouts
Syntax highlighting is supported in code snippet too.
Moreover, callout boxes are available for tips, notes, warnings, and important remarks,
with appropriate icons or colors.

```python
def f(x, square=True):
    # Python code snippet
    return (x**2) if square else x
```

::: {.callout-note title="Markdown syntax"}
The manuscript is written in [Markdown](https://quarto.org/docs/authoring/markdown-basics.html), 
a plain-text **easy syntax**.
:::

### Dummy text

*Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec semper leo nec quam aliquam consectetur. Donec sollicitudin elit nec nunc congue, quis malesuada nulla cursus. Mauris vulputate vehicula velit, et malesuada nunc luctus quis. Nullam efficitur leo sit amet odio iaculis consequat. Nam ultrices, orci fermentum gravida aliquet, eros eros accumsan neque, quis tincidunt lectus tortor a enim. Phasellus eu tellus et ipsum blandit pulvinar. Mauris in lorem vitae libero viverra tristique a non velit.*

<!-- {{< lipsum 1 >}} -->
