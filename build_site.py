"""Single-page Core Micro study dashboard.

Produces one big index.html containing:
- All 173 concepts as collapsible cards, with 4 inline sections (intuition / math / widget / examples).
- All 6 Question Typing files merged inline, organised by topic, with collapsible Part A / Part B Essay / Part B Long subsections.
- Sidebar with collapsible per-topic dropdowns. Each dropdown lists Question Types entries + concepts.
- Wiki links go to in-page anchors (#concept-<slug>) that auto-expand the target card.

Plus assets/style.css and assets/app.js.
"""

import os
import re
import html
from concepts_data import TOPICS, CONCEPTS
try:
    from phase2_content import PHASE2
except Exception:
    PHASE2 = {}

OUT = "/sessions/exciting-upbeat-davinci/mnt/Big Brain/Areas/Economics/Core Micro/Website"
QT_DIR = "/sessions/exciting-upbeat-davinci/mnt/Big Brain/Areas/Economics/Core Micro/Study Guide/Question Types"


def slugify(name: str) -> str:
    s = name.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s


CONCEPT_NAME_TO_SLUG = {c[1]: c[0] for c in CONCEPTS}


def topic_slug(t):
    return f"{t[0]}-{slugify(t[1])}"


TOPIC_COLORS = {
    1: "#5b8def", 2: "#7c4dff", 3: "#26a69a", 4: "#ef6c00",
    5: "#d81b60", 6: "#43a047", 7: "#fb8c00", 8: "#5e35b1",
}

# Topic -> QT file mapping (some topics share a QT file)
TOPIC_TO_QT = {
    1: "qt1", 2: "qt1",
    3: "qt2",
    4: "qt3", 5: "qt3",
    6: "qt4",
    7: "qt5",
    8: "qt6",
}

QT_FILES = [
    ("qt1", "Question Types 1 - General Equilibrium and Welfare.md", "General Equilibrium and Welfare", [1, 2]),
    ("qt2", "Question Types 2 - Externalities and Public Goods.md", "Externalities and Public Goods", [3]),
    ("qt3", "Question Types 3 - Game Theory and Industrial Organisation.md", "Game Theory and Industrial Organisation", [4, 5]),
    ("qt4", "Question Types 4 - Decisions under Risk.md", "Decisions under Risk", [6]),
    ("qt5", "Question Types 5 - Adverse Selection.md", "Adverse Selection", [7]),
    ("qt6", "Question Types 6 - Moral Hazard.md", "Moral Hazard", [8]),
]


# ============== Markdown to HTML, with wiki link to anchor rewrite ==============

def convert_inline(text):
    def wiki_link(m):
        target = m.group(1)
        alias = m.group(2) if m.group(2) else target
        if target.startswith('Concepts/'):
            name = target[len('Concepts/'):]
            slug = CONCEPT_NAME_TO_SLUG.get(name)
            if slug:
                return f'<a class="wikilink" href="#concept-{slug}" onclick="openConcept(\'{slug}\')">{alias}</a>'
            return f'<a class="wikilink missing" title="No concept page yet">{alias}</a>'
        return f'<a class="wikilink">{alias}</a>'
    text = re.sub(r'\[\[([^\]|]+)(?:\|([^\]]+))?\]\]', wiki_link, text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<em>\1</em>', text)
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    return text


def md_to_html(md_text):
    """Convert QT markdown into HTML with collapsible <details> for big-question and sub-question types."""
    lines = md_text.split('\n')
    out = []
    in_code = False
    in_list = False
    list_kind = None
    in_table = False
    pending_para = []

    def flush_para():
        if pending_para:
            out.append('<p>' + convert_inline(' '.join(pending_para)) + '</p>')
            pending_para.clear()

    def close_list():
        nonlocal in_list, list_kind
        if in_list:
            tag = 'ol' if list_kind == 'ol' else 'ul'
            out.append(f'</{tag}>')
            in_list = False
            list_kind = None

    def close_table():
        nonlocal in_table
        if in_table:
            out.append('</table>')
            in_table = False

    for raw in lines:
        line = raw.rstrip()
        if line.startswith('```'):
            flush_para(); close_list(); close_table()
            if in_code:
                out.append('</code></pre>'); in_code = False
            else:
                out.append('<pre><code>'); in_code = True
            continue
        if in_code:
            out.append(html.escape(line)); continue

        m = re.match(r'^(#{1,4})\s+(.*)', line)
        if m:
            flush_para(); close_list(); close_table()
            level = len(m.group(1))
            txt = m.group(2)
            # Convert ## sections to summaries inside details for collapsibility
            # We'll rely on the QT-file structure: H2 = "Part A: ..." / "Part B: essays" / etc; H3 = sub-question type
            out.append(f"<h{level}>{convert_inline(txt)}</h{level}>")
            continue
        if line.startswith('> '):
            flush_para(); close_list(); close_table()
            out.append(f"<blockquote>{convert_inline(line[2:])}</blockquote>")
            continue
        if line.startswith('|'):
            flush_para(); close_list()
            cells = [c.strip() for c in line.strip('|').split('|')]
            if all(re.match(r'^:?-+:?$', c) for c in cells):
                continue
            if not in_table:
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
        m = re.match(r'^(\s*)[-\*]\s+(.*)', line)
        if m:
            flush_para()
            if not in_list:
                out.append('<ul>'); in_list = True; list_kind = 'ul'
            elif list_kind == 'ol':
                close_list(); out.append('<ul>'); in_list = True; list_kind = 'ul'
            out.append(f'<li>{convert_inline(m.group(2))}</li>')
            continue
        m = re.match(r'^(\s*)(\d+)\.\s+(.*)', line)
        if m:
            flush_para()
            if not in_list:
                out.append('<ol>'); in_list = True; list_kind = 'ol'
            elif list_kind == 'ul':
                close_list(); out.append('<ol>'); in_list = True; list_kind = 'ol'
            out.append(f'<li>{convert_inline(m.group(3))}</li>')
            continue
        if line.strip() in ('---', '***', '___'):
            flush_para(); close_list(); close_table()
            out.append('<hr>')
            continue
        if line.strip() == '':
            flush_para(); close_list()
            continue
        # Regular paragraph line: accumulate
        if pending_para and in_list:
            close_list()
        pending_para.append(line.strip())

    flush_para(); close_list(); close_table()
    if in_code:
        out.append('</code></pre>')
    return '\n'.join(out)


def structure_qt_html(raw_html: str) -> str:
    """Transform the converted QT HTML into a structure with collapsible details per H2 and H3 section.

    Pattern (post-conversion):
      <h1>...</h1>                  (page title — keep)
      <blockquote>intro</blockquote>
      <hr>
      <h2>Excluded sub-topics</h2>  -> details
      <h2>Part A: ...</h2>          -> details, with H3 children as nested details
      <h2>Part B: essays</h2>       -> details
      <h2>Part B: long-answer</h2>  -> details
      <h2>How to recognise...</h2>  -> details
      <h2>Applied procedures</h2>   -> details (if present)

    The H3 sections inside each Part X H2 should also collapse.
    """
    # Split into tokens by line; we'll re-emit grouped under <details>.
    nodes = re.split(r'(?=<h[12]\b|<hr>)', raw_html)
    out = []
    open_h2 = False
    open_h3 = False

    for chunk in nodes:
        if not chunk.strip():
            continue
        # H1: keep as-is (top header)
        if chunk.startswith('<h1'):
            # close any open sections
            if open_h3:
                out.append('</div></details>'); open_h3 = False
            if open_h2:
                out.append('</div></details>'); open_h2 = False
            out.append(chunk)
            continue
        if chunk.startswith('<hr>'):
            continue  # drop horizontal rules; details borders do the job
        if chunk.startswith('<h2'):
            # Close prior open sections
            if open_h3:
                out.append('</div></details>'); open_h3 = False
            if open_h2:
                out.append('</div></details>'); open_h2 = False
            # Parse heading text out of <h2>...</h2>...
            m = re.match(r'<h2[^>]*>(.*?)</h2>(.*)', chunk, re.DOTALL)
            if not m:
                out.append(chunk); continue
            heading = m.group(1)
            rest = m.group(2)
            # Decide whether to open the details by default
            open_attr = ' open' if 'Part A' in heading else ''
            out.append(f'<details class="qt-section"{open_attr}><summary>{heading}</summary><div class="qt-section-body">')
            open_h2 = True
            # Now split rest into H3 chunks
            sub = re.split(r'(?=<h3\b)', rest)
            for sc in sub:
                sc = sc.strip()
                if not sc:
                    continue
                if sc.startswith('<h3'):
                    if open_h3:
                        out.append('</div></details>')
                        open_h3 = False
                    m3 = re.match(r'<h3[^>]*>(.*?)</h3>(.*)', sc, re.DOTALL)
                    if m3:
                        h3_text = m3.group(1)
                        h3_rest = m3.group(2)
                        out.append(f'<details class="qt-sub"><summary>{h3_text}</summary><div class="qt-sub-body">')
                        out.append(h3_rest)
                        open_h3 = True
                    else:
                        out.append(sc)
                else:
                    out.append(sc)
        else:
            out.append(chunk)

    if open_h3:
        out.append('</div></details>')
    if open_h2:
        out.append('</div></details>')
    return '\n'.join(out)


def load_qt_html(slug: str) -> str:
    fn = next((f for f in QT_FILES if f[0] == slug), None)
    if not fn:
        return ''
    with open(os.path.join(QT_DIR, fn[1]), 'r', encoding='utf-8') as f:
        md = f.read()
    return structure_qt_html(md_to_html(md))


# ============== Concept card rendering ==============

def render_concept_card(concept):
    slug, name, tid, tier, intuition = concept[0], concept[1], concept[2], concept[3], concept[4]
    color = TOPIC_COLORS[tid]
    tier_label = f"Tier {tier}" if isinstance(tier, int) else "From slides"
    tier_cls = f"tier-t{tier}" if isinstance(tier, int) else "tier-s"

    p2 = PHASE2.get(slug, {})
    math_html = p2.get('math')
    widget_html = p2.get('widget')
    examples_html = p2.get('examples')

    intuit_html = ''.join(f'<p>{p}</p>' for p in intuition)

    body = []
    body.append('<div class="concept-tabs">')
    # Tab 1: Intuition
    body.append(f'<div class="tab tab-intuition"><h4>1. Intuition</h4>{intuit_html}</div>')
    # Tab 2: Math
    if math_html:
        body.append(f'<div class="tab tab-math"><h4>2. Formal mathematics</h4>{math_html}</div>')
    else:
        body.append('<div class="tab tab-todo"><h4>2. Formal mathematics</h4><p>Coming in Phase 2 (priority depends on tier).</p></div>')
    # Tab 3: Widget
    if widget_html:
        body.append(f'<div class="tab tab-widget"><h4>3. Graphical illustration</h4>{widget_html}</div>')
    else:
        body.append('<div class="tab tab-todo"><h4>3. Graphical illustration</h4><p>Coming in Phase 2.</p></div>')
    # Tab 4: Examples
    if examples_html:
        body.append(f'<div class="tab tab-examples"><h4>4. Real-life examples and essay points</h4>{examples_html}</div>')
    else:
        body.append('<div class="tab tab-todo"><h4>4. Real-life examples and essay points</h4><p>Coming in Phase 2.</p></div>')
    body.append('</div>')
    body_str = '\n'.join(body)

    return f'''<details class="concept-card" id="concept-{slug}" data-slug="{slug}" data-topic="{tid}" data-tier="{tier}">
  <summary>
    <span class="concept-pill" style="background:{color}">{tid}</span>
    <span class="concept-name">{html.escape(name)}</span>
    <span class="tier-chip {tier_cls}">{tier_label}</span>
  </summary>
  <div class="concept-body">{body_str}</div>
</details>'''


# ============== Sidebar ==============

def build_sidebar():
    parts = ['<div class="sidebar-inner">',
             '<input id="search" class="search" type="text" placeholder="Search concepts and questions..." autocomplete="off">']
    for t in TOPICS:
        tid, tname, _, _ = t
        qt_slug = TOPIC_TO_QT[tid]
        color = TOPIC_COLORS[tid]
        parts.append(f'<details class="side-topic" data-topic-id="{tid}">')
        parts.append(f'  <summary class="side-topic-summary" style="border-left-color:{color}">'
                     f'<span class="side-topic-num" style="background:{color}">{tid}</span>'
                     f'<span class="side-topic-name">{html.escape(tname)}</span></summary>')
        parts.append('  <div class="side-topic-body">')
        # Question Types sub-block
        parts.append(f'    <details class="side-subblock">')
        parts.append(f'      <summary class="side-subblock-summary">Question Types</summary>')
        parts.append(f'      <ul class="side-list">')
        parts.append(f'        <li><a href="#qt-{qt_slug}-part-a" class="side-link" data-anchor="qt-{qt_slug}-part-a">Part A: short problems</a></li>')
        parts.append(f'        <li><a href="#qt-{qt_slug}-part-b-essays" class="side-link" data-anchor="qt-{qt_slug}-part-b-essays">Part B: essays</a></li>')
        parts.append(f'        <li><a href="#qt-{qt_slug}-part-b-long" class="side-link" data-anchor="qt-{qt_slug}-part-b-long">Part B: long answers</a></li>')
        parts.append(f'      </ul></details>')
        # Concepts sub-block
        topic_concepts = [c for c in CONCEPTS if c[2] == tid]
        tier_order = {1: 0, 2: 1, 3: 2, 4: 3, "S": 4}
        topic_concepts.sort(key=lambda c: (tier_order.get(c[3], 99), c[1]))
        parts.append(f'    <details class="side-subblock">')
        parts.append(f'      <summary class="side-subblock-summary">Concepts ({len(topic_concepts)})</summary>')
        parts.append(f'      <ul class="side-list">')
        for c in topic_concepts:
            slug, nm = c[0], c[1]
            parts.append(f'        <li><a href="#concept-{slug}" class="side-link" data-anchor="concept-{slug}" data-name="{html.escape(nm)}">{html.escape(nm)}</a></li>')
        parts.append(f'      </ul></details>')
        parts.append('  </div></details>')
    parts.append('</div>')
    return '\n'.join(parts)


# ============== Main page ==============

def build_index():
    sidebar = build_sidebar()

    # Hero
    body = [
        '<section class="hero">',
        '<h1>Core Microeconomics</h1>',
        '<p class="lead">Single-page revision dashboard. All 173 concepts and every past-paper question type 2014 to 2025 in one place. Click any wiki-link to jump to a concept card; click any topic in the sidebar to expand its question types and concept list.</p>',
        '<div class="hero-stats">',
        '<div class="stat"><div class="stat-num">173</div><div class="stat-label">Concepts</div></div>',
        '<div class="stat"><div class="stat-num">8</div><div class="stat-label">Topics</div></div>',
        '<div class="stat"><div class="stat-num">76</div><div class="stat-label">Past Questions</div></div>',
        '<div class="stat"><div class="stat-num">11</div><div class="stat-label">Past Papers</div></div>',
        '</div>',
        '</section>',
    ]

    # Pre-load all QT HTML
    qt_html_by_slug = {slug: load_qt_html(slug) for slug, _, _, _ in QT_FILES}

    rendered_qt_slugs = set()

    for t in TOPICS:
        tid, tname, tdesc, tsource = t
        color = TOPIC_COLORS[tid]
        qt_slug = TOPIC_TO_QT[tid]
        body.append(f'<section class="topic-section" id="topic-{tid}" data-topic-id="{tid}">')
        body.append(f'<h2 class="topic-h2" style="border-left:6px solid {color}; padding-left:.6em">'
                    f'<span class="topic-h2-num" style="background:{color}">{tid}</span> {html.escape(tname)}</h2>')
        body.append(f'<p class="topic-desc">{html.escape(tdesc)}</p>')
        body.append(f'<p class="source-note"><strong>Source:</strong> {html.escape(tsource)}</p>')

        # Question Types block (one per QT file; if a QT covers multiple topics, render once for the first topic that touches it)
        if qt_slug not in rendered_qt_slugs:
            rendered_qt_slugs.add(qt_slug)
            qt_meta = next(q for q in QT_FILES if q[0] == qt_slug)
            qt_title = qt_meta[2]
            qt_inner = qt_html_by_slug[qt_slug]
            # Inject anchors before each Part A / Part B Essay / Part B Long section by inspecting summaries
            qt_inner = re.sub(
                r'(<details class="qt-section"[^>]*><summary>)(.*?Part A.*?)(</summary>)',
                lambda m: f'<details class="qt-section" id="qt-{qt_slug}-part-a" open><summary>{m.group(2)}{m.group(3)}',
                qt_inner, count=1)
            qt_inner = re.sub(
                r'(<details class="qt-section"[^>]*><summary>)(Part B[^<]*essay[^<]*)(</summary>)',
                lambda m: f'<details class="qt-section" id="qt-{qt_slug}-part-b-essays"><summary>{m.group(2)}{m.group(3)}',
                qt_inner, count=1, flags=re.IGNORECASE)
            qt_inner = re.sub(
                r'(<details class="qt-section"[^>]*><summary>)(Part B[^<]*long[^<]*)(</summary>)',
                lambda m: f'<details class="qt-section" id="qt-{qt_slug}-part-b-long"><summary>{m.group(2)}{m.group(3)}',
                qt_inner, count=1, flags=re.IGNORECASE)
            body.append(f'<details class="qt-wrapper" open id="qt-block-{qt_slug}">')
            body.append(f'  <summary class="qt-wrapper-summary"><strong>Question Types: {html.escape(qt_title)}</strong> (past papers 2014 to 2025)</summary>')
            body.append(f'  <div class="qt-wrapper-body">{qt_inner}</div>')
            body.append('</details>')

        # Concept cards
        topic_concepts = [c for c in CONCEPTS if c[2] == tid]
        tier_order = {1: 0, 2: 1, 3: 2, 4: 3, "S": 4}
        topic_concepts.sort(key=lambda c: (tier_order.get(c[3], 99), c[1]))
        body.append(f'<h3 class="concepts-heading">Concepts ({len(topic_concepts)})</h3>')
        body.append('<div class="concept-grid">')
        for c in topic_concepts:
            body.append(render_concept_card(c))
        body.append('</div>')
        body.append('</section>')

    head = HEAD.format(title="Core Micro Study Guide")
    out = head + '<div class="layout">' + f'<aside class="sidebar">{sidebar}</aside>' + '<main class="content">' + '\n'.join(body) + '</main></div>' + TAIL
    with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as f:
        f.write(out)


HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="assets/style.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css" crossorigin="anonymous">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js" crossorigin="anonymous"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" crossorigin="anonymous"
  onload="renderMathInElement(document.body,{{delimiters:[{{left:'$$',right:'$$',display:true}},{{left:'$',right:'$',display:false}}],throwOnError:false}});"></script>
<script defer src="https://cdn.plot.ly/plotly-2.32.0.min.js"></script>
<script defer src="assets/app.js"></script>
</head>
<body>
<header class="topbar">
  <a class="logo" href="#">Core Micro</a>
  <nav class="topnav">
    <a href="#topic-1">GE</a>
    <a href="#topic-2">Welfare</a>
    <a href="#topic-3">Externalities</a>
    <a href="#topic-4">Game Theory</a>
    <a href="#topic-5">IO</a>
    <a href="#topic-6">Risk</a>
    <a href="#topic-7">Adverse Selection</a>
    <a href="#topic-8">Moral Hazard</a>
  </nav>
</header>
"""

TAIL = """
<footer class="footer">
  Core Micro Study Guide. Built from past papers 2014 to 2025, FHS lecture slides (Wk1 to Wk7), and Micro2025 reading list.
</footer>
</body>
</html>
"""


# ============== CSS + JS ==============

CSS = """
:root {
  --bg: #fafbfc; --bg-soft: #f4f6fa; --text: #1a202c; --text-soft: #4a5568;
  --accent: #2b6cb0; --border: #e2e8f0; --code-bg: #1a202c; --code-fg: #e2e8f0;
  --sidebar-bg: #fff;
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #0f1218; --bg-soft: #161b23; --text: #e4e7ee; --text-soft: #9aa3b2;
    --accent: #6fa3ff; --border: #232a36; --code-bg: #1c222c;
    --sidebar-bg: #131820;
  }
}
* { box-sizing: border-box; }
body { margin: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif; background: var(--bg); color: var(--text); line-height: 1.55; }
a { color: var(--accent); text-decoration: none; }
a:hover { text-decoration: underline; }

.topbar { position: sticky; top: 0; z-index: 100; background: var(--bg); border-bottom: 1px solid var(--border); display: flex; align-items: center; padding: .55em 1.2em; gap: 1em; }
.logo { font-weight: 700; font-size: 1.05em; color: var(--text); }
.topnav { display: flex; gap: .8em; margin-left: auto; }
.topnav a { color: var(--text-soft); font-size: .88em; }
.topnav a:hover { color: var(--accent); }

.layout { display: grid; grid-template-columns: 300px 1fr; min-height: calc(100vh - 50px); }
.sidebar { background: var(--sidebar-bg); border-right: 1px solid var(--border); overflow-y: auto; max-height: calc(100vh - 50px); position: sticky; top: 50px; padding: .8em 0; }
.sidebar-inner { padding: 0 1em; font-size: .9em; }
.search { width: 100%; padding: .5em .7em; background: var(--bg-soft); border: 1px solid var(--border); border-radius: 5px; color: var(--text); font-size: .92em; margin-bottom: .8em; }

.side-topic { margin-bottom: .35em; }
.side-topic > summary { list-style: none; cursor: pointer; padding: .45em .6em; background: var(--bg-soft); border-radius: 5px; border-left: 4px solid; display: flex; align-items: center; gap: .5em; }
.side-topic > summary::-webkit-details-marker { display: none; }
.side-topic > summary::after { content: "▶"; color: var(--text-soft); font-size: .7em; margin-left: auto; transition: transform .15s; }
.side-topic[open] > summary::after { transform: rotate(90deg); }
.side-topic-num { display: inline-block; width: 22px; height: 22px; text-align: center; line-height: 22px; color: white; border-radius: 50%; font-weight: 700; font-size: .78em; }
.side-topic-name { font-weight: 600; }
.side-topic-body { padding: .4em .3em .5em 1em; }

.side-subblock { margin-top: .3em; }
.side-subblock > summary { list-style: none; cursor: pointer; padding: .25em .4em; font-size: .85em; font-weight: 600; color: var(--text-soft); border-radius: 3px; }
.side-subblock > summary:hover { background: var(--bg-soft); }
.side-subblock > summary::-webkit-details-marker { display: none; }
.side-subblock > summary::before { content: "▸"; margin-right: .35em; transition: transform .15s; display: inline-block; }
.side-subblock[open] > summary::before { transform: rotate(90deg); }
.side-list { list-style: none; padding: .2em 0 0 1.1em; margin: 0; }
.side-list li { padding: .15em 0; font-size: .82em; }
.side-list .side-link { color: var(--text-soft); display: block; padding: .15em .3em; border-radius: 3px; }
.side-list .side-link:hover { background: var(--bg-soft); color: var(--accent); text-decoration: none; }

.content { padding: 1.5em 2.4em; max-width: 1080px; }
.hero { margin-bottom: 2em; }
.hero h1 { font-size: 2em; margin: 0 0 .3em; }
.lead { font-size: 1.05em; color: var(--text-soft); }
.hero-stats { display: flex; gap: 1.2em; margin-top: 1.4em; flex-wrap: wrap; }
.stat { background: var(--bg-soft); border: 1px solid var(--border); border-radius: 8px; padding: .9em 1.3em; min-width: 100px; }
.stat-num { font-size: 1.7em; font-weight: 700; color: var(--accent); }
.stat-label { font-size: .82em; color: var(--text-soft); }

.topic-section { margin: 2.5em 0; padding-top: .5em; }
.topic-h2 { font-size: 1.5em; margin: 0 0 .4em; }
.topic-h2-num { display: inline-block; width: 30px; height: 30px; line-height: 30px; text-align: center; color: white; border-radius: 50%; font-weight: 700; font-size: .75em; margin-right: .3em; vertical-align: middle; }
.topic-desc { color: var(--text-soft); margin-bottom: .4em; }
.source-note { font-size: .85em; color: var(--text-soft); margin-bottom: 1em; }

.concepts-heading { margin: 1.6em 0 .6em; font-size: 1.1em; color: var(--text-soft); }
.concept-grid { display: grid; gap: .6em; }

.concept-card { background: var(--sidebar-bg); border: 1px solid var(--border); border-radius: 7px; overflow: hidden; }
.concept-card > summary { list-style: none; padding: .6em .9em; cursor: pointer; display: flex; align-items: center; gap: .55em; }
.concept-card > summary::-webkit-details-marker { display: none; }
.concept-card > summary::after { content: "▶"; color: var(--text-soft); font-size: .75em; margin-left: auto; transition: transform .15s; }
.concept-card[open] > summary::after { transform: rotate(90deg); }
.concept-card:target { box-shadow: 0 0 0 3px rgba(43,108,176,.35); border-color: var(--accent); }
.concept-pill { display: inline-block; width: 22px; height: 22px; line-height: 22px; text-align: center; color: white; border-radius: 50%; font-weight: 700; font-size: .72em; }
.concept-name { font-weight: 600; }
.tier-chip { display: inline-block; font-size: .68em; padding: .12em .55em; border-radius: 10px; font-weight: 700; margin-left: auto; margin-right: .5em; }
.tier-chip.tier-t1 { background: #c8e6c9; color: #1b5e20; }
.tier-chip.tier-t2 { background: #fff9c4; color: #827717; }
.tier-chip.tier-t3 { background: #ffe0b2; color: #e65100; }
.tier-chip.tier-t4 { background: #ffcdd2; color: #b71c1c; }
.tier-chip.tier-s { background: #e1bee7; color: #4a148c; }
@media (prefers-color-scheme: dark) {
  .tier-chip.tier-t1 { background: #1b5e20; color: #c8e6c9; }
  .tier-chip.tier-t2 { background: #827717; color: #fff9c4; }
  .tier-chip.tier-t3 { background: #e65100; color: #ffe0b2; }
  .tier-chip.tier-t4 { background: #b71c1c; color: #ffcdd2; }
  .tier-chip.tier-s { background: #4a148c; color: #e1bee7; }
}

.concept-body { padding: 0 .9em 1em; border-top: 1px solid var(--border); background: var(--bg); }
.concept-tabs { display: flex; flex-direction: column; gap: .7em; margin-top: .8em; }
.tab { padding: .7em 1em; border-radius: 6px; border-left: 4px solid; background: var(--bg-soft); }
.tab h4 { font-size: .8em; text-transform: uppercase; letter-spacing: .08em; margin: 0 0 .4em; color: var(--text-soft); font-weight: 700; }
.tab.tab-intuition { border-left-color: #d69e2e; background: #fffbea; }
.tab.tab-math { border-left-color: #2c5282; background: #ebf4ff; }
.tab.tab-widget { border-left-color: #805ad5; background: #faf5ff; }
.tab.tab-examples { border-left-color: #38a169; background: #f0fff4; }
.tab.tab-todo { border-left-color: var(--text-soft); background: var(--bg-soft); opacity: .8; }
@media (prefers-color-scheme: dark) {
  .tab.tab-intuition { background: #2a2516; }
  .tab.tab-math { background: #182539; }
  .tab.tab-widget { background: #281d3a; }
  .tab.tab-examples { background: #17291d; }
  .tab.tab-todo { background: var(--bg-soft); }
}
.tab p { margin: .4em 0; }
.tab .katex-display { margin: .6em 0; padding: .2em 0; overflow-x: auto; }

.qt-wrapper { background: var(--sidebar-bg); border: 1px solid var(--border); border-radius: 8px; margin: 1em 0; overflow: hidden; }
.qt-wrapper > summary { list-style: none; padding: .8em 1.1em; cursor: pointer; background: var(--bg-soft); display: flex; align-items: center; }
.qt-wrapper > summary::-webkit-details-marker { display: none; }
.qt-wrapper > summary::after { content: "▶"; color: var(--text-soft); font-size: .8em; margin-left: auto; transition: transform .15s; }
.qt-wrapper[open] > summary::after { transform: rotate(90deg); }
.qt-wrapper-body { padding: .8em 1.1em; }
.qt-section { margin: .5em 0; border: 1px solid var(--border); border-radius: 6px; background: var(--bg); }
.qt-section > summary { list-style: none; padding: .65em .9em; cursor: pointer; font-weight: 600; color: var(--accent); background: var(--bg-soft); border-radius: 6px; display: flex; align-items: center; }
.qt-section > summary::-webkit-details-marker { display: none; }
.qt-section > summary::after { content: "▶"; color: var(--text-soft); font-size: .75em; margin-left: auto; transition: transform .15s; }
.qt-section[open] > summary::after { transform: rotate(90deg); }
.qt-section-body { padding: .5em .9em .9em; }
.qt-sub { margin: .5em 0; background: var(--sidebar-bg); border: 1px solid var(--border); border-left: 3px solid var(--accent); border-radius: 5px; }
.qt-sub > summary { list-style: none; padding: .5em .8em; cursor: pointer; font-weight: 600; }
.qt-sub > summary::-webkit-details-marker { display: none; }
.qt-sub > summary::after { content: "▶"; color: var(--text-soft); font-size: .72em; margin-left: auto; float: right; transition: transform .15s; }
.qt-sub[open] > summary::after { transform: rotate(90deg); }
.qt-sub-body { padding: .3em .9em .8em; }

.qt-wrapper-body h2, .qt-wrapper-body h3 { display: none; }
.qt-wrapper-body blockquote { border-left: 3px solid var(--accent); background: var(--bg-soft); padding: .5em 1em; margin: .8em 0; color: var(--text-soft); font-size: .92em; }
.qt-wrapper-body table { border-collapse: collapse; margin: .8em 0; font-size: .9em; }
.qt-wrapper-body th, .qt-wrapper-body td { padding: .35em .7em; border: 1px solid var(--border); text-align: left; }
.qt-wrapper-body th { background: var(--bg-soft); }
.qt-wrapper-body ol, .qt-wrapper-body ul { margin: .4em 0 .4em 1.6em; }
.qt-wrapper-body li { margin: .25em 0; }

.wikilink { color: var(--accent); background: rgba(43,108,176,.08); padding: .05em .3em; border-radius: 3px; font-weight: 500; }
.wikilink:hover { background: rgba(43,108,176,.18); text-decoration: none; }
.wikilink.missing { color: var(--text-soft); background: rgba(154,163,178,.12); cursor: help; }
code { background: var(--code-bg); color: var(--code-fg); padding: .08em .4em; border-radius: 3px; font-size: .88em; }
pre { background: var(--code-bg); color: var(--code-fg); padding: .7em 1em; overflow-x: auto; border-radius: 6px; }
pre code { background: none; padding: 0; }

.footer { border-top: 1px solid var(--border); padding: 1.5em 2.4em; color: var(--text-soft); font-size: .85em; text-align: center; }

.hidden { display: none !important; }

@media (max-width: 900px) {
  .layout { grid-template-columns: 1fr; }
  .sidebar { position: relative; max-height: none; border-right: none; border-bottom: 1px solid var(--border); }
  .topnav { display: none; }
  .content { padding: 1em 1em; }
}
"""

JS = """
// Auto-open concept card and scroll to it when navigated to
function openConcept(slug) {
  var el = document.getElementById('concept-' + slug);
  if (el) {
    el.open = true;
    // Open ancestor sections too
    var parent = el.parentElement;
    while (parent) {
      if (parent.tagName === 'DETAILS') parent.open = true;
      parent = parent.parentElement;
    }
    setTimeout(function() { el.scrollIntoView({ behavior: 'smooth', block: 'start' }); }, 60);
  }
}
function openAnchor(id) {
  var el = document.getElementById(id);
  if (el) {
    var node = el;
    while (node) {
      if (node.tagName === 'DETAILS') node.open = true;
      node = node.parentElement;
    }
    setTimeout(function() { el.scrollIntoView({ behavior: 'smooth', block: 'start' }); }, 60);
  }
}

document.addEventListener('DOMContentLoaded', function() {
  // Initial hash open
  if (window.location.hash) {
    var id = window.location.hash.substring(1);
    if (id.startsWith('concept-')) openConcept(id.substring('concept-'.length));
    else openAnchor(id);
  }
  // Sidebar links: scroll + auto-open target
  document.querySelectorAll('.side-link').forEach(function(a) {
    a.addEventListener('click', function(e) {
      var anchor = a.getAttribute('data-anchor');
      if (anchor) {
        if (anchor.startsWith('concept-')) openConcept(anchor.substring('concept-'.length));
        else openAnchor(anchor);
      }
    });
  });
  // Top nav links: scroll smoothly
  document.querySelectorAll('.topnav a').forEach(function(a) {
    a.addEventListener('click', function(e) {
      var href = a.getAttribute('href');
      if (href && href.startsWith('#')) {
        e.preventDefault();
        openAnchor(href.substring(1));
      }
    });
  });
  // Wiki links inside QT content: auto-open concept on click (also handled inline)
  document.querySelectorAll('a.wikilink[href^="#concept-"]').forEach(function(a) {
    a.addEventListener('click', function(e) {
      var href = a.getAttribute('href');
      if (href) {
        var slug = href.substring('#concept-'.length);
        openConcept(slug);
      }
    });
  });

  // Search
  var s = document.getElementById('search');
  if (s) {
    s.addEventListener('input', function() {
      var q = s.value.toLowerCase().trim();
      // Sidebar concept links
      document.querySelectorAll('.side-list .side-link').forEach(function(a) {
        var n = (a.getAttribute('data-name') || a.textContent).toLowerCase();
        var li = a.parentElement;
        if (q === '' || n.indexOf(q) >= 0) li.classList.remove('hidden');
        else li.classList.add('hidden');
      });
      // Concept cards
      document.querySelectorAll('.concept-card').forEach(function(card) {
        var name = (card.querySelector('.concept-name')||{}).textContent || '';
        var bodyTxt = (card.querySelector('.concept-body')||{}).textContent || '';
        var hay = (name + ' ' + bodyTxt).toLowerCase();
        if (q === '' || hay.indexOf(q) >= 0) card.classList.remove('hidden');
        else card.classList.add('hidden');
      });
    });
  }

  // Open the topic section in the sidebar matching the URL hash on load
  if (window.location.hash) {
    var hash = window.location.hash;
    var m = hash.match(/^#concept-(.+)$/);
    if (m) {
      var card = document.getElementById('concept-' + m[1]);
      if (card) {
        var topic = card.getAttribute('data-topic');
        var side = document.querySelector('.side-topic[data-topic-id="' + topic + '"]');
        if (side) side.open = true;
      }
    }
  }
});
"""

README = """# Core Micro Study Guide

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
"""


def write_assets():
    os.makedirs(os.path.join(OUT, 'assets'), exist_ok=True)
    with open(os.path.join(OUT, 'assets', 'style.css'), 'w', encoding='utf-8') as f:
        f.write(CSS)
    with open(os.path.join(OUT, 'assets', 'app.js'), 'w', encoding='utf-8') as f:
        f.write(JS)
    with open(os.path.join(OUT, 'README.md'), 'w', encoding='utf-8') as f:
        f.write(README)


def main():
    os.makedirs(OUT, exist_ok=True)
    # Best-effort cleanup of old multi-page artefacts
    for sub in ('topics', 'concepts', 'question-types'):
        d = os.path.join(OUT, sub)
        if os.path.isdir(d):
            try:
                import shutil
                shutil.rmtree(d)
            except Exception as e:
                print(f"Note: could not remove {sub}/ (continuing): {e}")
    write_assets()
    build_index()
    print('Built single-page site at:', OUT)


if __name__ == '__main__':
    main()
