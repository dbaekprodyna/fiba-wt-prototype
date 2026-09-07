#!/usr/bin/env python3
"""
FIBA 3x3 World Tour prototype — 24th round of design corrections.
Idempotent: every edit is guarded by a marker or an exact-once replace.
Run from the repo root.
"""
import io, os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
if not os.path.exists(os.path.join(ROOT, 'index.html')):
    ROOT = os.getcwd()

def read(p):
    with io.open(os.path.join(ROOT, p), encoding='utf-8') as f:
        return f.read()

def write(p, s):
    with io.open(os.path.join(ROOT, p), 'w', encoding='utf-8') as f:
        f.write(s)

def sub_once(s, old, new, label):
    n = s.count(old)
    if n == 0:
        if new in s:
            print('   = already applied:', label); return s
        raise SystemExit('!! NOT FOUND: ' + label)
    if n != 1:
        raise SystemExit('!! %d matches (want 1): %s' % (n, label))
    print('   + ', label)
    return s.replace(old, new, 1)

# ------------------------------------------------------------------ team.html
t = read('team.html')

# D-2 / M-6 : the sub-header image -> headline spacing is the main's own
# padding-top (28) plus wt.css's first-.tpl-sub padding-top (40 desktop /
# 24 phone) = 68 / 52. Both come down to a third: 23 / 17.
t = sub_once(t,
    '<main class="tpl-content" style="padding-top:28px">',
    '<main class="tpl-content wt-subtop">',
    'team.html: main -> .wt-subtop (sub-header spacing)')

# M-7 : mark the Season journey table so the phone layer can give it a
# sticky first column without touching the other R-02 tables.
t = sub_once(t,
    '<div class="R-02-StandingsTable--journey wt-tbl">',
    '<div class="R-02-StandingsTable--journey wt-tbl wt-jrn">',
    'team.html: journey table -> .wt-jrn')

write('team.html', t)

# ------------------------------------------------------------------- wt.css
c = read('assets/wt.css')

# D-1 / M-1 : the player-card stat labels read on one line.
old_k = """.wt-cards .pcard-k, .wt-roster .pcard-k {
  display: flex; flex-direction: column; align-items: flex-end;
  line-height: 1.2; text-align: right;
}"""
new_k = """.wt-cards .pcard-k, .wt-roster .pcard-k {
  display: flex; flex-direction: row; align-items: baseline;
  justify-content: flex-end; gap: 0.32em;
  line-height: 1.2; text-align: right; white-space: nowrap;
}"""
c = sub_once(c, old_k, new_k, 'wt.css: .pcard-k label on one line')

# also drop the now-wrong comment above it
c = c.replace(
    "/* the stat column reads down the top-right corner the key visual\n   leaves free, so each label breaks onto its own second line */",
    "/* the stat column reads down the top-right corner the key visual\n   leaves free; each label stays on one line (24th round) */")

if '.wt-subtop' not in c:
    c += """

/* ---------------------------------------------------------------
   24th round — the sub-page headline sits closer to its 4px bar.
   The gap was the main's 28px plus F-04's own 40px first-block
   padding; both are folded into one third of that on the block
   itself, so the bar and the name read as one lock-up.
   --------------------------------------------------------------- */
.wt-subtop { padding-top: 0; }
.wt-subtop > .tpl-sub:first-child { padding-top: 23px; }
"""
    print('   +  wt.css: .wt-subtop spacing block')
else:
    print('   =  wt.css: .wt-subtop already there')

write('assets/wt.css', c)

# --------------------------------------------------------------- mobile.css
m = read('assets/mobile.css')

# M-2 : the city strip scrolls sideways and only sideways.
old_s14 = """  .s14 { padding: 0 12px; gap: 8px; }
  .s14-nav { display: none; }
  .s14-scroll { scrollbar-width: none; }
  .s14-scroll::-webkit-scrollbar { display: none; }"""
new_s14 = """  .s14 { padding: 0 12px; gap: 8px; }
  .s14-nav { display: none; }
  /* overflow-x:auto with overflow-y left at visible makes the second
     axis auto too, so a diagonal swipe drags the strip up and down
     inside its own 44px box. The strip is a rail: one axis, and the
     browser is told so for the touch handler as well as the layout. */
  .s14-scroll {
    overflow-x: auto;
    overflow-y: hidden;
    touch-action: pan-x;
    overscroll-behavior-x: contain;
    overscroll-behavior-y: none;
    scrollbar-width: none;
  }
  .s14-scroll::-webkit-scrollbar { display: none; }"""
m = sub_once(m, old_s14, new_s14, 'mobile.css: S-14 horizontal-only scroll')

# M-3 : the hero. The corner key visuals come back at a size the band
# can hold, and the lock-up is sized by its own strapline.
old_hero = """  .hwt-in { padding: 0 16px; }
  .hwt-lock { flex-direction: column; align-items: center; gap: 10px; }
  .hwt-logo { width: min(72vw, 280px); }
  .hwt-s {
    font-size: 13px;
    line-height: 16px;
    letter-spacing: 0.6px;
    white-space: normal;
    text-align: center;
  }
  .hwt-kv-l, .hwt-kv-r { display: none; }"""
new_hero = """  .hwt-in { padding: 0 16px; }
  /* The strapline is the measure. It is set on one line and the
     lock-up above it is stretched to exactly that line's width, so
     the two read as one block rather than as a logo with a caption
     under it. `width: 0` keeps the logo out of the column's own
     intrinsic width — otherwise the 385px artwork would set it —
     and `min-width: 100%` paints it back at the column's width. */
  .hwt-lock {
    flex-direction: column;
    align-items: stretch;
    width: max-content;
    max-width: 100%;
    gap: 6px;
  }
  .hwt-logo { width: 0; min-width: 100%; height: auto; }
  .hwt-s {
    font-size: 12px;
    line-height: 15px;
    letter-spacing: 0.4px;
    white-space: nowrap;
    text-align: center;
  }
  /* The two supplied corner elements are drawn at the band's full
     192px height. On a phone they come down to a third of it and sit
     on the floor of the band, below the lock-up's line — present at
     both edges, and never behind the type. */
  .hwt-kv-l, .hwt-kv-r { display: block; }
  .hwt-kv {
    top: auto;
    bottom: 0;
    height: 54px;
  }"""
m = sub_once(m, old_hero, new_hero, 'mobile.css: hero lock-up + corner KVs')

# M-4 : every section keeps the page's own 16px gutters. The rails
# stop bleeding to the screen edge.
old_bleed = """    gap: 12px;
    /* full bleed: the rail reaches both edges of the screen and
       no further, so the next card shows and the swipe reads */
    margin-left: -16px;
    margin-right: -16px;
    padding: 0 16px;
    width: auto;
    overflow-x: auto;"""
new_bleed = """    gap: 12px;
    /* 24th round: the rails sit inside the page's own gutters, so
       Latest news, Individual world ranking, Road to the Final, Top
       moment and Photos start and end on the same two lines as Next
       stop and Overview. The next card still shows — that is the
       card width's job, not the bleed's. */
    margin-left: 0;
    margin-right: 0;
    padding: 0;
    width: 100%;
    overflow-x: auto;"""
m = sub_once(m, old_bleed, new_bleed, 'mobile.css: rails inside the 16px gutters')

# M-5 : no scrollbar under a section that swipes — neither the browser's
# own nor the el-22 bar that was standing in for one.
old_ind = """  /* ---- the el-22 bar under each rail ----------------------- */
  .wt-railind {
    display: flex;
    width: 100%;
    margin-top: 14px;
  }
  .wt-railind .ind-prog { width: 100%; height: 4px; }
  .wt-railind .ind-fill { height: 4px; }"""
new_ind = """  /* ---- the el-22 bar under each rail -----------------------
     24th round: withdrawn. A bar under a rail reads as a scrollbar,
     not as an indicator, and the card edge showing at the gutter
     already says the row moves. mobile.js still builds and tracks
     it, so restoring it is one display value. */
  .wt-railind {
    display: none;
    width: 100%;
    margin-top: 14px;
  }
  .wt-railind .ind-prog { width: 100%; height: 4px; }
  .wt-railind .ind-fill { height: 4px; }

  /* and no native bar on anything that scrolls sideways */
  .wt-news-side, .wt-cards, .wt-road, .wt-shorts, .wt-photos,
  .s14-scroll, .wt-tbl, .car, .mscroll {
    scrollbar-width: none;
    -ms-overflow-style: none;
  }
  .wt-news-side::-webkit-scrollbar, .wt-cards::-webkit-scrollbar,
  .wt-road::-webkit-scrollbar, .wt-shorts::-webkit-scrollbar,
  .wt-photos::-webkit-scrollbar, .s14-scroll::-webkit-scrollbar,
  .wt-tbl::-webkit-scrollbar, .car::-webkit-scrollbar,
  .mscroll::-webkit-scrollbar { width: 0; height: 0; display: none; }"""
m = sub_once(m, old_ind, new_ind, 'mobile.css: rail indicator + scrollbars off')

# M-6 / M-7 : the team page block
if 'wt-subtop' not in m:
    m += """

/* ============================================================
   D. The team page  (phone) — 24th round
   ============================================================ */
@media (max-width: 767px) {

  /* ---- F-04's 4px bar -------------------------------------
     The bar was the one thing on the page still running to both
     screen edges. It is a rule under a headline, so it starts and
     stops where the headline does. */
  .wt-subbar {
    height: 4px;
    width: calc(100% - 32px);
    margin-left: 16px;
    margin-right: 16px;
  }
  /* and the headline comes up to meet it — a third of the gap */
  .wt-subtop > .tpl-sub:first-child { padding-top: 17px; }

  /* ---- R-02 Season journey --------------------------------
     Six columns of prose will not fit 358px and must not be
     squeezed into it, so this one table scrolls sideways the way
     the Nations League's do: the rows are laid out at their own
     width, the event column is pinned to the left edge, and every
     cell holds one line that ends in an ellipsis rather than
     wrapping to two. mobile.js cuts the text itself at 12
     characters; this is the frame it sits in. */
  .wt-jrn {
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
    overscroll-behavior-x: contain;
  }
  .wt-jrn > .trow, .wt-jrn > .thead {
    width: max-content;
    min-width: 100%;
  }
  .wt-jrn .cell { padding: 0 10px; }
  .wt-jrn .c-event {
    position: sticky;
    left: 0;
    z-index: 3;
    flex: 0 0 132px;
    width: 132px;
    min-width: 132px;
    background-color: inherit;
    box-shadow: 1px 0 0 var(--border-subtle);
  }
  .wt-jrn .c-tier  { flex: 0 0 116px; width: 116px; }
  .wt-jrn .c-dates { flex: 0 0 104px; width: 104px; }
  .wt-jrn .c-n1    { flex: 0 0 68px;  width: 68px; }
  .wt-jrn .c-entry { flex: 0 0 132px; width: 132px; }
  .wt-jrn .cell > span, .wt-jrn .cell .lbl {
    display: block;
    min-width: 0;
    max-width: 100%;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  .wt-jrn .thead .cell .t-caption { white-space: nowrap; }
  /* el-14 Chip is a cut-corner surface; it may shrink, not wrap */
  .wt-jrn .chip { min-height: 0; min-width: 0; }
}
"""
    print('   +  mobile.css: team-page block (bar, spacing, journey table)')
else:
    print('   =  mobile.css: team-page block already there')

write('assets/mobile.css', m)

# ---------------------------------------------------------------- mobile.js
j = read('assets/mobile.js')

if 'truncCells' not in j:
    addition = """

/* ------------------------------------------------------------------
   24th round — Season journey cells hold 12 characters on a phone.
   A proportional font cannot be cut by CSS at a character count, so
   the text is cut here and the original kept on the node. Above the
   phone breakpoint every cell is put back, which is what makes this
   safe to run on a resize as well as on load.
   ------------------------------------------------------------------ */
(function () {
  var LIMIT = 12;

  function truncCells() {
    var phone = window.matchMedia('(max-width: 767px)').matches;
    var nodes = document.querySelectorAll('.wt-jrn .trow .cell > span, .wt-jrn .trow .cell .lbl');
    for (var i = 0; i < nodes.length; i++) {
      var n = nodes[i];
      if (n.dataset.full === undefined) n.dataset.full = n.textContent;
      var full = n.dataset.full;
      var want = (phone && full.length > LIMIT) ? full.slice(0, LIMIT).replace(/\\s+$/, '') + '\\u2026' : full;
      if (n.textContent !== want) n.textContent = want;
      if (phone && full !== want) n.title = full;
      else n.removeAttribute('title');
    }
  }

  var t;
  function onResize() { clearTimeout(t); t = setTimeout(truncCells, 120); }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', truncCells);
  } else {
    truncCells();
  }
  window.addEventListener('resize', onResize);
})();
"""
    j = j + addition
    write('assets/mobile.js', j)
    print('   +  mobile.js: 12-character cell truncation')
else:
    print('   =  mobile.js: truncation already there')

print('done.')
