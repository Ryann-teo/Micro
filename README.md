# Core Micro Study Guide

Single-page revision dashboard for the Oxford FHS Core Microeconomics paper.

## Contents

- **173 concept cards** covering every concept referenced in past papers 2014 to 2025 and in the FHS lecture slides Wk1 to Wk7. Click to expand.
- **6 Question Typing blocks** (one per pair of topics) merged inline so you can see all question types across topics on a single page. Wiki-links go to in-page concept cards.
- **Sidebar** with collapsible per-topic dropdowns containing Question Types and Concept lists.

## Phase status

Each concept card has four sections:
1. Intuition. Filled in for all 173.
2. Formal mathematics. Phase 2 (Tier 1 written; rest todo).
3. Graphical illustration / interactive widget. Phase 2 (Tier 1 written; rest todo).
4. Real-life examples and essay points. Phase 2 (Tier 1 written; rest todo).

## Deploy

`push.bat` (Windows) or `push.sh` (bash) pushes to https://github.com/Ryann-teo/Micro.git. After the first push, enable GitHub Pages at https://github.com/Ryann-teo/Micro/settings/pages (Source: Deploy from a branch, Branch: main, Folder: / (root)).

Live site: https://ryann-teo.github.io/Micro/

## Rebuild

`update.bash` regenerates the site from `concepts_data.py` and `phase2_content.py` and pushes. Run after editing either data file.
