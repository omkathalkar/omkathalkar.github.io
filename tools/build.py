#!/usr/bin/env python3
"""Rebuild the four HTML pages from content.json.

Usage (from the site root):   python3 tools/build.py
Edit tools/content.json (news, papers, featured items...), run this, then commit.
Only the Python standard library is needed.
"""
import json
import os
from html import escape

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
C = json.load(open(os.path.join(HERE, "content.json"), encoding="utf-8"))
S = C["site"]
e = escape

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Courier+Prime:ital,wght@0,400;0,700;1,400'
         '&family=JetBrains+Mono:wght@400;500;700&display=swap">')

NAV = [("index.html#about", "About", "home"), ("index.html#research", "Research", "home"),
       ("publications.html", "Publications", "publications"), ("featured.html", "Featured", "featured"),
       ("news.html", "News", "news"), ("index.html#contact", "Contact", "home")]


def head(title, desc):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:image" content="{S['url']}/{C['hero']['photo']}">
<meta name="theme-color" content="#0d0d0d">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='8' fill='%230d0d0d'/%3E%3Ctext x='10' y='44' font-family='monospace' font-size='34' font-weight='700' fill='%23e8e8e8'%3Eok%3C/text%3E%3Ccircle cx='52' cy='42' r='4' fill='%234f82ff'/%3E%3C/svg%3E">
{FONTS}
<link rel="stylesheet" href="assets/css/style.css">
</head>
"""


def header(active):
    links = []
    for href, label, key in NAV:
        cur = ' aria-current="page"' if key == active and key != "home" else ""
        if active != "home" and label == "About":
            href, label = "index.html", "Home"
        if active != "home" and label in ("Research", "Contact"):
            continue
        if active == "home" and href.startswith("index.html#"):
            href = href[len("index.html"):]
        links.append(f'<a class="nav-link" href="{href}"{cur}>{label}</a>')
    return f"""<header class="site-header">
  <nav class="nav wrap" aria-label="Main">
    <a class="brand" href="index.html" aria-label="{e(S['short'])} — home">
      <span class="brand-mark">ok<span>.</span></span>
      <span class="brand-sub">Athens · 37.98° N</span>
    </a>
    <div class="nav-links">
      {chr(10).join('      ' + l for l in links).strip()}
      <a class="btn btn-primary" href="{S['cv']}">CV ↓</a>
    </div>
  </nav>
</header>"""


def footer():
    return f"""<footer class="site-footer">
  <div class="wrap"><span>© 2026 {e(S['name'])}</span><span>Last updated {e(S['updated'])} · Athens</span></div>
</footer>
<script src="assets/js/main.js" defer></script>
</body>
</html>
"""


def pub_html(p):
    img = f'<img src="{p["img"]}" alt="Figure from {e(p["title"])}" loading="lazy">' if p.get("img") else ""
    links = "".join(f'<a class="btn-small chip" href="{e(h)}">{e(l)} ↗</a>' for l, h in p["links"])
    links = f'<div class="pub-links">{links}</div>' if links else ""
    return f"""<li class="pub {p['kind']}" data-kind="{p['kind']}">
  <span class="pub-year">{p['year']}</span>
  <div class="pub-body">
    <span class="pub-venue">{e(p['venue'])}</span>
    <span class="pub-title">{e(p['title'])}</span>
    <span class="pub-authors">{e(p['pre'])}<strong>{e(p['me'])}</strong>{e(p['post'])}</span>
    {links}
  </div>
  {img}
</li>"""


def card_html(f):
    return f"""<figure class="card" data-kind="{f['kind']}">
  <img src="{f['img']}" alt="{e(f['title'])}" style="object-position: {f['pos']}" loading="lazy">
  <figcaption><span class="kind">{e(f.get('label', f['kind']))}</span><span class="title">{e(f['title'])}</span><span class="sub">{e(f['sub'])}</span></figcaption>
</figure>"""


def press_html(m):
    return f"""<a class="link-row" href="{e(m['url'])}"><span><span class="t">{e(m['title'])}</span><span class="s">{e(m['source'])} · {e(m['date'])}</span></span><span class="arrow" aria-hidden="true">↗</span></a>"""


def news_html(n, with_type=False):
    t = f'<span class="news-type {n["type"]}">{n["type"]}</span>' if with_type else ""
    date = n["m"] if with_type else f'{n["m"]} {n["y"]}'
    return f'<li data-kind="{n["type"]}"><span class="news-date">{date}</span><span class="news-text">{e(n["text"])}</span>{t}</li>'


def filters(target, opts):
    btns = "".join(f'<button type="button" class="btn-small" data-filter="{k}" aria-pressed="{"true" if k == "all" else "false"}">{l} · {n}</button>' for k, l, n in opts)
    return f'<div class="filters" role="group" aria-label="Filter" data-filter-group="{target}">{btns}</div>'


def section_head(num, title, link=None):
    a = f'<a class="btn-small" href="{link[0]}">{link[1]}</a>' if link else ""
    return f'<div class="section-head"><div class="section-title"><span class="section-num">{num}</span><h2>{title}</h2></div>{a}</div>'


def year_groups(items, render, key):
    years = []
    for it in items:
        if it[key] not in years:
            years.append(it[key])
    out = []
    for y in years:
        lis = "\n".join(render(it) for it in items if it[key] == y)
        out.append(f'<section class="year-group"><h2>{y}</h2><ul>{lis}</ul></section>')
    return "\n".join(out)


# ------------------------------------------------------------------ index
def build_index():
    H, P = C["hero"], C["project"]
    latest = json.dumps([[f'{n["m"]} {n["y"]}', n["text"]] for n in C["news"][:6]], ensure_ascii=False)
    facts = "".join(
        f'<div><dt>{e(f["k"])}</dt><dd>' + (f'<a href="{e(f["href"])}">{e(f["v"])} ↗</a>' if f.get("href") else e(f["v"])) + '</dd></div>'
        for f in C["facts"])
    toks = "".join(f'<span class="tok{" sink" if i == 0 else ""}" data-score="{s}">{e(w)}</span>' for i, (w, s) in enumerate(C["kv_tokens"]))
    rows = "".join(f'<tr><th scope="row">{e(k)}</th><td>{e(v)}</td></tr>' for k, v in C["about"]["rows"])
    bio = "".join(f"<p>{p}</p>" for p in C["about"]["bio"])
    chall = "".join(f'<li><b>{i + 1}</b><span>{e(c)}</span></li>' for i, c in enumerate(P["challenges"]))
    research = []
    for i, r in enumerate(C["research"]):
        kw = "".join(f"<li>{e(k)}</li>" for k in r["kw"])
        kw = f"<ul>{kw}</ul>" if kw else ""
        research.append(f"""<details{' open' if i == 0 else ''}>
  <summary><span class="r-num">0{i + 1}</span><span class="r-head"><span class="r-tag">{e(r['tag'])}</span><span class="r-title">{e(r['title'])}</span></span><span class="r-when">{e(r['when'])}</span><span class="r-icon" aria-hidden="true">+</span></summary>
  <div class="r-body"><p>{e(r['desc'])}</p>{kw}</div>
</details>""")
    path = "".join(f'<li><span class="when">{e(p["when"])}</span><span class="role">{e(p["role"])}</span><span class="org">{e(p["org"])}</span><span class="note">{e(p["note"])}</span></li>' for p in C["path"][:3])
    pubs = "\n".join(pub_html(p) for p in C["publications"][:3])
    feats = "\n".join(card_html(f) for f in C["featured"][:3])
    press = "\n".join(press_html(m) for m in C["press"][:3])
    news = "\n".join(news_html(n) for n in C["news"][:3])
    teach = "".join(f"<li><b>{e(r)}</b><span>{e(w)}</span></li>" for r, w in C["teaching"])
    K = C["contact"]
    links = "".join(f'<a class="link-row" href="{e(h)}"><span><span class="t">{e(l)}</span><span class="s">{e(s)}</span></span><span class="arrow" aria-hidden="true">↗</span></a>' for l, s, h in K["links"])
    bars = "".join(f'<span style="flex:{f};background:{c}"></span>' for f, c in [(3, "var(--accent)"), (1, "var(--accent-2)"), (2, "var(--line)"), (1, "var(--accent)"), (4, "var(--line)"), (1, "var(--accent-2)")])

    html = head(f"{S['short']} — Doctoral Researcher, NTUA", S["description"]) + f"""<body>
{header('home')}

<div class="latest" aria-label="Latest news" data-latest='{e(latest)}'>
  <div class="latest-row wrap">
    <span class="latest-tag">Latest</span>
    <span class="latest-date"></span>
    <span class="latest-text" aria-live="polite"></span>
    <div class="latest-ctrl"><button type="button" data-prev aria-label="Previous update">‹</button><span class="latest-pos"></span><button type="button" data-next aria-label="Next update">›</button></div>
  </div>
  <div class="latest-bar"></div>
</div>

<main>
<section id="home" class="hero wrap">
  <div class="hero-text">
    <p class="hero-kicker">{e(H['kicker'])}</p>
    <h1>Om<br>Kathalkar</h1>
    <div class="hero-bars" aria-hidden="true">{bars}</div>
    <p class="hero-lead">{e(H['lead_before'])}<em>{e(H['lead_em'])}</em>{e(H['lead_after'])}</p>
    <div class="hero-actions">
      <a class="btn btn-primary" href="#research">View research →</a>
      <a class="btn btn-ghost" href="#kv">Try the KV-cache demo</a>
    </div>
  </div>
  <figure class="hero-photo">
    <img src="{H['photo']}" alt="{e(H['photo_alt'])}" width="753" height="1003">
    <figcaption>{e(H['caption'])}</figcaption>
  </figure>
</section>

<div class="wrap"><dl class="facts" aria-label="At a glance">{facts}</dl></div>

<section id="kv" class="kv" aria-labelledby="kv-h" data-kv>
  <div class="kv-inner wrap">
    <div class="kv-copy">
      <span class="label" style="color:var(--accent-2)">My research in 20 seconds</span>
      <h2 id="kv-h">What is KV-cache compression?</h2>
      <p>While an LLM reads, it stores a key and a value for every token. On long prompts and long reasoning chains that cache fills GPU memory. Eviction keeps the tokens that matter and drops the rest. Drag the budget to see it.</p>
      <label for="kv-budget"><span>Cache budget</span><span data-budget>35%</span></label>
      <input id="kv-budget" type="range" min="10" max="100" step="5" value="35">
      <div class="kv-meter">
        <div class="kv-meter-row"><span>Tokens kept</span><strong data-kept></strong></div>
        <div class="kv-track"><div class="kv-fill"></div></div>
      </div>
      <p class="kv-note">Illustration only — importance scores are hand-set for this demo. The first token is always kept: models lean on it as an attention sink.</p>
    </div>
    <div class="kv-tokens" aria-label="Tokens in the cache">{toks}</div>
  </div>
</section>

<section id="about" class="section wrap" style="padding-top:96px">
  {section_head('01', 'About')}
  <div class="about-grid">
    <div>
      <p class="about-intro">{C['about']['intro']}</p>
      <table class="about-table"><tbody>{rows}</tbody></table>
    </div>
    <div class="about-bio">{bio}</div>
  </div>
</section>

<section id="research" class="section wrap">
  {section_head('02', 'Research')}
  <article class="project" aria-labelledby="fi-h">
    <div class="project-main">
      <span class="label">Current project</span><span class="dot"></span>
      <h3 id="fi-h">{e(P['name'])}</h3>
      <p class="project-sub">{e(P['full'])}</p>
      {''.join(f'<p>{e(p)}</p>' for p in P['paras'])}
    </div>
    <div class="project-side">
      <p class="label" style="color:var(--muted);margin-bottom:14px">Challenges it tackles</p>
      <ol>{chall}</ol>
    </div>
  </article>
  <div class="research-list">
{chr(10).join(research)}
  </div>
</section>

<section id="experience" class="section wrap">
  {section_head('03', 'Path', (S['cv'], 'Full CV ↗'))}
  <ol class="path">{path}</ol>
</section>

<section id="publications" class="section wrap">
  {section_head('04', 'Publications', ('publications.html', f"All {len(C['publications'])} publications &amp; patents →"))}
  <ul class="pub-list">
{pubs}
  </ul>
</section>

<section id="featured" class="section wrap">
  {section_head('05', 'Featured', ('featured.html', 'All awards, talks &amp; media →'))}
  <div class="cards">
{feats}
  </div>
  <h3 class="label media-h" style="color:var(--muted)">In the media</h3>
  <div class="press">
{press}
  </div>
</section>

<section id="news" class="section wrap">
  <div class="news-wrap">
    <div class="news-col">
      {section_head('06', 'News', ('news.html', 'All news →'))}
      <ul class="news-list">
{news}
      </ul>
    </div>
    <aside class="teaching" id="teaching">
      <span class="label">Teaching &amp; mentoring</span>
      <ul>{teach}</ul>
    </aside>
  </div>
</section>

<section id="contact" class="section wrap" style="padding-bottom:96px">
  {section_head('07', 'Contact')}
  <div class="contact-grid">
    <div>
      <p class="contact-lead">The best way to reach me is email. Happy to talk research, collaborations, or a good idea.</p>
      <div class="contact-actions">
        <a class="btn btn-primary" href="mailto:{K['email']}">{K['email']}</a>
        <button type="button" class="btn btn-ghost" data-copy="{K['email']}">Copy address</button>
      </div>
      <p class="muted" style="margin-top:18px">Personal: <a href="mailto:{K['personal']}">{K['personal']}</a></p>
      <address>{'<br>'.join(e(a) for a in K['address'])}</address>
    </div>
    <div class="contact-links">{links}</div>
  </div>
</section>
</main>
""" + footer()
    return html


def subpage(active, title, kicker, h1, sub, filt, body):
    return head(f"{title} — {S['short']}", f"{title} — {S['description']}") + f"""<body class="subpage">
{header(active)}
<main class="wrap">
  <a class="btn-small" href="index.html">← Back to home</a>
  <div class="page-head">
    <div><span class="label">{kicker}</span><h1>{h1}</h1><p>{sub}</p></div>
    {filt}
  </div>
  {body}
</main>
""" + footer()


def build_publications():
    P = C["publications"]
    np_, nt = sum(p["kind"] == "paper" for p in P), sum(p["kind"] == "patent" for p in P)
    body = f'<div id="pub-scope">{year_groups(P, pub_html, "year")}</div>'
    return subpage("publications", "Publications & patents", "Research output", "Publications &amp; patents",
                   f"{np_} peer-reviewed papers · {nt} patents · since 2022",
                   filters("#pub-scope", [("all", "All", len(P)), ("paper", "Papers", np_), ("patent", "Patents", nt)]), body)


def build_featured():
    F = C["featured"]
    cnt = lambda k: sum(f["kind"] == k for f in F)
    body = f"""<div class="cards" id="feat-scope">
{chr(10).join(card_html(f) for f in F)}
</div>
<section aria-labelledby="media-h" style="margin-top:80px">
  <div class="section-title" style="margin-bottom:20px"><h2 id="media-h">In the media</h2><span class="muted" style="font-family:var(--mono);font-size:13px">{len(C['press'])} stories</span></div>
  <div class="press">{''.join(press_html(m) for m in C['press'])}</div>
</section>"""
    return subpage("featured", "Featured", "Gallery &amp; press", "Featured",
                   "Awards, talks and milestones — and where the work has been covered.",
                   filters("#feat-scope", [("all", "All", len(F)), ("Award", "Awards", cnt("Award")), ("Talk", "Talks", cnt("Talk")), ("Milestone", "Milestones", cnt("Milestone"))]), body)


def build_news():
    N = C["news"]
    cnt = lambda k: sum(n["type"] == k for n in N)
    body = f'<div id="news-scope">{year_groups(N, lambda n: news_html(n, True), "y")}</div>'
    return subpage("news", "News", "Updates", "News", "Papers, milestones and moves — newest first.",
                   filters("#news-scope", [("all", "All", len(N)), ("Paper", "Papers", cnt("Paper")), ("Career", "Career", cnt("Career")), ("Milestone", "Milestones", cnt("Milestone"))]), body)


if __name__ == "__main__":
    pages = {"index.html": build_index(), "publications.html": build_publications(),
             "featured.html": build_featured(), "news.html": build_news()}
    for name, html in pages.items():
        with open(os.path.join(ROOT, name), "w", encoding="utf-8") as fh:
            fh.write(html)
        print("wrote", name)
