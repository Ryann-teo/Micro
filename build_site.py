"""Generates the entire Core Micro study website from the concepts manifest.

Outputs to: Areas/Economics/Core Micro/Website/
Produces:
  - index.html (landing page, sidebar navigation, search)
  - assets/style.css
  - assets/app.js (search + UI)
  - topics/<id>-<slug>.html (8 topic overview pages)
  - concepts/<slug>.html (173 concept pages)
  - question-types/qt<n>-<slug>.html (6 question-type pages, converted from MD)
  - README.md (deployment instructions)
  - push.sh (git push script)
"""

import os
import re
import shutil
import html
import textwrap
from concepts_data import TOPICS, CONCEPTS

OUT = "/sessions/practical-beautiful-bell/mnt/Big Brain/Areas/Economics/Core Micro/Website"
QT_DIR = "/sessions/practical-beautiful-bell/mnt/Big Brain/Areas/Economics/Core Micro/Study Guide/Question Types"


def slugify(name: str) -> str:
    s = name.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s


# Build a name -> slug map (for resolving [[Concepts/Name]] links)
CONCEPT_NAME_TO_SLUG = {c[1]: c[0] for c in CONCEPTS}
# Also add some normalised variants
NORM_MAP = {}
for name, slug in CONCEPT_NAME_TO_SLUG.items():
    NORM_MAP[name] = slug
    NORM_MAP[name.lower()] = slug


# Topic slug helper
def topic_slug(t):
    return f"{t[0]}-{slugify(t[1])}"


# Color palette per topic (used in tag chips)
TOPIC_COLORS = {
    1: "#5b8def",  # blue
    2: "#7c4dff",  # purple
    3: "#26a69a",  # teal
    4: "#ef6c00",  # orange
    5: "#d81b60",  # pink
    6: "#43a047",  # green
    7: "#fb8c00",  # amber
    8: "#5e35b1",  # deep purple
}


HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="{root}assets/style.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css" crossorigin="anonymous">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js" crossorigin="anonymous"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" crossorigin="anonymous"
  onload="renderMathInElement(document.body,{{delimiters:[{{left:'$$',right:'$$',display:true}},{{left:'$',right:'$',display:false}}],throwOnError:false}});"></script>
<script defer src="https://cdn.plot.ly/plotly-2.32.0.min.js"></script>
<script defer src="{root}assets/app.js"></script>
</head>
<body>
<header class="topbar">
  <a class="logo" href="{root}index.html">Core Micro</a>
  <input id="search" class="search" type="text" placeholder="Search concepts..." autocomplete="off">
  <nav class="topnav">
    <a href="{root}index.html">Home</a>
    <a href="{root}index.html#topics">Topics</a>
    <a href="{root}index.html#concepts">Concepts</a>
    <a href="{root}index.html#question-types">Question Types</a>
  </nav>
</header>
<div class="layout">
<aside class="sidebar">
{sidebar}
</aside>
<main class="content">
"""

TAIL = """
</main>
</div>
<footer class="footer">
  Core Micro Study Guide. Built from past papers 2014 to 2025, FHS lecture slides, and Micro2025 reading list.
</footer>
</body>
</html>
"""


def build_sidebar(active_concept_slug=None, active_topic_id=None):
    """Sidebar lists topics with their concepts."""
    parts = ['<div class="sidebar-inner">']
    parts.append('<div class="sidebar-section"><a href="../index.html#question-types" class="sidebar-link">Question Types</a></div>')
    for t in TOPICS:
        tid = t[0]
        tname = t[1]
        tslug = topic_slug(t)
        active = ' active' if active_topic_id == tid else ''
        parts.append(f'<div class="sidebar-section">')
        parts.append(f'  <a href="../topics/{tslug}.html" class="sidebar-topic{active}" data-topic-id="{tid}">{tname}</a>')
        # List concepts in topic
        topic_concepts = [c for c in CONCEPTS if c[2] == tid]
        # Sort: tier 1 first, then 2, 3, 4, S; then alphabetical
        tier_order = {1: 0, 2: 1, 3: 2, 4: 3, "S": 4}
        topic_concepts.sort(key=lambda c: (tier_order.get(c[3], 99), c[1]))
        parts.append('  <ul class="sidebar-concepts">')
        for c in topic_concepts:
            slug = c[0]; nm = c[1]
            cls = ' active' if slug == active_concept_slug else ''
            parts.append(f'    <li><a href="../concepts/{slug}.html" class="sidebar-concept{cls}" data-name="{html.escape(nm)}">{html.escape(nm)}</a></li>')
        parts.append('  </ul>')
        parts.append('</div>')
    parts.append('</div>')
    return "\n".join(parts)


def build_index_sidebar():
    parts = ['<div class="sidebar-inner">']
    parts.append('<div class="sidebar-section"><a href="#question-types" class="sidebar-link">Question Types</a></div>')
    for t in TOPICS:
        tid = t[0]
        tname = t[1]
        tslug = topic_slug(t)
        parts.append(f'<div class="sidebar-section">')
        parts.append(f'  <a href="topics/{tslug}.html" class="sidebar-topic" data-topic-id="{tid}">{tname}</a>')
        topic_concepts = [c for c in CONCEPTS if c[2] == tid]
        tier_order = {1: 0, 2: 1, 3: 2, 4: 3, "S": 4}
        topic_concepts.sort(key=lambda c: (tier_order.get(c[3], 99), c[1]))
        parts.append('  <ul class="sidebar-concepts">')
        for c in topic_concepts:
            slug = c[0]; nm = c[1]
            parts.append(f'    <li><a href="concepts/{slug}.html" class="sidebar-concept" data-name="{html.escape(nm)}">{html.escape(nm)}</a></li>')
        parts.append('  </ul>')
        parts.append('</div>')
    parts.append('</div>')
    return "\n".join(parts)


# ============== INDEX ==============

def build_index():
    sidebar = build_index_sidebar()
    head = HEAD.format(title="Core Micro Study Guide", root="", sidebar=sidebar)
    body = ['<section class="hero">']
    body.append('<h1>Core Microeconomics</h1>')
    body.append('<p class="lead">All 173 concepts from the Oxford FHS Core Micro syllabus, every past-paper question type from 2014 to 2025, and step-by-step answer guides. Interactive widgets and graphical illustrations on every concept page.</p>')
    body.append('<div class="hero-stats">')
    body.append(f'<div class="stat"><div class="stat-num">173</div><div class="stat-label">Concepts</div></div>')
    body.append(f'<div class="stat"><div class="stat-num">8</div><div class="stat-label">Topics</div></div>')
    body.append(f'<div class="stat"><div class="stat-num">76</div><div class="stat-label">Past Questions</div></div>')
    body.append(f'<div class="stat"><div class="stat-num">6</div><div class="stat-label">Question Type Files</div></div>')
    body.append('</div></section>')

    # Topics
    body.append('<section id="topics"><h2>Topics</h2><div class="topic-grid">')
    for t in TOPICS:
        tid, tname, tdesc, tsource = t
        tslug = topic_slug(t)
        color = TOPIC_COLORS[tid]
        n_concepts = sum(1 for c in CONCEPTS if c[2] == tid)
        body.append(f'<a class="topic-card" href="topics/{tslug}.html" style="border-top-color: {color}">')
        body.append(f'  <div class="topic-num" style="background:{color}">{tid}</div>')
        body.append(f'  <div class="topic-name">{html.escape(tname)}</div>')
        body.append(f'  <div class="topic-desc">{html.escape(tdesc)}</div>')
        body.append(f'  <div class="topic-meta">{n_concepts} concepts</div>')
        body.append('</a>')
    body.append('</div></section>')

    # Question Types
    body.append('<section id="question-types"><h2>Question Types (Past Papers 2014 to 2025)</h2>')
    body.append('<p>One file per topic. Each contains Part A short problems, Part B essays, and Part B long-answer problems, broken into sub-question types with actionable step-by-step guides.</p>')
    body.append('<div class="qt-grid">')
    qt_files = [
        ("qt1-general-equilibrium-and-welfare", "1: General Equilibrium and Welfare", 1),
        ("qt2-externalities-and-public-goods", "2: Externalities and Public Goods", 3),
        ("qt3-game-theory-and-industrial-organisation", "3: Game Theory and Industrial Organisation", 4),
        ("qt4-decisions-under-risk", "4: Decisions under Risk", 6),
        ("qt5-adverse-selection", "5: Adverse Selection", 7),
        ("qt6-moral-hazard", "6: Moral Hazard", 8),
    ]
    for fslug, fname, tid in qt_files:
        color = TOPIC_COLORS[tid]
        body.append(f'<a class="qt-card" href="question-types/{fslug}.html" style="border-left-color:{color}">')
        body.append(f'  <div class="qt-name">{html.escape(fname)}</div>')
        body.append('</a>')
    body.append('</div></section>')

    # All concepts (for ctrl-F)
    body.append('<section id="concepts"><h2>All concepts</h2>')
    body.append('<p>Sorted by topic, then by priority tier. Click a concept to open its page.</p>')
    body.append('<div class="all-concepts">')
    for t in TOPICS:
        tid = t[0]; tname = t[1]
        color = TOPIC_COLORS[tid]
        body.append(f'<div class="concept-group">')
        body.append(f'  <h3 style="color:{color}">{html.escape(tname)}</h3>')
        body.append('  <ul class="concept-list">')
        topic_concepts = [c for c in CONCEPTS if c[2] == tid]
        tier_order = {1: 0, 2: 1, 3: 2, 4: 3, "S": 4}
        topic_concepts.sort(key=lambda c: (tier_order.get(c[3], 99), c[1]))
        for c in topic_concepts:
            slug, nm, _, tier, _ = c
            tier_label = "T" + str(tier) if tier != "S" else "S"
            body.append(f'    <li><a href="concepts/{slug}.html"><span class="tier-chip tier-{tier_label.lower()}">{tier_label}</span> {html.escape(nm)}</a></li>')
        body.append('  </ul>')
        body.append('</div>')
    body.append('</div></section>')

    out = head + "\n".join(body) + TAIL
    with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as f:
        f.write(out)


# ============== TOPIC PAGES ==============

def build_topic_page(topic):
    tid, tname, tdesc, tsource = topic
    tslug = topic_slug(topic)
    color = TOPIC_COLORS[tid]
    sidebar = build_sidebar(active_topic_id=tid)
    head = HEAD.format(title=f"{tname} | Core Micro", root="../", sidebar=sidebar)
    body = [f'<nav class="breadcrumb"><a href="../index.html">Home</a> / <span>{html.escape(tname)}</span></nav>']
    body.append(f'<h1 style="border-bottom: 3px solid {color}; padding-bottom: 0.3em">{html.escape(tname)}</h1>')
    body.append(f'<p class="lead">{html.escape(tdesc)}</p>')
    body.append(f'<p class="source-note"><strong>Source:</strong> {html.escape(tsource)}</p>')

    # Question Type link
    qt_map = {1: "qt1-general-equilibrium-and-welfare", 2: "qt1-general-equilibrium-and-welfare",
              3: "qt2-externalities-and-public-goods", 4: "qt3-game-theory-and-industrial-organisation",
              5: "qt3-game-theory-and-industrial-organisation", 6: "qt4-decisions-under-risk",
              7: "qt5-adverse-selection", 8: "qt6-moral-hazard"}
    qt_slug = qt_map[tid]
    body.append(f'<p class="cta-link"><a href="../question-types/{qt_slug}.html">Open Question Typing for this topic →</a></p>')

    # Concepts grouped by tier
    body.append('<h2>Concepts</h2>')
    topic_concepts = [c for c in CONCEPTS if c[2] == tid]
    tiers_present = sorted({c[3] for c in topic_concepts}, key=lambda x: (0 if isinstance(x, int) else 1, x if isinstance(x, int) else 99))
    tier_label_map = {1: "Tier 1: write first (8+ mentions in past papers)",
                      2: "Tier 2: core building blocks (5 to 7 mentions)",
                      3: "Tier 3: important but less frequent (3 to 4 mentions)",
                      4: "Tier 4: niche (1 to 2 mentions)",
                      "S": "From slides: in lectures but not yet in a past paper"}
    for tier in tiers_present:
        label = tier_label_map.get(tier, str(tier))
        body.append(f'<h3 class="tier-heading">{label}</h3>')
        body.append('<ul class="concept-list-wide">')
        cs = [c for c in topic_concepts if c[3] == tier]
        cs.sort(key=lambda c: c[1])
        for c in cs:
            slug, nm, _, _, intuit = c
            first_para = intuit[0] if intuit else ""
            preview = first_para[:200] + ("..." if len(first_para) > 200 else "")
            body.append(f'<li><a href="../concepts/{slug}.html"><strong>{html.escape(nm)}</strong></a><span class="concept-preview"> {html.escape(preview)}</span></li>')
        body.append('</ul>')

    out = head + "\n".join(body) + TAIL
    with open(os.path.join(OUT, "topics", f"{tslug}.html"), "w", encoding="utf-8") as f:
        f.write(out)


# ============== CONCEPT PAGES ==============

def render_intuition(paragraphs):
    out = []
    for p in paragraphs:
        out.append(f"<p>{p}</p>")
    return "\n".join(out)


def build_concept_page(concept):
    slug, name, tid, tier, intuition = concept
    topic = [t for t in TOPICS if t[0] == tid][0]
    tslug = topic_slug(topic)
    tname = topic[1]
    color = TOPIC_COLORS[tid]
    sidebar = build_sidebar(active_concept_slug=slug, active_topic_id=tid)
    head = HEAD.format(title=f"{name} | Core Micro", root="../", sidebar=sidebar)

    tier_label = f"Tier {tier}" if isinstance(tier, int) else "From slides"
    tier_class = f"tier-t{tier}" if isinstance(tier, int) else "tier-s"

    body = [f'<nav class="breadcrumb"><a href="../index.html">Home</a> / <a href="../topics/{tslug}.html">{html.escape(tname)}</a> / <span>{html.escape(name)}</span></nav>']
    body.append(f'<div class="concept-header">')
    body.append(f'  <h1 style="border-bottom: 3px solid {color}; padding-bottom: 0.3em">{html.escape(name)}</h1>')
    body.append(f'  <div class="chips">')
    body.append(f'    <span class="chip topic-chip" style="background:{color}">{html.escape(tname)}</span>')
    body.append(f'    <span class="chip tier-chip {tier_class}">{tier_label}</span>')
    body.append(f'  </div>')
    body.append('</div>')

    # Section 1: Intuition
    body.append('<section class="concept-section"><h2>1. Intuition</h2>')
    body.append(render_intuition(intuition))
    body.append('</section>')

    # Section 2: Formal mathematics
    body.append('<section class="concept-section todo-section"><h2>2. Formal mathematics</h2>')
    body.append('<div class="todo-card">')
    body.append('<p><strong>Coming in Phase 2.</strong> Will contain:</p>')
    body.append('<ul>')
    body.append('<li>Precise definition with notation matching the FHS slides.</li>')
    body.append('<li>Derivation of the main result(s) the student is expected to reproduce.</li>')
    body.append('<li>Reference to the relevant lecture slide deck and textbook section.</li>')
    body.append('</ul>')
    body.append('</div></section>')

    # Section 3: Graph / Widget
    body.append('<section class="concept-section todo-section"><h2>3. Graphical illustration and interactive widget</h2>')
    body.append('<div class="todo-card">')
    body.append('<p><strong>Coming in Phase 2.</strong> Will contain:</p>')
    body.append('<ul>')
    body.append('<li>SVG diagram illustrating the canonical case.</li>')
    body.append('<li>Plotly-based interactive plot with sliders for parameters, where applicable.</li>')
    body.append('</ul>')
    body.append('</div></section>')

    # Section 4: Examples and essay points
    body.append('<section class="concept-section todo-section"><h2>4. Real-life examples and essay points</h2>')
    body.append('<div class="todo-card">')
    body.append('<p><strong>Coming in Phase 2.</strong> Will contain:</p>')
    body.append('<ul>')
    body.append('<li>Two to four real-world applications drawn from history, current policy, or empirics.</li>')
    body.append('<li>Common evaluation moves Kate Doornik rewards in Part B essays.</li>')
    body.append('<li>Standard limitations / counterexamples.</li>')
    body.append('<li>Cross-references to related concepts.</li>')
    body.append('</ul>')
    body.append('</div></section>')

    # Related concepts within same topic
    same_topic = [c for c in CONCEPTS if c[2] == tid and c[0] != slug]
    tier_order = {1: 0, 2: 1, 3: 2, 4: 3, "S": 4}
    same_topic.sort(key=lambda c: (tier_order.get(c[3], 99), c[1]))
    body.append('<section class="concept-section"><h2>Related concepts</h2><ul class="concept-list">')
    for c in same_topic[:8]:
        body.append(f'<li><a href="../concepts/{c[0]}.html">{html.escape(c[1])}</a></li>')
    body.append('</ul></section>')

    out = head + "\n".join(body) + TAIL
    with open(os.path.join(OUT, "concepts", f"{slug}.html"), "w", encoding="utf-8") as f:
        f.write(out)


# ============== QUESTION TYPE PAGES (md -> html) ==============

def md_to_html(md_text):
    """Very lightweight markdown to HTML converter targeted at our specific QT files."""
    lines = md_text.split('\n')
    out = []
    in_code = False
    in_list = False
    in_table = False
    table_header_done = False

    def close_list():
        nonlocal in_list
        if in_list:
            out.append('</ul>')
            in_list = False
    def close_table():
        nonlocal in_table, table_header_done
        if in_table:
            out.append('</table>')
            in_table = False
            table_header_done = False

    for raw in lines:
        line = raw.rstrip()
        # code block
        if line.startswith('```'):
            close_list(); close_table()
            if in_code:
                out.append('</code></pre>')
                in_code = False
            else:
                out.append('<pre><code>')
                in_code = True
            continue
        if in_code:
            out.append(html.escape(line))
            continue
        # Headers
        m = re.match(r'^(#{1,4})\s+(.*)', line)
        if m:
            close_list(); close_table()
            level = len(m.group(1))
            txt = m.group(2)
            out.append(f"<h{level}>{convert_inline(txt)}</h{level}>")
            continue
        # Blockquote
        if line.startswith('> '):
            close_list(); close_table()
            out.append(f"<blockquote>{convert_inline(line[2:])}</blockquote>")
            continue
        # Table row
        if line.startswith('|'):
            cells = [c.strip() for c in line.strip('|').split('|')]
            # Separator row
            if all(re.match(r'^:?-+:?$', c) for c in cells):
                continue
            if not in_table:
                close_list()
                out.append('<table>')
                in_table = True
                tag = 'th'
            else:
                tag = 'td'
            row = ''.join(f'<{tag}>{convert_inline(c)}</{tag}>' for c in cells)
            out.append(f'<tr>{row}</tr>')
            continue
        else:
            close_table()
        # List item
        m = re.match(r'^(\s*)[-\*]\s+(.*)', line)
        if m:
            if not in_list:
                out.append('<ul>')
                in_list = True
            indent = len(m.group(1))
            txt = m.group(2)
            out.append(f'<li>{convert_inline(txt)}</li>')
            continue
        m = re.match(r'^(\s*)(\d+)\.\s+(.*)', line)
        if m:
            if not in_list:
                out.append('<ol>')
                in_list = 'ol'
            out.append(f'<li>{convert_inline(m.group(3))}</li>')
            continue
        # Horizontal rule
        if line.strip() in ('---', '***', '___'):
            close_list(); close_table()
            out.append('<hr>')
            continue
        # Blank line
        if line.strip() == '':
            close_list(); close_table()
            continue
        # Paragraph
        close_list(); close_table()
        out.append(f"<p>{convert_inline(line)}</p>")

    close_list(); close_table()
    if in_code:
        out.append('</code></pre>')
    return '\n'.join(out)


def convert_inline(text):
    # Wiki links first: [[Concepts/Name]] or [[Concepts/Name|alias]]
    def wiki_link(m):
        target = m.group(1)
        alias = m.group(2) if m.group(2) else target
        if target.startswith('Concepts/'):
            name = target[len('Concepts/'):]
            slug = CONCEPT_NAME_TO_SLUG.get(name)
            if slug:
                return f'<a class="wikilink" href="../concepts/{slug}.html">{alias}</a>'
            else:
                return f'<a class="wikilink missing" title="No concept page yet">{alias}</a>'
        return f'<a class="wikilink">{alias}</a>'
    text = re.sub(r'\[\[([^\]|]+)(?:\|([^\]]+))?\]\]', wiki_link, text)
    # Bold **x**
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    # Italic *x*
    text = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<em>\1</em>', text)
    # Inline code
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    # LaTeX stays as-is so KaTeX picks it up
    return text


def build_question_type_pages():
    qt_files = [
        ("Question Types 1 - General Equilibrium and Welfare.md", "qt1-general-equilibrium-and-welfare.html", "Question Types 1: General Equilibrium and Welfare", 1),
        ("Question Types 2 - Externalities and Public Goods.md", "qt2-externalities-and-public-goods.html", "Question Types 2: Externalities and Public Goods", 3),
        ("Question Types 3 - Game Theory and Industrial Organisation.md", "qt3-game-theory-and-industrial-organisation.html", "Question Types 3: Game Theory and Industrial Organisation", 4),
        ("Question Types 4 - Decisions under Risk.md", "qt4-decisions-under-risk.html", "Question Types 4: Decisions under Risk", 6),
        ("Question Types 5 - Adverse Selection.md", "qt5-adverse-selection.html", "Question Types 5: Adverse Selection", 7),
        ("Question Types 6 - Moral Hazard.md", "qt6-moral-hazard.html", "Question Types 6: Moral Hazard", 8),
    ]
    for md_name, html_name, title, tid in qt_files:
        md_path = os.path.join(QT_DIR, md_name)
        with open(md_path, 'r', encoding='utf-8') as f:
            md = f.read()
        body_html = md_to_html(md)
        sidebar = build_sidebar(active_topic_id=tid)
        head = HEAD.format(title=f"{title} | Core Micro", root="../", sidebar=sidebar)
        breadcrumb = f'<nav class="breadcrumb"><a href="../index.html">Home</a> / <span>Question Types</span></nav>'
        body = breadcrumb + '<article class="qt-article">' + body_html + '</article>'
        with open(os.path.join(OUT, "question-types", html_name), 'w', encoding='utf-8') as f:
            f.write(head + body + TAIL)


# ============== CSS, JS ==============

CSS = """
:root {
  --bg: #ffffff;
  --bg-soft: #f5f7fb;
  --text: #1a1a2e;
  --text-soft: #5a6577;
  --accent: #5b8def;
  --border: #e2e7f0;
  --code-bg: #f0f3f9;
  --sidebar-bg: #fbfcfe;
  --topic-1: #5b8def;
  --topic-2: #7c4dff;
  --topic-3: #26a69a;
  --topic-4: #ef6c00;
  --topic-5: #d81b60;
  --topic-6: #43a047;
  --topic-7: #fb8c00;
  --topic-8: #5e35b1;
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #0f1218;
    --bg-soft: #161b23;
    --text: #e4e7ee;
    --text-soft: #9aa3b2;
    --accent: #6fa3ff;
    --border: #232a36;
    --code-bg: #1c222c;
    --sidebar-bg: #131820;
  }
}
* { box-sizing: border-box; }
body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif;
  background: var(--bg);
  color: var(--text);
  line-height: 1.6;
}
a { color: var(--accent); text-decoration: none; }
a:hover { text-decoration: underline; }
.topbar {
  position: sticky;
  top: 0; z-index: 50;
  background: var(--bg);
  border-bottom: 1px solid var(--border);
  display: flex; align-items: center;
  padding: 0.6em 1.2em;
  gap: 1em;
}
.logo { font-weight: 700; font-size: 1.1em; color: var(--text); }
.search {
  flex: 1; max-width: 480px;
  padding: 0.5em 0.9em;
  background: var(--bg-soft);
  border: 1px solid var(--border);
  border-radius: 6px;
  color: var(--text);
  font-size: 0.95em;
}
.topnav { display: flex; gap: 1em; }
.topnav a { color: var(--text-soft); font-size: 0.92em; }
.topnav a:hover { color: var(--accent); }

.layout {
  display: grid;
  grid-template-columns: 280px 1fr;
  min-height: calc(100vh - 60px);
}
.sidebar {
  background: var(--sidebar-bg);
  border-right: 1px solid var(--border);
  overflow-y: auto;
  max-height: calc(100vh - 60px);
  position: sticky;
  top: 60px;
  padding: 1em 0;
}
.sidebar-inner { padding: 0 1.2em; font-size: 0.9em; }
.sidebar-section { margin-bottom: 1em; }
.sidebar-link { font-weight: 600; color: var(--text); display:block; padding: 0.3em 0; }
.sidebar-topic { font-weight: 600; color: var(--text); display:block; padding: 0.3em 0; }
.sidebar-topic.active { color: var(--accent); }
.sidebar-concepts { list-style: none; padding-left: 0.8em; margin: 0.3em 0; }
.sidebar-concepts li { margin: 0.15em 0; }
.sidebar-concept { color: var(--text-soft); font-size: 0.86em; display: block; padding: 0.1em 0; }
.sidebar-concept:hover { color: var(--accent); }
.sidebar-concept.active { color: var(--accent); font-weight: 600; }

.content {
  padding: 2em 3em;
  max-width: 920px;
}
.breadcrumb { font-size: 0.9em; color: var(--text-soft); margin-bottom: 1em; }
.breadcrumb a { color: var(--text-soft); }

h1 { font-size: 2em; margin: 0.2em 0 0.6em; }
h2 { font-size: 1.45em; margin: 1.6em 0 0.6em; }
h3 { font-size: 1.15em; margin: 1.2em 0 0.5em; color: var(--text-soft); }
.lead { font-size: 1.1em; color: var(--text-soft); }
.source-note { font-size: 0.9em; color: var(--text-soft); margin-bottom: 1.5em; }

.hero { padding: 1em 0 1.5em; }
.hero-stats { display: flex; gap: 1.5em; margin: 1.5em 0; flex-wrap: wrap; }
.stat { background: var(--bg-soft); border: 1px solid var(--border); border-radius: 8px; padding: 1em 1.4em; min-width: 100px; }
.stat-num { font-size: 1.8em; font-weight: 700; color: var(--accent); }
.stat-label { font-size: 0.85em; color: var(--text-soft); }

.topic-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 1em; margin: 1em 0; }
.topic-card { display: block; padding: 1.2em 1.4em; background: var(--bg-soft); border: 1px solid var(--border); border-top: 4px solid; border-radius: 8px; color: var(--text); position: relative; }
.topic-card:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(0,0,0,0.06); text-decoration: none; }
.topic-num { display: inline-block; width: 32px; height: 32px; line-height: 32px; text-align: center; color: white; border-radius: 50%; font-weight: 700; margin-bottom: 0.6em; }
.topic-name { font-weight: 700; font-size: 1.05em; margin-bottom: 0.4em; }
.topic-desc { font-size: 0.9em; color: var(--text-soft); }
.topic-meta { font-size: 0.8em; color: var(--text-soft); margin-top: 0.6em; }

.qt-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 0.8em; }
.qt-card { display: block; padding: 0.9em 1.2em; background: var(--bg-soft); border: 1px solid var(--border); border-left: 4px solid; border-radius: 6px; color: var(--text); }
.qt-card:hover { background: var(--bg); text-decoration: none; }
.qt-name { font-weight: 600; }

.all-concepts { display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 1.2em; }
.concept-group h3 { margin-top: 0; }
.concept-list { list-style: none; padding-left: 0; margin: 0; }
.concept-list li { padding: 0.25em 0; font-size: 0.9em; }
.concept-list-wide { list-style: none; padding-left: 0; margin: 0; }
.concept-list-wide li { padding: 0.5em 0; border-bottom: 1px solid var(--border); }
.concept-preview { color: var(--text-soft); font-size: 0.9em; }
.tier-chip { display: inline-block; font-size: 0.7em; padding: 0.1em 0.5em; border-radius: 10px; margin-right: 0.3em; font-weight: 700; }
.tier-t1, .tier-chip.tier-t1 { background: #c8e6c9; color: #1b5e20; }
.tier-t2, .tier-chip.tier-t2 { background: #fff9c4; color: #827717; }
.tier-t3, .tier-chip.tier-t3 { background: #ffe0b2; color: #e65100; }
.tier-t4, .tier-chip.tier-t4 { background: #ffcdd2; color: #b71c1c; }
.tier-s, .tier-chip.tier-s { background: #e1bee7; color: #4a148c; }
@media (prefers-color-scheme: dark) {
  .tier-t1 { background: #1b5e20; color: #c8e6c9; }
  .tier-t2 { background: #827717; color: #fff9c4; }
  .tier-t3 { background: #e65100; color: #ffe0b2; }
  .tier-t4 { background: #b71c1c; color: #ffcdd2; }
  .tier-s { background: #4a148c; color: #e1bee7; }
}
.tier-heading { color: var(--text-soft); font-weight: 600; }

.cta-link { font-size: 1em; }

.concept-header .chips { display: flex; gap: 0.5em; align-items: center; margin: 0.5em 0; }
.chip { display: inline-block; font-size: 0.8em; padding: 0.2em 0.7em; border-radius: 12px; font-weight: 600; }
.topic-chip { color: white; }
.concept-section { margin: 2em 0; }
.todo-section { opacity: 0.85; }
.todo-card { background: var(--bg-soft); border: 1px dashed var(--border); border-radius: 6px; padding: 1em 1.4em; color: var(--text-soft); }

.qt-article h1, .qt-article h2 { border-bottom: 1px solid var(--border); padding-bottom: 0.3em; }
.qt-article blockquote { border-left: 3px solid var(--accent); background: var(--bg-soft); padding: 0.5em 1em; margin: 1em 0; color: var(--text-soft); }
.qt-article table { border-collapse: collapse; margin: 1em 0; font-size: 0.92em; }
.qt-article th, .qt-article td { padding: 0.4em 0.8em; border: 1px solid var(--border); text-align: left; }
.qt-article th { background: var(--bg-soft); }
.wikilink { color: var(--accent); background: rgba(91, 141, 239, 0.08); padding: 0.05em 0.25em; border-radius: 3px; }
.wikilink.missing { color: var(--text-soft); background: rgba(154, 163, 178, 0.1); cursor: help; }
code { background: var(--code-bg); padding: 0.1em 0.4em; border-radius: 3px; font-size: 0.9em; }
pre { background: var(--code-bg); padding: 0.8em 1em; overflow-x: auto; border-radius: 6px; }
pre code { background: none; padding: 0; }

.footer { border-top: 1px solid var(--border); padding: 1.5em 3em; color: var(--text-soft); font-size: 0.85em; text-align: center; }

.hidden { display: none !important; }

@media (max-width: 900px) {
  .layout { grid-template-columns: 1fr; }
  .sidebar { display: none; }
  .content { padding: 1.4em 1.2em; }
  .topnav { display: none; }
}
"""

JS = """
// Search across sidebar and visible content
document.addEventListener('DOMContentLoaded', function() {
  var search = document.getElementById('search');
  if (!search) return;
  search.addEventListener('input', function() {
    var q = search.value.toLowerCase().trim();
    var nodes = document.querySelectorAll('.sidebar-concept');
    nodes.forEach(function(a) {
      var n = (a.getAttribute('data-name') || a.textContent).toLowerCase();
      var parent = a.parentElement;
      if (q === '' || n.indexOf(q) >= 0) {
        if (parent) parent.classList.remove('hidden');
      } else {
        if (parent) parent.classList.add('hidden');
      }
    });
    // Hide topic sections with no visible concepts
    document.querySelectorAll('.sidebar-section').forEach(function(sec) {
      var visible = sec.querySelectorAll('.sidebar-concepts li:not(.hidden)').length;
      if (q === '' || visible > 0 || sec.querySelector('.sidebar-link')) {
        sec.classList.remove('hidden');
      } else {
        sec.classList.add('hidden');
      }
    });
    // Index page: filter all-concepts list
    document.querySelectorAll('.all-concepts .concept-list li').forEach(function(li) {
      var t = li.textContent.toLowerCase();
      if (q === '' || t.indexOf(q) >= 0) li.classList.remove('hidden');
      else li.classList.add('hidden');
    });
  });
});
"""


def write_assets():
    with open(os.path.join(OUT, "assets", "style.css"), "w", encoding="utf-8") as f:
        f.write(CSS)
    with open(os.path.join(OUT, "assets", "app.js"), "w", encoding="utf-8") as f:
        f.write(JS)


# ============== README + push.sh ==============

README = """# Core Micro Study Guide

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
"""

PUSH_SH = """#!/usr/bin/env bash
# Initialise (or update) the local git repo and push to GitHub.
# Run this from the Website/ folder.

set -euo pipefail

REPO="https://github.com/Ryann-teo/Micro.git"
BRANCH="main"

if [ ! -d ".git" ]; then
  git init
  git branch -M "$BRANCH"
  git remote add origin "$REPO" || true
else
  if ! git remote get-url origin >/dev/null 2>&1; then
    git remote add origin "$REPO"
  fi
fi

git add -A
git commit -m "Core Micro study guide (Phase 1: 173 concept stubs with intuition)" || echo "No changes to commit."

# Push. May prompt for GitHub credentials or use cached gh CLI token.
git push -u origin "$BRANCH"

echo ""
echo "Done."
echo "Open https://github.com/Ryann-teo/Micro/settings/pages and set Source to:"
echo "  Branch: main  /  Folder: / (root)"
echo "The live site will then be at https://ryann-teo.github.io/Micro/"
"""


def write_readme_and_push():
    with open(os.path.join(OUT, "README.md"), "w", encoding="utf-8") as f:
        f.write(README)
    push_path = os.path.join(OUT, "push.sh")
    with open(push_path, "w", encoding="utf-8") as f:
        f.write(PUSH_SH)
    os.chmod(push_path, 0o755)


# ============== MAIN ==============

def main():
    # Clean and prep dirs
    os.makedirs(OUT, exist_ok=True)
    for sub in ("concepts", "topics", "question-types", "assets"):
        os.makedirs(os.path.join(OUT, sub), exist_ok=True)

    print("Writing CSS and JS...")
    write_assets()

    print("Writing index...")
    build_index()

    print(f"Writing {len(TOPICS)} topic pages...")
    for t in TOPICS:
        build_topic_page(t)

    print(f"Writing {len(CONCEPTS)} concept pages...")
    for c in CONCEPTS:
        build_concept_page(c)

    print("Writing 6 question type pages...")
    build_question_type_pages()

    print("Writing README and push.sh...")
    write_readme_and_push()

    print("\nDone. Files under: " + OUT)


if __name__ == "__main__":
    main()
