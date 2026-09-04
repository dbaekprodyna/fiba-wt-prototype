# -*- coding: utf-8 -*-
"""FIBA 3x3 World Tour 2026 — page builder.

Every element and module below is the Nations League design system's,
called by its own class names, so a client can put the two sites side
by side and see the same components underneath. The only World Tour
specific classes are the four branding slots, all prefixed hwt- / wt-.
"""
import io, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data import *

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---- Material Symbols paths, the set the design system uses --------
def sv(path, size=18, box='0 -960 960 960'):
    return ('<svg fill="currentColor" height="%d" width="%d" viewBox="%s" '
            'xmlns="http://www.w3.org/2000/svg"><path d="%s"></path></svg>'
            % (size, size, box, path))

P_ARROW  = "M686-450H160v-60h526L438-758l42-42 320 320-320 320-42-42 248-248Z"
P_DOWN   = "M480-344 240-584l43-43 197 197 197-197 43 43-240 240Z"
P_RIGHT  = "M530-481 332-679l43-43 241 241-241 241-43-43 198-198Z"
P_LEFT   = "M622-241 381-482l241-241 43 43-198 198 198 198-43 43Z"
P_SEARCH = ("M796-121 533-384q-30 26-70 40.5T378-329q-108 0-183-75t-75-181q0-106 75-181t182-75q106 0 180.5 "
            "75T632-585q0 43-14 83t-42 75l264 262-44 44ZM377-389q81 0 138-57.5T572-585q0-81-57-138.5T377-781q-82 "
            "0-139.5 57.5T180-585q0 81 57.5 138.5T377-389Z")
P_PLAY   = "M320-200v-560l440 280-440 280Z"
P_APPS   = ("M240-160q-33 0-56.5-23.5T160-240q0-33 23.5-56.5T240-320q33 0 56.5 23.5T320-240q0 33-23.5 "
            "56.5T240-160Zm240 0q-33 0-56.5-23.5T400-240q0-33 23.5-56.5T480-320q33 0 56.5 23.5T560-240q0 "
            "33-23.5 56.5T480-160Zm240 0q-33 0-56.5-23.5T640-240q0-33 23.5-56.5T720-320q33 0 56.5 23.5T800-240q0 "
            "33-23.5 56.5T720-160ZM240-400q-33 0-56.5-23.5T160-480q0-33 23.5-56.5T240-560q33 0 56.5 23.5T320-480q0 "
            "33-23.5 56.5T240-400Zm240 0q-33 0-56.5-23.5T400-480q0-33 23.5-56.5T480-560q33 0 56.5 23.5T560-480q0 "
            "33-23.5 56.5T480-400Zm240 0q-33 0-56.5-23.5T640-480q0-33 23.5-56.5T720-560q33 0 56.5 23.5T800-480q0 "
            "33-23.5 56.5T720-400ZM240-640q-33 0-56.5-23.5T160-720q0-33 23.5-56.5T240-800q33 0 56.5 23.5T320-720q0 "
            "33-23.5 56.5T240-640Zm240 0q-33 0-56.5-23.5T400-720q0-33 23.5-56.5T480-800q33 0 56.5 23.5T560-720q0 "
            "33-23.5 56.5T480-640Zm240 0q-33 0-56.5-23.5T640-720q0-33 23.5-56.5T720-800q33 0 56.5 23.5T800-720q0 "
            "33-23.5 56.5T720-640Z")
P_CAM    = ("M480-260q75 0 127.5-52.5T660-440q0-75-52.5-127.5T480-620q-75 0-127.5 52.5T300-440q0 75 52.5 "
            "127.5T480-260Zm0-60q-50 0-85-35t-35-85q0-50 35-85t85-35q50 0 85 35t35 85q0 50-35 85t-85 "
            "35ZM140-120q-24 0-42-18t-18-42v-520q0-24 18-42t42-18h141l74-80h250l74 80h141q24 0 42 18t18 "
            "42v520q0 24-18 42t-42 18H140Z")

RIO_SRC = "https://res.cloudinary.com/ddsbdyeyj/image/upload/ar_16:9,c_lfill,g_auto/w_900,c_lfill/q_auto/v1775569288/xehdyqi9rgq05komndpp"

NAV = ["Home", "Teams", "Standings", "Stats", "News", "Photos", "Videos", "Calendar", "More"]

# ================================================================ head
def head(title):
    return """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<!-- Kept out of search results. This tag is the part that actually
     works: robots.txt deliberately does NOT block crawling, because a
     blocked crawler never reads this line and the bare URL can still
     be listed. See robots.txt. -->
<meta name="robots" content="noindex, nofollow, noarchive, nosnippet, noimageindex, notranslate">
<meta name="googlebot" content="noindex, nofollow, noimageindex">
<title>%s</title>

<!-- The Nations League design system, byte for byte -->
<link rel="stylesheet" href="assets/fonts.css">
<link rel="stylesheet" href="assets/tokens.css">
<link rel="stylesheet" href="assets/base.css">
<link rel="stylesheet" href="assets/elements.css">
<link rel="stylesheet" href="assets/modules.css">
<link rel="stylesheet" href="assets/motion.css">
<link rel="stylesheet" href="assets/interactions.css">
<link rel="stylesheet" href="assets/behaviour.css">
<link rel="stylesheet" href="assets/s13.css">
<!-- three components this build added to the system -->
<link rel="stylesheet" href="assets/ds-additions.css">
<!-- and the World Tour brand layer: four slots, nothing else -->
<link rel="stylesheet" href="assets/wt.css">
</head>
<!-- class="live" is the design system's own gate: it switches on
     every hover, focus and pressed state documented in the system. -->
<body class="live wt-brand">
""" % title

TAIL = """<script defer src="assets/wt.js"></script>
</body>
</html>"""

# ================================================================ chrome
def flag(ioc, ring=True):
    return ('<div class="flag%s"><img src="assets/flags/%s.svg" alt=""></div>'
            % (' flag-ring' if ring else '', ioc))

def ftag(team, ioc, size='s'):
    return ('<div class="el-13-FederationTag--%s ftag ftag-%s cut cut-s ftag-plain ftag-teamfirst">'
            '%s<div class="ftag-txt"><span class="ftag-name">%s</span>'
            '<span class="ftag-code">%s</span></div></div>'
            % (size + '-code-name', size, flag(ioc), team, ioc))

def lnk(label, href="#", cls=""):
    return ('<a class="nav-a" href="%s"><div class="ctl-02-Link--default lnk %s">'
            '<span class="lbl">%s</span>%s</div></a>' % (href, cls, label, sv(P_ARROW)))

def btn(label, href="#", kind="primary"):
    if kind == "primary":
        return ('<a class="nav-a" href="%s"><div class="ctl-01-Button--primary-default btn cut cut-m btn-primary">'
                '<span class="lbl">%s</span>%s</div></a>' % (href, label, sv(P_ARROW)))
    return ('<a class="nav-a" href="%s"><div class="ctl-01-Button--outline-default btn cut cut-m btn-outline cut-out">'
            '<div class="cutfill"></div><span class="lbl">%s</span>%s</div></a>' % (href, label, sv(P_ARROW)))

def chip_plain(label, size="xs"):
    return ('<div class="el-14-Chip--%s-default chip chip-%s cut cut-s cut-out">'
            '<div class="cutfill"></div><span class="lbl">%s</span></div>' % (size, size, label))

def chip(label, href="#", size="m"):
    return ('<a class="nav-a" href="%s"><div class="el-14-Chip--%s-default chip chip-%s cut cut-s cut-out">'
            '<div class="cutfill"></div><span class="lbl">%s</span></div></a>' % (href, size, size, label))

def badge_live(label="Live"):
    return ('<div class="el-05-StatusBadge--live badge badge-live cut cut-s">'
            '<span class="badge-dot"></span><span class="lbl">%s</span></div>' % label)

def sec_head(title, right=""):
    r = right or ''
    return ('<div class="el-01-SectionHeader--default el01-wrap"><div class="el01">'
            '<div class="el01-left"><h2 class="t-h2">%s</h2></div>%s</div></div>' % (title, r))

def chrome(active):
    items = []
    for n in NAV:
        cls = "f03-i f03-on" if n == active else "f03-i"
        href = "index.html" if n == "Home" else ("team.html" if n == "Teams" else "#")
        items.append('<a class="nav-a" href="%s"><div class="%s">%s</div></a>' % (href, cls, n))
    stops = []
    for name, slug, st in STOPS:
        cls = {"past": "s14-i s14-done", "live": "s14-i s14-on", "next": "s14-i"}[st]
        dot = '<span class="s14-dot" aria-label="live"></span>' if st == "live" else ''
        stops.append('<a class="nav-a" href="#"><div class="%s" tabindex="0">%s%s</div></a>' % (cls, name, dot))
    return """<header class="wt-bleed">
  <!-- F-02 GlobalHeader -->
  <div class="F-02-GlobalHeader--default f02">
    <a class="nav-a" href="https://www.fiba.basketball"><span class="f02-corp">fiba.basketball</span></a>
    <div class="f02-fam">
      <a class="nav-a" href="#"><span class="f02-famlink">Nations League</span></a>
      <a class="nav-a" href="#"><span class="f02-famlink">Women's Series</span></a>
      <a class="nav-a" href="#"><span class="f02-famlink">Challengers</span></a>
      <a class="nav-a" href="#"><span class="f02-famlink">Play 3x3</span></a>
    </div>
  </div>
  <!-- F-03 CompetitionNav — the selected item's bar is white, as it is
       on every family site; the brand colour never enters a nav state -->
  <div class="F-03-CompetitionNav--default f03">
    <a class="nav-a" href="index.html"><div class="f03-mark"><div class="brandlogo"><img src="assets/img/logo-3x3.svg" alt="FIBA 3x3" width="71" height="30"></div></div></a>
    <a class="nav-a" href="index.html"><div class="f03-word"><div class="brandlogo"><img src="assets/img/wt-logo.svg" alt="World Tour" width="90" height="18"></div></div></a>
    <div class="f03-nav"><div class="f03-list">%s
      <a class="nav-a" href="#"><div class="f03-search">%s</div></a>
    </div></div>
    <div class="f03-season"><span class="f03-caret">%s</span><span class="f03-year">2026</span></div>
  </div>
  <!-- S-14 StopBar — added to the design system by this build -->
  <div class="S-14-StopBar--default s14">
    <button class="s14-nav" data-dir="prev" aria-label="Earlier stops">%s</button>
    <div class="s14-scroll">%s</div>
    <button class="s14-nav" data-dir="next" aria-label="Later stops">%s</button>
    <a class="nav-a" href="#"><div class="s14-all" tabindex="0">%s All 36 stops</div></a>
  </div>
</header>""" % ("".join(items), sv(P_SEARCH, 20), sv(P_DOWN, 20),
                sv(P_LEFT, 16), "".join(stops), sv(P_RIGHT, 16), sv(P_APPS, 14))

# ================================================================ hero
def hero():
    """Branding slot 1. The Nations League .hnl band, World Tour artwork."""
    return """<section class="hwt wt-bleed" aria-label="FIBA 3x3 World Tour 2026">
  <img class="hwt-bg" src="assets/img/wt-bg.png" alt="" width="3456" height="768">
  <img class="hwt-kv hwt-kv-l" src="assets/img/wt-el-left.svg" alt="" width="352" height="192">
  <img class="hwt-kv hwt-kv-r" src="assets/img/wt-el-right.svg" alt="" width="338" height="192">
  <div class="hwt-in">
    <h1 class="hwt-lock">
      <img class="hwt-logo" src="assets/img/wt-lockup.svg" alt="FIBA 3x3 World Tour" width="385" height="52">
      <span class="hwt-s">15th season &middot; 14 Masters &middot; one Final</span>
    </h1>
  </div>
</section>"""

# ================================================================ S-13
def countdown():
    """S-13 Countdown, variant = compact. data-until is a real instant,
       so wt.js runs the figures rather than printing a picture of them."""
    u = "".join('<div class="s13-u cut cut-s"><span class="s13-v" data-u="%s">--</span><span class="s13-k">%s</span></div>' % x
                for x in [("d", "D"), ("h", "H"), ("m", "M"), ("s", "S")])
    return """<div class="tpl-sub reveal">
  <div class="S-13-Countdown--compact s13 s13-compact cut cut-m" data-until="2026-09-26T10:00:00Z">
    <div class="s13-head">
      <div class="s13-t">Next stop &middot; Deqing</div>
      <div class="s13-sub">Deqing, China &middot; 26 September 2026</div>
    </div>
    <div class="s13-units">%s</div>
  </div>
</div>""" % u

# ================================================================ news
def news_card(n, lead=False):
    w = 1200 if lead else 640
    return """<div class="c02-hcard%s" data-href="%s" tabindex="0" role="link">
  <div class="c02-himg cut cut-m"><img src="%s" alt="" loading="lazy"></div>
  <div class="c02-hb">
    <div style="display:flex">%s</div>
    <div class="c02-title">%s</div>
    <span class="t-caption">%s</span>
  </div>
</div>""" % (' wt-news-lead' if lead else '', n['href'], cld(n['ver'], n['img'], w),
           chip_plain(n['tag'], 'xs'), n['t'], n['date'])

def news_block():
    side = "".join(news_card(n) for n in NEWS[1:5])
    return """<div class="tpl-sub reveal">
  %s
  <div class="C-02-NewsRail--grid wt-news">%s<div class="wt-news-side">%s</div></div>
</div>""" % (sec_head("Latest news", lnk("All news")), news_card(NEWS[0], True), side)

# ================================================================ tables
def thead(cells):
    c = "".join('<div class="cell %s"><span class="t-caption" style="color:inherit">%s</span></div>' % (cl, t)
                for cl, t in cells)
    return '<div class="el-08-TableHeaderRow cut cut-s thead">%s</div>' % c

def trow(cells, extra="", href=None, small=False):
    c = "".join('<div class="cell %s">%s</div>' % (cl, v) for cl, v in cells)
    at = ' data-href="%s" tabindex="0" role="link"' % href if href else ''
    return '<div class="el-04-TeamRow trow%s %s"%s>%s</div>' % (' trow-sm' if small else '', extra, at, c)

def dat(v):
    return '<span class="t-data-m">%s</span>' % v

# ================================================================ split
def overview():
    """S-09 Overview — the module, with the World Tour's four figures."""
    ks = [("17", "Masters"), ("1", "Final"), ("10", "played"), ("7", "to go")]
    k = "".join('<div class="s09-k"><span class="s09-kv">%s</span><span class="s09-kl">%s</span></div>' % x for x in ks)
    ks2 = [("48", "teams ranked"), ("22", "Challengers"), ("39", "cities")]
    k2 = "".join('<div class="s09-k"><span class="s09-kv">%s</span><span class="s09-kl">%s</span></div>' % x for x in ks2)
    return """<div class="tpl-sub reveal">
  %s
  <div class="S-09-Overview--tour s09 brandstroke cut cut-m cut-out">
    <div class="cutfill"></div>
    <div class="s09-lines">
      <div class="s09-line wt-ov-line"><span class="s09-lab">Season 2026</span><div class="s09-brk">%s</div></div>
      <div class="s09-line wt-ov-line"><span class="s09-lab">The field</span><div class="s09-brk">%s</div></div>
    </div>
    <div class="s09-right"><span class="t-caption">Season progress</span>
      <div class="s09-bar"><div class="s09-track cut cut-s"></div>
        <div class="s09-fill" style="--w:59%%"><div class="s09-done cut cut-s" style="flex:1"></div><div class="s09-live cut cut-s" style="flex:0"></div></div>
      </div>
      <span class="t-caption">10 of 17 Masters played</span>
    </div>
  </div>
</div>""" % (sec_head("Overview"), k, k2)

def livenow():
    """S-01 LiveConferenceAccordion built on el-07 AccordionShell."""
    rows = []
    for pool, team, ioc, seed, pts in ZADAR_FIELD:
        me = ' wt-me' if team == 'Ub' else ''
        href = 'team.html' if team == 'Ub' else None
        rows.append(trow([('c-pool', '<div class="el-05-StatusBadge--marker-r marker marker-r cut cut-s"><span class="lbl">%s</span></div>' % pool),
                          ('c-team', ftag(team, ioc)),
                          ('c-n1 cell-num', dat(seed)),
                          ('c-n2 cell-num', dat(pts if pts is not None else '&mdash;'))],
                         extra=me, href=href, small=True))
    head_ = thead([('c-pool', 'Pool'), ('c-team', 'Team'), ('c-n1 cell-num', 'Seed'), ('c-n2 cell-num', 'Tour pts')])
    return """<div class="tpl-sub reveal">
  %s
  <div class="S-01-LiveAccordion--open el-07-AccordionShell--default acc cut cut-m cut-out" data-open="true">
    <div class="cutfill"></div>
    <div class="acc-head cut-tb" role="button" tabindex="0" aria-expanded="true">
      <div class="acc-left">%s<span class="t-h3">Zadar</span><span class="t-body-s">Masters &middot; Stop 3 of 17 &middot; Greeting to the Sun</span></div>
      <div class="acc-left">
        <div class="dots-wrap"><div class="dots"><div class="dot dot-done"></div><div class="dot dot-done"></div><div class="dot dot-live"></div><div class="dot"></div><div class="dot"></div><div class="dot"></div></div><span class="t-caption">Stop 3 of 17</span></div>
        <span class="acc-caret">%s</span>
      </div>
    </div>
    <div class="acc-fold"><div class="acc-body">
      <div class="wt-game">
        <div class="wt-game-t">%s<span class="wt-game-n">Ub</span><span class="wt-game-s">14</span></div>
        <div class="wt-game-mid">%s<span class="t-caption">Pool A &middot; 6:42</span></div>
        <div class="wt-game-t r"><span class="wt-game-s">11</span><span class="wt-game-n">Toronto</span>%s</div>
      </div>
      <div class="wt-tbl">%s%s</div>
    </div></div>
  </div>
</div>""" % (sec_head("Live now"), badge_live(), sv(P_DOWN, 24), flag('SRB'), badge_live(), flag('CAN'),
             head_, "".join(rows))

def worldranking(rows=None):
    """R-02 StandingsTable — el-08 + el-04, the Tour standings."""
    n = rows or len(STANDINGS)
    tr = []
    for rk, team, ioc, pts, wp, avg in STANDINGS[:n]:
        me = ' wt-me' if team == 'Ub' else ''
        href = 'team.html' if team == 'Ub' else None
        tr.append(trow([('c-rk', dat(rk)), ('c-team', ftag(team, ioc)), ('c-n1 cell-num', dat(pts))],
                       extra=me, href=href, small=True))
    return """<div class="tpl-sub reveal">
  %s
  <div class="R-02-StandingsTable--tour wt-tbl">%s%s</div>
  <div>%s</div>
</div>""" % (sec_head("World ranking"),
             thead([('c-rk', '#'), ('c-team', 'Team'), ('c-n1 cell-num', 'Pts')]),
             "".join(tr), btn("Full standings", kind="outline"))

def split_block(rows=None):
    return """<div class="tpl-split wt-split">
  <div class="tpl-colL">%s%s</div>
  <div class="tpl-colR">%s</div>
</div>""" % (overview(), livenow(), worldranking(rows))

# ================================================================ find
def find_block():
    teams = ["Ub", "Liman", "Amsterdam RABOBANK", "Baskets Bonn", "Miami", "Antwerp", "Shanghai", "Vienna"]
    players = ["Stojacic", "de Jong", "Giessmann", "Nerandžić", "Caruso", "Milivojevic", "Parrott", "Travis"]
    def panel(title, placeholder, xs):
        cs = "".join(chip(x, "team.html" if x == "Ub" else "#") for x in xs)
        return """<div class="tpl-sub">%s
  <div class="E-01-TeamFinder--default" style="display:flex;flex-direction:column;gap:16px">
    <div class="el-11-SearchInput--default search cut cut-m cut-out"><div class="cutfill"></div>%s<div class="search-txt">%s</div></div>
    <div class="wt-chips">%s</div>
  </div>
</div>""" % (sec_head(title), sv(P_SEARCH, 24), placeholder, cs)
    return """<div class="tpl-sub reveal"><div class="wt-find">%s%s</div></div>""" % (
        panel("Find a team", "Search 48 teams on the 2026 Tour", teams),
        panel("Find a player", "Search every player on the 2026 Tour", players))

# ================================================================ E-08
COURT = None
def court_svg():
    global COURT
    if COURT is None:
        COURT = io.open(os.path.join(OUT, 'assets/img/court-white.svg'), encoding='utf-8').read().replace('\n', '')
    return COURT

def pcard(p, size="xs", rank=None, k1=("World", "rank"), v1=None, k2=("Ranking", "pts"), v2=None, href="#"):
    """E-08 PlayerCard — the module's four layers, branding slot 3 in
       the key visual, a real cut-out where the silhouette was."""
    v1 = v1 if v1 is not None else str(p.get('rk', ''))
    v2 = v2 if v2 is not None else p.get('pts', '')
    rankplate = '<div class="pcard-rank">%s</div>' % rank if rank else ''
    kk = lambda t: '<span>%s</span><span>%s</span>' % t
    return """<a class="nav-a sh sh-e1 sh-lift pcard-sh" href="%s">
 <div class="E-08-PlayerCard--wt pcard pcard-%s cut cut-l">
  <div class="cutfill"></div><div class="pcard-shine"></div>
  <div class="pcard-shot"><img class="pcard-photo" src="%s" alt="%s %s" loading="lazy"></div>
  <div class="pcard-kv wt-kv"><img src="assets/img/wt-el-card.svg" alt=""></div>
  %s
  <div class="pcard-stats">
   <div class="pcard-stat"><div class="pcard-k">%s</div><div class="pcard-v">%s</div></div>
   <div class="pcard-stat"><div class="pcard-k">%s</div><div class="pcard-v">%s</div></div>
  </div>
  <div class="pcard-plate cut cut-m">
   <div class="pcard-flagbox">%s<span class="pcard-ioc">%s</span></div>
   <div class="pcard-names"><div class="pcard-first">%s</div><div class="pcard-last">%s</div></div>
  </div>
 </div>
</a>""" % (href, size, photo(p['uuid']), p['first'], p['last'], rankplate,
           kk(k1), v1, kk(k2), v2, flag(p['ioc'], ring=False), p['ioc'], p['first'], p['last'])

def cards_block():
    cs = "".join(pcard(p, "xs", rank=str(p['rk']), href="team.html" if p['team'] == "Ub" else "#") for p in PLAYERS)
    return """<div class="tpl-sub reveal">
  %s
  <div class="E-10-RosterGrid--cards wt-cards">%s</div>
</div>""" % (sec_head("Individual world ranking",
             '<div style="display:flex;align-items:center;gap:16px"><span class="t-caption">Updated 3 Sep 2026</span>%s</div>' % lnk("Full ranking")), cs)

# ================================================================ ad / road / shorts / photos
def ad_block():
    return """<div class="tpl-sub">
  <div class="el-29-AdSpace--full ad ad-full cut cut-m cut-out"><div class="cutfill"></div>
    <span class="ad-lbl">Advertising</span><span class="ad-dim">1440 x 160</span></div>
</div>"""

def meter(label_html, value, pct):
    """el-31 MeterBar, accent variant."""
    return """<div class="el-31-MeterBar--accent meter meter-accent">
  <div class="meter-top"><div class="meter-lab">%s</div><span class="meter-v">%s</span></div>
  <div class="meter-track cut cut-s"><div class="meter-fill cut cut-s" style="--w:%d%%"></div></div>
</div>""" % (label_html, value, pct)

def road_block():
    top = 575
    qualified = [("Ub", "SRB", 575), ("Liman", "SRB", 535), ("Amsterdam RABOBANK", "NED", 430), ("Baskets Bonn", "GER", 428)]
    chasing = [("Skyliners", "GER", 303), ("Antwerp", "BEL", 300), ("Miami", "USA", 295), ("Ulaanbaatar MMC Energy", "MGL", 293)]
    def meters(xs):
        return "".join(meter('%s<span>%s</span>' % (flag(i), t), p, max(4, round(p * 100.0 / top))) for t, i, p in xs)
    def panel(k, v, body):
        return """<div class="el-16-Card--default card cut cut-m cut-out" style="width:100%%"><div class="cutfill"></div>
  <div class="wt-pad"><span class="t-caption">%s</span><div class="t-h3">%s</div>%s</div></div>""" % (k, v, body)

    def final_panel():
        """el-16 Card, media variant: the photograph is the surface and
           the type sits on it. The only card in the row that is a place
           rather than a table."""
        return ("""<div class="el-16-Card--media card wt-final cut cut-m">
  <img class="wt-final-img" src="__RIO__" alt="Rio de Janeiro" loading="lazy">
  <span class="wt-final-scrim"></span>
  <div class="wt-final-in">
    <span class="t-caption">The Final</span>
    <div class="t-h3">Rio de Janeiro</div>
    <p class="t-body-s">The season ends with the twelve best teams of 2026, on the sand at Copacabana. Seven Masters still to play.</p>
  </div>
</div>""").replace("__RIO__", RIO_SRC)
    todo = "".join('<div class="meter-top"><div class="meter-lab"><span>%s</span></div><span class="meter-v">%s</span></div>' % x
                   for x in [("Deqing", "26 Sep"), ("Málaga", "10 Oct"), ("Macau", "24 Oct"),
                             ("Zaisan", "14 Nov"), ("Manama", "28 Nov"), ("Hong Kong", "5 Dec")])
    return """<div class="tpl-sub reveal">
  %s
  <div class="wt-road">
    %s%s%s%s
  </div>
</div>""" % (sec_head("Road to the Final", lnk("How teams qualify")),
             final_panel(),
             panel("In the twelve", "Leading four", '<div style="display:flex;flex-direction:column;gap:12px">%s</div>' % meters(qualified)),
             panel("Chasing", "5th to 8th", '<div style="display:flex;flex-direction:column;gap:12px">%s</div>' % meters(chasing)),
             panel("Still to come", "7 Masters", '<div style="display:flex;flex-direction:column;gap:8px">%s</div>' % todo))

def shorts_block():
    """el-32 VideoThumb — added to the design system by this build."""
    cs = []
    for vid, title in SHORTS:
        cs.append("""<a class="nav-a el-32-VideoThumb--portrait vth" href="https://www.youtube.com/shorts/%s" target="_blank" rel="noopener">
  <div class="vth-p cut cut-m">
    <img src="https://i.ytimg.com/vi/%s/oar2.jpg" alt="" loading="lazy">
    <span class="vth-scrim"></span>
    <span class="vth-badge cut cut-s">%s Shorts</span>
  </div>
  <span class="vth-t">%s</span>
</a>""" % (vid, vid, sv(P_PLAY, 12), title))
    return """<div class="tpl-sub reveal">
  %s
  <div class="wt-shorts">%s</div>
</div>""" % (sec_head("Top moment", lnk("All Shorts", "https://www.youtube.com/@FIBA3x3/shorts")), "".join(cs))

def photos_block(items, title="Photos"):
    """C-03 PhotoGallery — the module's tiles and el-22 indicator."""
    cs = []
    for t, n, ver, ident in items:
        cs.append("""<a class="nav-a" href="#"><div class="car-slide cut cut-m">
  <img src="%s" alt="" loading="lazy"><span class="car-cap">%s %s</span></div>
  <span class="t-caption" style="display:block;padding-top:10px">%s</span></a>""" % (cld(ver, ident, 640), sv(P_CAM, 13), n, t))
    ind = ('<div class="el-22-CarouselIndicator--prog ind"><div class="ind-prog cut cut-s"><div class="ind-fill" style="width:22px"></div></div>'
           + '<div class="ind-d cut cut-s"></div>' * 4 + '</div>')
    ctrl = ('<div class="car-ctrl"><div class="car-btn cut cut-s cut-out"><div class="cutfill"></div>%s</div>'
            '<div class="car-btn cut cut-s cut-out"><div class="cutfill"></div>%s</div></div>' % (sv(P_LEFT, 20), sv(P_RIGHT, 20)))
    return """<div class="tpl-sub reveal">
  %s
  <div class="C-03-PhotoGallery--auto car">
    <div class="wt-photos">%s</div>
    <div class="car-bar">%s%s</div>
  </div>
</div>""" % (sec_head(title, lnk("All galleries")), "".join(cs), ind, ctrl)

# ================================================================ F-06
def footer():
    cols = [
        ("The Tour", ["Teams", "Standings", "Stats", "Calendar", "How to qualify"]),
        ("Watch", ["Videos", "Where to watch", "Live streams", "Top moments"]),
        ("Events", ["Masters", "Challengers", "Quests", "The Final", "Host a stop"]),
        ("3x3", ["Nations League", "Women's Series", "World Cup", "Europe Cup", "Play 3x3"]),
        ("About", ["Contact support", "Media services", "Terms and conditions", "Privacy policy"]),
    ]
    c = "".join('<div class="f06-col"><span class="f06-colh">%s</span>%s</div>'
                % (h, "".join('<a class="nav-a" href="#"><span class="f06-link">%s</span></a>' % x for x in xs))
                for h, xs in cols)
    sup = "".join('<div class="brandlogo"><img src="assets/img/%s" alt="" style="width:%dpx">' % v + '</div>'
                  for v in [("spon-avant.svg", 104), ("spon-bodet.svg", 62), ("spon-enlio.svg", 62),
                            ("spon-magicsky.svg", 30), ("spon-schelde.svg", 84)])
    soc = "".join('<a class="nav-a" href="#"><div class="brandlogo"><img src="assets/img/soc-%d.svg" alt="" width="22" height="22"></div></a>' % i
                  for i in (1, 2, 3, 4))
    return """<footer class="F-06-SiteFooter--default f06 wt-bleed">
  <div class="f06-spon">
    <div class="f06-spongrp"><span class="t-caption">Official ball</span>
      <div class="brandlogo"><img src="assets/img/spon-wilson.svg" alt="Wilson" style="width:92px"></div></div>
    <div class="f06-spongrp"><span class="t-caption">Official suppliers</span>
      <div class="f06-sponlogos">%s</div></div>
  </div>
  <div class="f06-brandrow">
    <div class="f06-brand"><div class="brandlogo"><img src="assets/img/wt-lockup.svg" alt="FIBA 3x3 World Tour" width="231" height="31"></div></div>
    <div class="f06-social">%s</div>
  </div>
  <div class="f06-cols">%s</div>
  <div class="f06-bar">
    <div class="f06-fiba"><div class="brandlogo"><img src="assets/img/logo-fiba.svg" alt="FIBA" width="83" height="40"></div></div>
    <div class="f06-legal">Copyright FIBA. All rights reserved. The 3x3 marks (including but not limited to the FIBA 3x3 Endorsement Stamp, the FIBA 3x3 Infinity Logo and the 3x3 word mark) are FIBA intellectual property, protected by trade mark and/or copyright laws around the world. All use of the 3x3 marks must be with the consent of FIBA and under the control of FIBA.</div>
  </div>
</footer>""" % (sup, soc, c)

# ================================================================ home
def home(rows=None):
    return (head("FIBA 3x3 World Tour 2026")
            + chrome("Home")
            + hero()
            + '<main class="tpl-content">'
            + countdown()
            + news_block()
            + split_block(rows)
            + find_block()
            + cards_block()
            + ad_block()
            + road_block()
            + shorts_block()
            + photos_block(PHOTOS_HOME)
            + '</main>'
            + footer() + TAIL)

# ================================================================ team
def team():
    spot = [("World Tour rank", "1"), ("Tour points", "575"), ("Masters won", "2"),
            ("Games played", "33"), ("Games won", "24"), ("Win %", "72"), ("Points avg", "19.3")]
    sp = "".join('<div class="wt-spot-c"><span class="t-caption">%s</span><span class="wt-spot-v">%s</span></div>' % x for x in spot)
    roster = "".join(pcard(p, "xs") for p in UB_ROSTER)
    sel = "".join('<div class="meter-top"><div class="meter-lab"><span>%s</span></div><span class="meter-v">Hard seed</span></div>' % n
                  for n in UB_SELECTIONS)
    jr = []
    for name, tier, dates, standing, pts, qual in UB_SEASON:

        me = ' wt-me' if name == 'Zadar' else ''
        jr.append(trow([('c-event', '<span class="t-data-m">%s</span>' % name),
                        ('c-tier', chip_plain(tier)),
                        ('c-dates', '<span class="t-body-s">%s</span>' % dates),
                        ('c-n1 cell-num', dat(standing)),
                        ('c-n1 cell-num', dat(pts)),
                        ('c-entry', '<span class="t-body-s" style="color:var(--text-muted)">%s</span>' % qual)],
                       extra=me))
    crumb = ('<div class="el-23-Breadcrumb--three-levels crumbs">'
             '<a class="nav-a" href="index.html"><span class="crumb">World Tour 2026</span></a>'
             '<span class="crumb-sep">%s</span><a class="nav-a" href="#"><span class="crumb">Teams</span></a>'
             '<span class="crumb-sep">%s</span><span class="crumb crumb-cur">Ub</span></div>' % (sv(P_RIGHT, 14), sv(P_RIGHT, 14)))
    return (head("Ub | FIBA 3x3 World Tour 2026")
        + chrome("Teams")
        + """<div class="tpl-content" style="padding-bottom:0;gap:0">
  <div class="tpl-sub" style="padding:20px 0 16px 0">%s</div>
</div>
<img class="wt-subbar wt-bleed" src="assets/img/wt-bar.svg" alt="">
<main class="tpl-content" style="padding-top:28px">
  <div class="tpl-sub">
    <div class="E-04-TeamHeader--qualified wt-subhead">
      <div class="wt-subhead-l"><h1 class="wt-h1">Ub</h1><span class="wt-h1-sub">%s Serbia &middot; World No.&nbsp;1</span></div>
      <div style="display:flex;align-items:center;gap:16px"><span class="t-caption">Hard seeded &middot; 2026</span>%s</div>
    </div>
    <div class="el-16-Card--default card cut cut-m cut-out" style="width:100%%"><div class="cutfill"></div>
      <div class="wt-spot">%s</div>
    </div>
  </div>
  <div class="tpl-sub reveal">%s<div class="E-10-RosterGrid--cards wt-roster">%s</div></div>
  <div class="tpl-sub reveal">
    <div class="wt-two">
      <div class="tpl-sub">%s
        <div class="el-16-Card--default card cut cut-m cut-out" style="width:100%%"><div class="cutfill"></div>
          <div class="wt-pad"><div style="display:flex;flex-direction:column;gap:10px">%s</div>
          <p class="t-body-s">A hard-seeded team picks the Masters it will play. These four were confirmed in January; the rest of Ub&#39;s season is earned through Challengers and performance slots.</p></div>
        </div>
      </div>
      <div class="tpl-sub">%s
        <div class="R-02-StandingsTable--journey wt-tbl">%s%s</div>
      </div>
    </div>
  </div>
  %s
</main>""" % (crumb, flag('SRB'), btn("Follow", kind="outline"), sp,
              sec_head("Roster", '<span class="t-caption">Six registered players</span>'), roster,
              sec_head("Event selections"), sel,
              sec_head("Season journey", lnk("All results")),
              thead([('c-event', 'Event'), ('c-tier', 'Tier'), ('c-dates', 'Dates'),
                     ('c-n1 cell-num', 'Finish'), ('c-n1 cell-num', 'Pts'), ('c-entry', 'Entry')]),
              "".join(jr),
              photos_block(PHOTOS_TEAM, "Photos"))
        + footer() + TAIL)

if __name__ == '__main__':
    rows = int(sys.argv[1]) if len(sys.argv) > 1 else None
    io.open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8').write(home(rows))
    io.open(os.path.join(OUT, 'team.html'), 'w', encoding='utf-8').write(team())
    print('wrote index.html + team.html')
