# Core Micro Study Guide

A complete study companion for the Oxford FHS Core Microeconomics paper.

## What's here

- **173 concept pages** covering every concept referenced in past papers 2014 to 2025 and in the FHS lecture slides (Wk1 to Wk7).
- **8 topic overview pages** matching the lecture structure.
- **6 Question Typing pages** with step-by-step guides to Part A short problems, Part B essays, and Part B long-answer problems.

## Status

This is the Phase 1 build. Each concept page currently contains:

1. **Intuition** (plain-English explanation, 1 to 3 paragraphs). Filled in.
2. **Formal mathematics**. Placeholder.
3. **Graphical illustration / interactive widget**. Placeholder.
4. **Real-life examples and essay points**. Placeholder.

Phase 2 will fill in the math, widgets, and examples for the top-priority concepts.

## Hosting

The site is plain HTML/CSS/JS with KaTeX and Plotly loaded from CDN. No build step.

To enable GitHub Pages: in the repo settings, go to Pages, set source to `main` branch, root folder. The site will be live at `https://ryann-teo.github.io/Micro/`.

## Local preview

```
cd Website
python3 -m http.server 8000
```

Open http://localhost:8000.

## Updating

Run `python3 build_site.py` from the `site-build/` folder after editing `concepts_data.py`.
