#!/usr/bin/env python3
"""Regenerate assets/mobile.js from the Nations League chrome.

The World Tour phone navigation IS the Nations League phone navigation:
the same F-03m header, the same el-18 NavTab bar, the same More sheet,
with this build's wordmark and this build's destinations. Generating it
rather than transcribing it is what stops the two drifting apart.

    python3 tools/gen_mobile.py
"""
# Generates wt/assets/mobile.js from the Nations League chrome, so the
# World Tour phone navigation is the same navigation, not a second
# interpretation of it.
import os
import re

# The Nations League repository, beside this one.
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NL_PATH = os.environ.get(
    'NL_MOBILE_JS',
    os.path.join(os.path.dirname(HERE), 'fiba-nl-prototype', 'assets', 'mobile.js'))
NL = open(NL_PATH, encoding='utf-8').read()

def tmpl(name):
    return re.search(r'var %s\s*=\s*`(.*?)`;' % name, NL, re.S).group(1)

HEADER = tmpl('HEADER')
TABBAR = tmpl('TABBAR')

# ---- HEADER: the Nations League wordmark becomes the World Tour one
i = HEADER.find('<a class="f03m-l" href="index.html" aria-label="Nations League home">')
j = HEADER.find('</a>', HEADER.find('</svg></div>', i)) + 4
assert i > 0 and j > i, (i, j)
WT_WORD = ('<a class="f03m-l" href="index.html" aria-label="World Tour home">'
           '<div class="brandlogo"><img src="assets/img/wt-logo.svg" alt="World Tour" '
           'width="90" height="18"></div></a>')
HEADER = HEADER[:i] + WT_WORD + HEADER[j:]

# ---- TABBAR: Conferences -> Standings, and the two destinations the
#      World Tour build actually has
def tab(html, name):
    a = html.find('data-tab="%s"' % name)
    start = html.rfind('<a class="mnav-tab"', 0, a)
    if start < 0:
        start = html.rfind('<div class="mnav-tab', 0, a)
    end = html.find('</a>', a)
    if end < 0 or (html.find('<a class="mnav-tab"', a) != -1 and
                   html.find('<a class="mnav-tab"', a) < end):
        end = len(html)
    return start, end + 4

s, e = tab(TABBAR, 'Conferences')
CONF = TABBAR[s:e]
# the bar chart Material Symbols draws for a standing
LEADER = ('M120-120v-80h720v80H120Zm80-160v-280h120v280H200Zm200 0v-480h120v480H400Z'
          'm200 0v-360h120v360H600Z')
STAND = CONF
STAND = STAND.replace('href="conferences.html"', 'href="#"')
STAND = STAND.replace('data-tab="Conferences"', 'data-tab="Standings"')
STAND = re.sub(r'<path d="M324-111[^"]*"></path>', '<path d="%s"></path>' % LEADER, STAND)
STAND = STAND.replace('<div class="ntab-l">Conferences</div>',
                      '<div class="ntab-l">Standings</div>')
assert 'Standings' in STAND and LEADER in STAND, STAND[:200]
TABBAR = TABBAR[:s] + STAND + TABBAR[e:]
TABBAR = TABBAR.replace('href="calendar.html"', 'href="#"')
TABBAR = TABBAR.replace('href="teams.html"', 'href="team.html"')

SHEET = """<div class="f03m-sheet mnav-sheet" hidden=""> <div class="f03m-sheet-top" style="justify-content:flex-end"> <div class="f03m-close mnav-close" role="button" tabindex="0" style="display:flex;align-items:center;gap:6px;color:var(--chrome-text-muted)"> <span class="t-caption" style="color:inherit">Close</span> <svg fill="currentColor" height="20" viewBox="0 -960 960 960" width="20"><path d="m251-160-91-91 229-229-229-229 91-91 229 229 229-229 91 91-229 229 229 229-91 91-229-229-229 229Z"></path></svg> </div> </div> <div class="f03m-sheet-body"> <div class="f03m-grp"> <div class="f03m-grp-h">World Tour</div> <a class="f03m-l" href="team.html">Teams</a> <div class="f03m-l" tabindex="0">Standings</div> <div class="f03m-l" tabindex="0">Stats</div> <div class="f03m-l" tabindex="0">News</div> <div class="f03m-l" tabindex="0">Photos</div> <div class="f03m-l" tabindex="0">Videos</div> <div class="f03m-l" tabindex="0">Calendar</div> </div> <div class="f03m-grp"> <div class="f03m-grp-h">Info</div> <div class="f03m-l" tabindex="0">About the World Tour</div> <div class="f03m-l" tabindex="0">How to qualify</div> <div class="f03m-l" tabindex="0">FAQ</div> </div> </div> </div>"""

BODY = r'''/* ============================================================
   FIBA 3x3 World Tour 2026 — mobile.js
   The phone chrome, and the five rails that swipe.

     1  F-03m header + el-18 NavTab bar + the "More" sheet,
        injected into every page — the Nations League's own
        mobile navigation, with the World Tour's wordmark and
        this build's destinations. The markup is generated from
        assets/mobile.js in the Nations League repository (see
        tools/gen_mobile.py), so the two sites cannot drift.
     2  F-06m: the footer's five columns become el-19 rows.
     3  The five home-page sections that are grids on a desktop
        become swipe rails on a phone. The rail is CSS
        (mobile.css); what is here is the el-22 progress
        indicator under it, so a reader can see how much of the
        row is still to the right.

   Nothing in this file forks a component: every class it writes
   is one the design system already documents.
   ============================================================ */
(function () {
  'use strict';

  var HEADER = `__HEADER__`;
  var TABBAR = `__TABBAR__`;
  var SHEET  = `__SHEET__`;

  function $(s, r) { return (r || document).querySelector(s); }
  function $$(s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); }

  /* ---------- 1  the chrome ---------------------------------- */
  function buildChrome() {
    if ($('.mnav')) return;

    var nav = document.createElement('div');
    nav.className = 'mnav';
    nav.innerHTML = HEADER + SHEET + TABBAR;
    document.body.appendChild(nav);

    /* Which of the five is the page you are on. Two of this
       build's pages exist; everything else on the bar is a
       destination the prototype does not draw yet, so More
       carries the mark whenever the bar cannot. */
    var here = (location.pathname.split('/').pop() || 'index.html');
    var onBar = false;
    $$('.mnav-tab', nav).forEach(function (t) {
      var href = t.getAttribute('href');
      if (href && href === here) {
        t.querySelector('.ntab').classList.add('ntab-on');
        onBar = true;
      }
    });
    if (!onBar) {
      var more = $('.mnav-more .ntab', nav);
      if (more) more.classList.add('ntab-on');
    }

    /* ---- the More sheet ------------------------------------ */
    var sheet = $('.mnav-sheet', nav);
    function openSheet(on) {
      if (!sheet) return;
      sheet.hidden = !on;
      document.documentElement.classList.toggle('mnav-locked', on);
      var m = $('.mnav-more .ntab', nav);
      if (m) m.classList.toggle('ntab-open', on);
    }
    function tap(el, fn) {
      if (!el) return;
      el.addEventListener('click', function (e) { e.preventDefault(); fn(); });
      el.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); fn(); }
      });
    }
    tap($('.mnav-more', nav), function () { openSheet(sheet.hidden); });
    tap($('.mnav-close', nav), function () { openSheet(false); });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') openSheet(false);
    });

    /* F-02 is hidden on a phone and it is the only place the
       family links live. They move into the sheet, which is
       where the mobile spec puts them. */
    var fam = $('.f02-fam');
    var body = $('.f03m-sheet-body', nav);
    if (fam && body) {
      var grp = document.createElement('div');
      grp.className = 'f03m-grp';
      grp.innerHTML = '<div class="f03m-grp-h">Competition family</div>';
      $$('.f02-famlink', fam).forEach(function (l) {
        var a = document.createElement('a');
        a.className = 'f03m-l';
        a.href = (l.closest('a') && l.closest('a').getAttribute('href')) || '#';
        a.textContent = l.textContent.trim();
        a.addEventListener('click', function () { openSheet(false); });
        grp.appendChild(a);
      });
      body.appendChild(grp);
    }
  }

  /* ---------- 2  F-06m: the footer columns fold -------------- */
  function buildFooterAccordion() {
    var cols = $('.f06-cols');
    if (!cols || $('.f06m-cols')) return;

    var wrap = document.createElement('div');
    wrap.className = 'f06m-cols disc-dark';

    $$('.f06-col', cols).forEach(function (col) {
      var head = col.querySelector('.f06-colh');
      if (!head) return;
      var links = $$('.f06-link', col);

      var disc = document.createElement('div');
      disc.className = 'disc';
      var h = document.createElement('div');
      h.className = 'disc-head';
      h.setAttribute('role', 'button');
      h.setAttribute('tabindex', '0');
      h.innerHTML = '<span class="disc-t"></span>' +
        '<svg class="disc-chev" fill="currentColor" height="20" viewBox="0 -960 960 960" width="20">' +
        '<path d="M480-345 240-585l56-56 184 184 184-184 56 56-240 240Z"></path></svg>';
      h.querySelector('.disc-t').textContent = head.textContent.trim();

      var body = document.createElement('div');
      body.className = 'disc-body';
      links.forEach(function (l) {
        /* this build wraps every footer link in an a.nav-a and puts
           the label in a span, so the href is on the ancestor */
        var href = l.closest('a') ? l.closest('a').getAttribute('href') : null;
        var a = document.createElement(href ? 'a' : 'span');
        a.className = 'disc-link';
        if (href) a.href = href;
        a.textContent = l.textContent.trim();
        body.appendChild(a);
      });
      disc.appendChild(h);
      disc.appendChild(body);
      wrap.appendChild(disc);
    });

    cols.parentNode.insertBefore(wrap, cols.nextSibling);

    /* el-19's open/close is the design system's own behaviour, and
       this build has no app.js — five lines rather than a second
       disclosure implementation. */
    $$('.disc-head', wrap).forEach(function (h) {
      function toggle() { h.parentElement.classList.toggle('disc-open'); }
      h.addEventListener('click', toggle);
      h.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); toggle(); }
      });
    });
  }

  /* ---------- 3  the rails ----------------------------------- */
  /* Five sections are grids of equal cards on a desktop. On a
     phone a grid of six becomes six full-width rows and the
     section stops being one thing you can take in — so each one
     becomes a rail with scroll snapping, which is the same shape
     the design system already uses for el-03 chips and the E-10
     roster.

     The rail itself is CSS. What a rail cannot say on its own is
     how far it runs, so each one gets the el-22 CarouselIndicator
     the Photos block already carries: a progress bar that tracks
     the scroll. */
  var RAILS = ['.wt-news-side', '.wt-cards', '.wt-road', '.wt-shorts', '.wt-photos'];

  function phone() { return window.matchMedia('(max-width: 767px)').matches; }

  function indicator(rail) {
    if (rail._ind) return rail._ind;
    var ind = document.createElement('div');
    ind.className = 'el-22-CarouselIndicator--prog ind wt-railind';
    ind.innerHTML = '<div class="ind-prog cut cut-s"><div class="ind-fill"></div></div>';
    rail.parentNode.insertBefore(ind, rail.nextSibling);
    rail._ind = ind;
    return ind;
  }

  function paint(rail) {
    var ind = rail._ind;
    if (!ind) return;
    var max = rail.scrollWidth - rail.clientWidth;
    var run = max > 4 ? rail.clientWidth / rail.scrollWidth : 1;
    var pos = max > 4 ? rail.scrollLeft / max : 0;
    var fill = ind.firstChild.firstChild;
    var w = Math.max(8, Math.min(100, run * 100));
    fill.style.width = w.toFixed(2) + '%';
    fill.style.marginLeft = (pos * (100 - w)).toFixed(2) + '%';
    ind.hidden = !(max > 4);
  }

  function rails() {
    RAILS.forEach(function (sel) {
      $$(sel).forEach(function (rail) {
        if (!phone()) { if (rail._ind) rail._ind.hidden = true; return; }
        indicator(rail);
        if (!rail._bound) {
          rail._bound = 1;
          rail.addEventListener('scroll', function () {
            if (rail._t) return;
            rail._t = requestAnimationFrame(function () { rail._t = 0; paint(rail); });
          }, { passive: true });
        }
        paint(rail);
      });
    });
  }

  function init() {
    buildChrome();
    buildFooterAccordion();
    rails();
    window.addEventListener('resize', rails);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
'''

out = (BODY.replace('__HEADER__', HEADER)
           .replace('__TABBAR__', TABBAR)
           .replace('__SHEET__', SHEET))
open(os.path.join(HERE, 'assets', 'mobile.js'), 'w', encoding='utf-8').write(out)
print('written', len(out))
