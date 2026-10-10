# Om Kathalkar — personal academic website

A fast, dependency-free static site: dark theme, electric-blue accent, typewriter type
(Courier Prime + JetBrains Mono). Four pages, no build step needed to publish.

## What's inside

```
index.html            Home — hero, KV-cache demo, about, research, top-3 lists, contact
publications.html     All 7 papers + 3 patents, grouped by year, filter: All / Papers / Patents
featured.html         9 photo cards (filter: Awards / Talks / Milestones) + 6 press links
news.html             All 12 updates by year, filter: Papers / Career / Milestones
assets/
  css/style.css       All styling. Colours and fonts are variables at the top (:root)
  js/main.js          Latest strip, KV demo slider, filters, copy-email button (~90 lines)
  img/                Portrait, publication figures, featured photos (web-sized JPEGs)
  docs/               Om_Kathalkar_CV.pdf
tools/
  content.json        ALL text and lists (news, papers, featured, research, contact…)
  build.py            Regenerates the four .html pages from content.json
```

## Publish on GitHub Pages (replaces the current al-folio site)

1. Back up the current site: on GitHub, create a branch from `main` (e.g. `al-folio-backup`).
2. In your `omkathalkar.github.io` repo on `main`, delete the old Jekyll files
   (or start from an empty repo) and copy **everything in this folder** to the repo root.
3. Add an empty file named `.nojekyll` at the repo root (tells GitHub not to run Jekyll).
4. Commit and push. Settings → Pages → Source: *Deploy from a branch*, `main`, `/ (root)`.
5. Wait about a minute, then open https://omkathalkar.github.io

Preview locally first:

```bash
cd this-folder
python3 -m http.server 8000      # then open http://localhost:8000
```

## Updating content

Everything you'll change regularly lives in `tools/content.json`:

- **Add a news item:** add an object at the *top* of `"news"`
  (`{"y": "2026", "m": "Dec", "type": "Paper", "text": "…"}`; type is Paper, Career or Milestone).
  The newest 6 also feed the blue "Latest" strip; the newest 3 show on the home page.
- **Add a paper/patent:** add to `"publications"` (newest first). `"kind"` is `paper` or `patent`.
  Put a figure in `assets/img/publications/` and set `"img"`; leave it out for no thumbnail.
- **Add a featured photo:** put a JPEG (~1400px wide) in `assets/img/featured/` and add to `"featured"`
  (`"kind"`: Award, Talk or Milestone).
- **Change the CV:** replace `assets/docs/Om_Kathalkar_CV.pdf`.

Then rebuild the pages (Python 3, standard library only):

```bash
python3 tools/build.py
```

You can also edit the `.html` files directly — just note that `build.py` overwrites them.

## Re-theming

Open `assets/css/style.css` and edit the variables in `:root`:

- `--accent` / `--button` — the blue (e.g. `#2fbf9b` for mint, `#e08a5c` for orange)
- `--bg`, `--surface`, `--line` — background tones
- `--font` — main typeface (swap the Google Fonts link in `build.py` if you change it)

## Notes

- Analytics: your old site used Google Analytics `G-CYV1Y2X5MC`. To keep it, paste the
  standard gtag snippet into the `head()` function in `tools/build.py` and rebuild.
- The TRAQID project page (`/traqid/`) lived in the old repo; keep that folder when you
  replace the site so the link from the publications list keeps working.
- Accessibility: keyboard focus rings, reduced-motion support, alt text on every image,
  44px touch targets.
