# FIBA 3x3 World Tour 2026 — prototype

Two pages, built to show one thing: **the Nations League design system carries
straight over to a family site, and only four things change.**

This folder is standalone. It is not linked into `fiba-nl-prototype` and shares
no page with it, so it can go up at its own URL.

## Preview

    ./preview.command

or `python3 -m http.server 8080`, then <http://localhost:8080/index.html>.

| File | What it is |
|---|---|
| `index.html` | World Tour home |
| `team.html`  | Ub (SRB) — reachable by clicking **Ub** in Live now or in the World ranking |

## The system, not a copy of it

`assets/tokens.css`, `base.css`, `elements.css`, `modules.css`, `motion.css`,
`interactions.css` and `behaviour.css` are the Nations League build's own files,
byte for byte. Every component on these pages is called by its system name, so
the two sites can be put side by side and read as one system:

| On the page | Component |
|---|---|
| top strip, nav, footer | F-02 GlobalHeader · F-03 CompetitionNav · F-06 SiteFooter |
| the season strip under the nav | **S-14 StopBar** (new) |
| countdown to the next stop | S-13 Countdown, variant = compact |
| section titles | el-01 SectionHeader — *no rule under it; the system never had one* |
| Latest news | C-02 NewsRail + el-14 Chip |
| Overview | S-09 Overview |
| Live now | S-01 LiveAccordion on el-07 AccordionShell + el-05 StatusBadge |
| World ranking, Season journey | R-02 StandingsTable = el-08 TableHeaderRow + el-04 TeamRow + el-13 FederationTag |
| Find a team / a player | E-01 TeamFinder + el-11 SearchInput + el-14 Chip |
| Individual world ranking, Roster | E-10 RosterGrid + E-08 PlayerCard |
| Advertising | el-29 AdSpace |
| Road to the Final | **el-31 MeterBar** (new) |
| Top moment | **el-32 VideoThumb** (new) |
| Photos | C-03 PhotoGallery + el-22 CarouselIndicator |
| team page header | E-04 TeamHeader + el-23 Breadcrumb |
| buttons and links everywhere | ctl-01 Button · ctl-02 Link |

`<body class="live">` is the system's own gate: it switches on every hover,
focus and pressed state the system documents. The corner cut, the elevation on
a card, the accordion's open, the bouncing live dot and the section reveal are
all the system's — nothing here reimplements them.

### Three components this build added to the system

They did not exist, so they were written in the system's idiom and merged back
into it: `assets/ds-additions.css` is also in the Nations League build, linked
from `system/index.html`, documented at `system/pages/additions.html`, and
listed in the design system's own menu under **Additions · World Tour**.

- **S-14 StopBar** — the season as a submenu: past dim, tonight white with the
  dot, still-to-come legible. No dates; S-07 is the calendar.
- **el-31 MeterBar** — one value against a track, stackable so rows compare.
- **el-32 VideoThumb** — a video poster that links out. The system has no
  player on purpose; ctl-07 WatchLive sends people to YouTube.

## The four branding slots

Everything World Tour lives in `assets/wt.css`. Swapping these four is what
would turn this into the Women's Series:

1. **the home hero** — `wt-bg.png`, `wt-el-left.svg`, `wt-el-right.svg`, `wt-lockup.svg`
2. **the sub-page headline and its 4px bar** — `wt-bar.svg`
3. **the player-card key visual** — `wt-el-card.svg`
4. **the accent** — World Tour Red

**Where the accent may not go.** Red is a surface and a graphic, never a
control. It does not touch ctl-01 Button, ctl-02 Link, any focus ring or any
nav state — those stay black and white on every family site, which is what
makes the system recognisable. Its only structural job is `--status-live`,
which is already the system's own red.

### The hero mask

The season photograph is supplied at twice the band height on purpose. It is
centred in a 192px band with 96px of slack above and below, the band clips it,
and the parallax is clamped to exactly that slack — so the plate covers the
band edge to edge at every scroll position and the red ground behind it is
never uncovered.

## Where the content comes from

Every figure, headline, photograph, name and video was read off a live source
on 3 September 2026 — nothing is placeholder copy:

- news, tour standings, the Zadar field, Ub's season — `worldtour.fiba3x3.com/2026`
- individual world ranking (men) — `fiba3x3.com/en/rankings/individual.html`
- player portraits — `assets.fiba3x3.com`
- the six Shorts — `youtube.com/@FIBA3x3/shorts`, all men's World Tour

Photographs, portraits and Shorts posters load from FIBA's own CDNs, so the
pages need a connection to show them. Everything else — fonts included — is in
this folder.

## Rebuilding

    python3 build/build.py 20

`build/data.py` holds the content, `build/build.py` the markup. The argument is
how many rows the World ranking shows; 20 is the number that makes the right
column finish level with Overview + Live now on the left.


## Publishing it, and keeping it out of Google

GitHub Pages serves this folder as-is — it is already a static site with no
build step. `.nojekyll` is here so Pages publishes every file untouched.

Run these in Terminal, from this folder:

    cd ~/Documents/FIBA-2026/fiba-wt-prototype
    git init -b main
    git add -A
    git commit -m "FIBA 3x3 World Tour 2026 prototype"
    git remote add origin git@github.com:<you>/<repo>.git
    git push -u origin main

Then in the repository: **Settings → Pages → Source: Deploy from a branch →
`main` / `/ (root)`**. The site appears at
`https://<you>.github.io/<repo>/` a minute or so later.

### Staying out of search results

Both pages carry:

    <meta name="robots" content="noindex, nofollow, noarchive, nosnippet, noimageindex, notranslate">

That tag is the part that works, and `robots.txt` here deliberately **allows**
crawling so that it can. This is the one counter-intuitive bit: a
`Disallow: /` in robots.txt stops a crawler fetching the page, so it never
reads the `noindex` — and if anyone links to the URL, Google can still list it
as a bare result with no title. Allowing the fetch and serving `noindex` is
what actually keeps it out. Do not add a `Disallow` unless you also remove the
meta tags.

GitHub Pages gives no control over response headers, so `X-Robots-Tag` is not
available; the meta tag is the whole lever there.

### What this does and does not give you

`noindex` keeps the site out of search results. It does **not** make it
private: a GitHub Pages site is public to anyone who has the URL, whether the
repository is public or private. For a client pitch that is usually fine —
an unguessable repository name plus `noindex` means only the people you send
the link to will ever see it.

If the URL itself has to be protected, GitHub Pages is the wrong host. The two
straightforward alternatives:

- **Cloudflare Pages + Cloudflare Access** — free tier, sign-in by email
  allow-list, drag-and-drop or Git deploy.
- **Netlify** — password protection on a site is a paid feature, but the
  deploy is the same drag-and-drop.

A note either way: the photographs, portraits and Shorts posters load from
FIBA's own CDNs. They will keep working on a public URL, but they are hotlinks
— if a client is going to keep this online for any length of time, copy those
files into `assets/` first.
