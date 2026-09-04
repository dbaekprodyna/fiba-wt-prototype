/* ============================================================
   FIBA 3x3 World Tour 2026 — wt.js
     1  scroll reveal (.reveal / .is-in, motion.css)
     2  the hero parallax, clamped to the band's mask
     3  S-14 StopBar: centre the live stop, arrow paging
     4  el-07 AccordionShell open / close
     5  rows and cards that behave as links
   ============================================================ */
(function () {
  'use strict';
  var D = document;
  function qsa(r, s) { return Array.prototype.slice.call(r.querySelectorAll(s)); }

  /* ---------- 1  scroll reveal ------------------------------- */
  var io = null;
  if ('IntersectionObserver' in window) {
    io = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.01 });
  }
  function scan() {
    qsa(D, '.reveal:not(.is-in)').forEach(function (n) {
      if (io) io.observe(n); else n.classList.add('is-in');
    });
    sweep();
  }
  /* An element that gains its layout while already behind the reader
     never changes its intersection ratio, so the observer is never
     called for it. This is what catches those. */
  function sweep() {
    var vh = window.innerHeight || 0;
    qsa(D, '.reveal:not(.is-in)').forEach(function (n) {
      var r = n.getBoundingClientRect();
      if (r.width + r.height === 0) return;
      if (r.top < vh) n.classList.add('is-in');
    });
  }

  /* ---------- 2  hero parallax -------------------------------
     [node, rate, mode]. A layer given +0.3 travels down at three
     tenths of the page's speed, so it reads as further away.

     THE CLAMP. The photograph is twice the band's height and sits
     centred, so it has exactly half a band of slack above and
     below. Its travel is clamped to that slack — at the bottom of
     its run the plate still covers the band edge to edge, and the
     red ground behind it is never uncovered. The corner elements
     are drawn INTO their own edges, so the left one holds still:
     at any other rate a strip of flat red opens between the band's
     corner and the artwork's.                                    */
  var pq = window.matchMedia('(min-width: 901px)');
  var par = null, ticking = false;

  function build() {
    var band = D.querySelector('.hwt');
    if (!band) return null;
    var q = function (s) { return band.querySelector(s); };
    var slack = band.offsetHeight / 2;         /* the mask's headroom */
    var L = [];
    [[q('.hwt-kv-l'), 0.00, 0, 1e9],
     [q('.hwt-kv-r'), 0.20, 0, 1e9],
     [q('.hwt-bg'), 0.45, 0, slack],
     [q('.hwt-in'), -0.16, 2, 1e9]]
      .forEach(function (e) { if (e[0]) { e[0].classList.add('hwt-par'); L.push(e); } });
    return L.length ? { band: band, layers: L, h: band.offsetHeight || 1, slack: slack } : null;
  }
  function frame() {
    ticking = false;
    if (!par) return;
    var s = window.pageYOffset || D.documentElement.scrollTop || 0;
    var p = Math.min(s, par.h * 1.6);
    par.layers.forEach(function (e) {
      var yv = p * e[1];
      var cap = e[3];
      if (yv > cap) yv = cap; else if (yv < -cap) yv = -cap;
      /* At rest the inline transform comes off altogether — an
         unscrolled band has to be the band it always was. */
      e[0].style.transform = Math.abs(yv) < 0.05 ? '' : 'translate3d(0,' + yv.toFixed(1) + 'px,0)';
      if (e[2] === 2) {
        var t = (p / par.h - 0.34) / 0.66;
        var o = 1 - Math.min(1, Math.max(0, t));
        e[0].style.opacity = o > 0.999 ? '' : o.toFixed(3);
      }
    });
  }
  function onScroll() { if (!ticking && par) { ticking = true; requestAnimationFrame(frame); } }
  function sync() {
    if (pq.matches) {
      if (!par) par = build();
      if (par) { par.h = par.band.offsetHeight || 1; par.slack = par.h / 2;
                 par.layers.forEach(function (e) { if (e[3] !== 1e9) e[3] = par.slack; });
                 frame(); }
    } else if (par) {
      par.layers.forEach(function (e) { e[0].style.transform = ''; e[0].style.opacity = ''; e[0].classList.remove('hwt-par'); });
      par = null;
    }
  }

  /* ---------- 3  S-14 StopBar -------------------------------- */
  function stopbar() {
    qsa(D, '.s14').forEach(function (bar) {
      var sc = bar.querySelector('.s14-scroll');
      var live = sc && sc.querySelector('.s14-on');
      if (sc && live) {
        sc.scrollLeft = Math.max(0, live.offsetLeft - (sc.clientWidth - live.offsetWidth) / 2);
      }
      qsa(bar, '.s14-nav').forEach(function (b) {
        b.addEventListener('click', function () {
          if (!sc) return;
          sc.scrollBy({ left: (b.dataset.dir === 'next' ? 1 : -1) * Math.round(sc.clientWidth * 0.7), behavior: 'smooth' });
        });
      });
    });
  }

  /* ---------- 4  el-07 AccordionShell ------------------------ */
  function accordions() {
    qsa(D, '.acc-head').forEach(function (h) {
      h.addEventListener('click', function () {
        var a = h.closest('.acc');
        if (!a) return;
        var open = a.dataset.open !== 'false';
        a.dataset.open = open ? 'false' : 'true';
        h.setAttribute('aria-expanded', String(!open));
      });
      h.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); h.click(); }
      });
    });
  }

  /* ---------- 5  S-13 Countdown — the figures run ------------
     One interval for every countdown on the page, ticking on the
     second. A figure that has not changed is left alone: re-running
     the bounce on all four every second would be a slot machine,
     not a clock. Only the figure that changed drops in.          */
  function countdowns() {
    var cds = qsa(D, '.s13[data-until]').map(function (n) {
      var t = Date.parse(n.dataset.until);
      if (isNaN(t)) return null;
      return { t: t, u: {}, last: {} };
    }).filter(Boolean);
    if (!cds.length) return;
    qsa(D, '.s13[data-until]').forEach(function (n, i) {
      if (!cds[i]) return;
      qsa(n, '.s13-v[data-u]').forEach(function (v) { cds[i].u[v.dataset.u] = v; });
    });
    function pad(v, w) { v = String(v); while (v.length < w) v = '0' + v; return v; }
    function tick() {
      var now = Date.now();
      cds.forEach(function (c) {
        var ms = Math.max(0, c.t - now);
        var s = Math.floor(ms / 1000);
        var val = { d: Math.floor(s / 86400), h: Math.floor(s / 3600) % 24,
                    m: Math.floor(s / 60) % 60, s: s % 60 };
        Object.keys(c.u).forEach(function (k) {
          var txt = k === 'd' ? String(val.d) : pad(val[k], 2);
          if (c.last[k] === txt) return;
          c.last[k] = txt;
          var el = c.u[k];
          el.textContent = txt;
          el.classList.remove('is-tick');
          /* reading offsetWidth restarts the animation; without it the
             class goes back on inside the same frame and nothing runs */
          void el.offsetWidth;
          el.classList.add('is-tick');
        });
      });
    }
    tick();
    setInterval(tick, 1000);
  }

  /* ---------- 6  rows and cards that are links ---------------- */
  function rowlinks() {
    qsa(D, '[data-href]').forEach(function (n) {
      n.addEventListener('click', function (e) {
        if (e.target.closest('a')) return;
        window.location.href = n.dataset.href;
      });
      n.addEventListener('keydown', function (e) {
        if (e.key === 'Enter') window.location.href = n.dataset.href;
      });
    });
  }

  function boot() {
    scan(); sync(); stopbar(); accordions(); countdowns(); rowlinks();
    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', function () { sync(); sweep(); });
    if (pq.addEventListener) pq.addEventListener('change', sync);
    /* A pane behind a tab has no box, so nothing ever comes back for
       it. A press is the only thing that opens one; a press sends
       the sweep round again. */
    D.addEventListener('click', function () { setTimeout(sweep, 80); }, true);
    D.body.setAttribute('data-rendered', '1');
  }
  if (D.readyState === 'loading') D.addEventListener('DOMContentLoaded', boot); else boot();
})();
