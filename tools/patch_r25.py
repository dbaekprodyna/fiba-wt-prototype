#!/usr/bin/env python3
"""
FIBA 3x3 World Tour prototype — 25th round (phone only).
  1  hero corner key visuals back to full band height, each shown as
     the sliver of its own inner edge
  2  a rail is clipped by the screen edge, never by the page margin,
     and every snap position lands on the margin
  3  Season journey: no rule down the right of the pinned column
Idempotent. Run from the repo root.
"""
import io, os

ROOT = os.path.dirname(os.path.abspath(__file__))
if not os.path.exists(os.path.join(ROOT, 'index.html')):
    ROOT = os.getcwd()

def read(p):
    with io.open(os.path.join(ROOT, p), encoding='utf-8') as f: return f.read()

def write(p, s):
    with io.open(os.path.join(ROOT, p), 'w', encoding='utf-8') as f: f.write(s)

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

m = read('assets/mobile.css')

# --- 1. the corner key visuals ------------------------------------------
old_kv = """  /* The two supplied corner elements are drawn at the band's full
     192px height. On a phone they come down to a third of it and sit
     on the floor of the band, below the lock-up's line — present at
     both edges, and never behind the type. */
  .hwt-kv-l, .hwt-kv-r { display: block; }
  .hwt-kv {
    top: auto;
    bottom: 0;
    height: 54px;
  }"""
new_kv = """  /* The two supplied corner elements keep the band's full 192px
     height, as they do on a desktop — they are not shrunk, they are
     cropped. Each is pushed out past its own screen edge until only
     the sliver facing the middle of the band is left: the right end
     of the left element, the left end of the right element. The
     translate is written against the element's OWN width (-100%),
     so the sliver stays the stated width whatever the artwork
     measures, and the band's overflow does the cutting. */
  .hwt-kv-l, .hwt-kv-r { display: block; }
  .hwt-kv {
    top: 0;
    bottom: auto;
    height: var(--wt-hero-h);
    --kv-peek: clamp(52px, 18vw, 96px);
  }
  .hwt-kv-l {
    left: 0;
    right: auto;
    transform: translateX(calc(var(--kv-peek) - 100%));
  }
  .hwt-kv-r {
    right: 0;
    left: auto;
    transform: translateX(calc(100% - var(--kv-peek)));
  }"""
m = sub_once(m, old_kv, new_kv, 'mobile.css: hero corner KVs at full height, edge slivers')

# --- 2. the rails are cut by the screen, not by the margin ---------------
old_bleed = """    gap: 12px;
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
new_bleed = """    gap: 12px;
    /* 25th round. Two things have to be true at once, and
       scroll-padding is what makes them both true.

       The margin has to hold: at rest, the leading card starts on
       the same 16px line as Next stop and Overview, and the section
       never puts a sliced card in the gutter.

       And the cut has to happen off the page: a card leaving the
       screen should run off the screen's own edge, the way a rail
       does, rather than be chopped on the margin line — that reads
       as broken artwork, not as a row that moves.

       So the scroller bleeds to both screen edges (the negative
       margin), its content is inset by the page gutter (the
       padding), and scroll-padding moves every snap position in by
       that same gutter. Snap to a card and it lands on the margin;
       between snaps the overflow disappears under the screen edge. */
    margin-left: -16px;
    margin-right: -16px;
    padding: 0 16px;
    width: auto;
    scroll-padding-left: 16px;
    scroll-padding-right: 16px;
    overflow-x: auto;"""
m = sub_once(m, old_bleed, new_bleed, 'mobile.css: rails bleed to the screen, snap to the margin')

# --- 3. Season journey ---------------------------------------------------
old_jrn = """  .wt-jrn {
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
    overscroll-behavior-x: contain;
  }"""
new_jrn = """  .wt-jrn {
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
    overscroll-behavior-x: contain;
    /* Same reason as the rails, on the side that scrolls. The left
       edge stays on the margin because the pinned Event column is
       parked there; the right edge is let out to the screen so a
       half-read cell is cut by the phone rather than by the gutter. */
    margin-right: -16px;
    /* .wt-tbl states width:100%, so the negative margin alone would
       only let the box overlap the gutter, not grow into it. */
    width: calc(100% + 16px);
    padding-right: 16px;
  }"""
m = sub_once(m, old_jrn, new_jrn, 'mobile.css: journey table cut by the screen on the right')

old_sticky = """    background-color: inherit;
    box-shadow: 1px 0 0 var(--border-subtle);
  }"""
new_sticky = """    background-color: inherit;
  }"""
m = sub_once(m, old_sticky, new_sticky, 'mobile.css: no rule down the pinned Event column')

write('assets/mobile.css', m)
print('done.')
