/* ============================================================
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

  var HEADER = `<div class="f03m mnav-bar-top"><a class="f03m-mark" href="index.html" aria-label="FIBA 3x3"><svg fill="none" height="24" viewBox="0 0 80 34" width="56" xmlns="http://www.w3.org/2000/svg"><path clip-rule="evenodd" fill-rule="evenodd" fill="black" d="M25.163 0L23.2917 7.95861H26.4343L43.2322 34H53.4538L55.3256 26.0398H52.1836L35.3845 0H25.163ZM63.9565 0.0484524L62.1089 7.91191H66.1382L65.023 12.4962H59.7968L57.8626 20.8728H63.1423L61.9392 25.9927H57.8486L55.9772 33.9514H67.0969L73.5479 29.039L75.4797 20.9058L72.0453 16.7773L77.2904 12.5637L79.0909 5.01178L74.9615 0.0484524H63.9565ZM11.993 0.0484524L5.54165 4.961L3.69073 12.6324L7.12519 16.7611L1.87971 20.9736L0 28.9878L4.12933 33.951H15.1338L16.981 26.0883H12.9513L14.1494 21.0415H19.3748L21.3088 12.6651H16.0279L17.1509 8.00726H20.7301L22.6003 0.0484524H11.993ZM51.2025 0.0970993L43.0008 7.38186L48.1111 15.3066L56.3824 7.95861H59.5779L61.4245 0.0970993H51.2025ZM22.2347 26.0398H19.4861L17.6387 33.9033H27.4146L35.5767 26.596L30.4645 18.6716L22.2347 26.0398Z"></path></svg></a><a class="f03m-l" href="index.html" aria-label="World Tour home"><div class="brandlogo"><img src="assets/img/wt-logo.svg" alt="World Tour" width="90" height="18"></div></a><div class="f03m-l f03m-search f03-search" role="button" tabindex="0" aria-label="Search"><svg fill="currentColor" height="22" viewBox="0 -960 960 960" width="22" xmlns="http://www.w3.org/2000/svg"><path d="M796-121 533-384q-30 26-70 40.5T378-329q-108 0-183-75t-75-181q0-106 75-181t182-75q106 0 180.5 75T632-585q0 43-14 83t-42 75l264 262-44 44ZM377-389q81 0 138-57.5T572-585q0-81-57-138.5T377-781q-82 0-139.5 57.5T180-585q0 81 57.5 138.5T377-389Z"></path></svg></div></div>`;
  var TABBAR = `<div class="tabbar tabbar-dark mnav-bar"><a class="mnav-tab" href="index.html"><div data-tab="Home" class="ntab cut cut-s"><svg fill="currentColor" height="20" viewBox="0 -960 960 960" width="20" xmlns="http://www.w3.org/2000/svg"><path d="M141-510h137q-7-48-28-90.5T198-674q-23 35-39 76t-18 88Zm541 0h137q-2-47-18-88t-39-76q-34 34-53.5 75T682-510ZM198-287q34-34 53.5-74.5T278-450H141q2 47 18 87.5t39 75.5Zm564 0q23-35 39-75.5t18-87.5H682q7 48 26.5 88.5T762-287ZM339-510h111v-309q-62 7-115.5 32T238-720q41 41 67 95t34 115Zm171 0h111q8-61 34.5-115t67.5-95q-43-42-97-67t-116-32v309Zm-60 369v-309H339q-8 61-34 114.5T238-241q43 42 94 67.5T450-141Zm60 0q67-7 118.5-32.5T723-241q-41-41-67.5-94.5T621-450H510v309Zm-30-334Zm0 395q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 83-31.5 156T763-197q-54 54-127 85.5T480-80Z"></path></svg><div class="ntab-l">Home</div><div class="ntab-bar"></div></div></a><a class="mnav-tab" href="#"><div data-tab="Standings" class="ntab cut cut-s"><svg fill="currentColor" height="20" viewBox="0 -960 960 960" width="20" xmlns="http://www.w3.org/2000/svg"><path d="M120-120v-80h720v80H120Zm80-160v-280h120v280H200Zm200 0v-480h120v480H400Zm200 0v-360h120v360H600Z"></path></svg><div class="ntab-l">Standings</div><div class="ntab-bar"></div></div></a><a class="mnav-tab" href="#"><div data-tab="Calendar" class="ntab cut cut-s"><svg fill="currentColor" height="20" viewBox="0 -960 960 960" width="20" xmlns="http://www.w3.org/2000/svg"><path d="M180-80q-24 0-42-18t-18-42v-620q0-24 18-42t42-18h65v-60h65v60h340v-60h65v60h65q24 0 42 18t18 42v620q0 24-18 42t-42 18H180Zm0-60h600v-430H180v430Zm0-490h600v-130H180v130Zm0 0v-130 130Zm300 230q-17 0-28.5-11.5T440-440q0-17 11.5-28.5T480-480q17 0 28.5 11.5T520-440q0 17-11.5 28.5T480-400Zm-188.5-11.5Q280-423 280-440t11.5-28.5Q303-480 320-480t28.5 11.5Q360-457 360-440t-11.5 28.5Q337-400 320-400t-28.5-11.5ZM640-400q-17 0-28.5-11.5T600-440q0-17 11.5-28.5T640-480q17 0 28.5 11.5T680-440q0 17-11.5 28.5T640-400ZM480-240q-17 0-28.5-11.5T440-280q0-17 11.5-28.5T480-320q17 0 28.5 11.5T520-280q0 17-11.5 28.5T480-240Zm-188.5-11.5Q280-263 280-280t11.5-28.5Q303-320 320-320t28.5 11.5Q360-297 360-280t-11.5 28.5Q337-240 320-240t-28.5-11.5ZM640-240q-17 0-28.5-11.5T600-280q0-17 11.5-28.5T640-320q17 0 28.5 11.5T680-280q0 17-11.5 28.5T640-240Z"></path></svg><div class="ntab-l">Calendar</div><div class="ntab-bar"></div></div></a><a class="mnav-tab" href="team.html"><div data-tab="Teams" class="ntab cut cut-s"><svg fill="currentColor" height="20" viewBox="0 -960 960 960" width="20" xmlns="http://www.w3.org/2000/svg"><path d="M0-240v-53q0-38.57 41.5-62.78Q83-380 150.38-380q12.16 0 23.39.5t22.23 2.15q-8 17.35-12 35.17-4 17.81-4 37.18v65H0Zm240 0v-65q0-32 17.5-58.5T307-410q32-20 76.5-30t96.5-10q53 0 97.5 10t76.5 30q32 20 49 46.5t17 58.5v65H240Zm540 0v-65q0-19.86-3.5-37.43T765-377.27q11-1.73 22.17-2.23 11.17-.5 22.83-.5 67.5 0 108.75 23.77T960-293v53H780Zm-480-60h360v-6q0-37-50.5-60.5T480-390q-79 0-129.5 23.5T300-305v5ZM149.57-410q-28.57 0-49.07-20.56Q80-451.13 80-480q0-29 20.56-49.5Q121.13-550 150-550q29 0 49.5 20.5t20.5 49.93q0 28.57-20.5 49.07T149.57-410Zm660 0q-28.57 0-49.07-20.56Q740-451.13 740-480q0-29 20.56-49.5Q781.13-550 810-550q29 0 49.5 20.5t20.5 49.93q0 28.57-20.5 49.07T809.57-410ZM480-480q-50 0-85-35t-35-85q0-51 35-85.5t85-34.5q51 0 85.5 34.5T600-600q0 50-34.5 85T480-480Zm.35-60Q506-540 523-557.35t17-43Q540-626 522.85-643t-42.5-17q-25.35 0-42.85 17.15t-17.5 42.5q0 25.35 17.35 42.85t43 17.5ZM480-300Zm0-300Z"></path></svg><div class="ntab-l">Teams</div><div class="ntab-bar"></div></div></a><div class="mnav-tab mnav-more" role="button" tabindex="0"><div data-tab="More" class="ntab cut cut-s"><svg fill="currentColor" height="20" viewBox="0 -960 960 960" width="20" xmlns="http://www.w3.org/2000/svg"><path d="M240-400q-33 0-56.5-23.5T160-480q0-33 23.5-56.5T240-560q33 0 56.5 23.5T320-480q0 33-23.5 56.5T240-400Zm240 0q-33 0-56.5-23.5T400-480q0-33 23.5-56.5T480-560q33 0 56.5 23.5T560-480q0 33-23.5 56.5T480-400Zm240 0q-33 0-56.5-23.5T640-480q0-33 23.5-56.5T720-560q33 0 56.5 23.5T800-480q0 33-23.5 56.5T720-400Z"></path></svg><div class="ntab-l">More</div><div class="ntab-bar"></div></div></div></div>`;
  var SHEET  = `<div class="f03m-sheet mnav-sheet" hidden=""> <div class="f03m-sheet-top" style="justify-content:flex-end"> <div class="f03m-close mnav-close" role="button" tabindex="0" style="display:flex;align-items:center;gap:6px;color:var(--chrome-text-muted)"> <span class="t-caption" style="color:inherit">Close</span> <svg fill="currentColor" height="20" viewBox="0 -960 960 960" width="20"><path d="m251-160-91-91 229-229-229-229 91-91 229 229 229-229 91 91-229 229 229 229-91 91-229-229-229 229Z"></path></svg> </div> </div> <div class="f03m-sheet-body"> <div class="f03m-grp"> <div class="f03m-grp-h">World Tour</div> <a class="f03m-l" href="team.html">Teams</a> <div class="f03m-l" tabindex="0">Standings</div> <div class="f03m-l" tabindex="0">Stats</div> <div class="f03m-l" tabindex="0">News</div> <div class="f03m-l" tabindex="0">Photos</div> <div class="f03m-l" tabindex="0">Videos</div> <div class="f03m-l" tabindex="0">Calendar</div> </div> <div class="f03m-grp"> <div class="f03m-grp-h">Info</div> <div class="f03m-l" tabindex="0">About the World Tour</div> <div class="f03m-l" tabindex="0">How to qualify</div> <div class="f03m-l" tabindex="0">FAQ</div> </div> </div> </div>`;

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
      var want = (phone && full.length > LIMIT) ? full.slice(0, LIMIT).replace(/\s+$/, '') + '\u2026' : full;
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
