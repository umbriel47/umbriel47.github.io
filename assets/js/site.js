// Colour-scheme toggle. The initial value is applied inline in <head> to avoid
// a flash; this only handles clicks and persistence.
(function () {
  var root = document.documentElement;

  function stored() {
    try { return localStorage.getItem('theme'); } catch (e) { return null; }
  }

  function systemDark() {
    return window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
  }

  function current() {
    return root.dataset.theme || (systemDark() ? 'dark' : 'light');
  }

  document.querySelectorAll('[data-theme-toggle]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var next = current() === 'dark' ? 'light' : 'dark';
      root.dataset.theme = next;
      try { localStorage.setItem('theme', next); } catch (e) {}
    });
  });

  // Close the mobile nav after following a link within the same page.
  var navToggle = document.getElementById('nav-toggle');
  if (navToggle) {
    document.querySelectorAll('.site-nav a').forEach(function (a) {
      a.addEventListener('click', function () { navToggle.checked = false; });
    });
  }

  // Remember the language only when the visitor explicitly switches, so that
  // merely reading one Chinese page does not change what "/" lands on.
  document.querySelectorAll('.lang-switch').forEach(function (a) {
    a.addEventListener('click', function () {
      var to = a.getAttribute('hreflang') === 'en' ? 'en' : 'zh';
      try { localStorage.setItem('lang', to); } catch (e) {}
    });
  });

  // Custom analytics events. Arts and Music are single pages, so a page view
  // cannot attribute interest to one artwork or one track; an explicit
  // interaction can. Fires only if an analytics provider actually loaded —
  // when the script is blocked, these are silent no-ops.
  function track(el) {
    var a = window.__analytics;
    if (!a || !a.event) return;
    var name = el.getAttribute('data-track');
    if (!name) return;
    try { a.event(name, el.getAttribute('data-track-title')); } catch (e) {}
  }

  document.querySelectorAll('a[data-track]').forEach(function (el) {
    el.addEventListener('click', function () { track(el); });
  });

  document.querySelectorAll('audio[data-track]').forEach(function (el) {
    // `play` fires on every resume; count the track once per page view.
    var counted = false;
    el.addEventListener('play', function () {
      if (counted) return;
      counted = true;
      track(el);
    });
  });

  // Article view count: sum GoatCounter's public counter over every path the
  // layout lists (an article and its translation). Any failure — blocked,
  // unreachable, slow — leaves the count hidden rather than showing a wrong 0.
  document.querySelectorAll('[data-views]').forEach(function (el) {
    var base = el.getAttribute('data-views');
    var paths = (el.getAttribute('data-views-paths') || '').split(' ').filter(Boolean);
    if (!base || !paths.length || !window.fetch) return;
    var ctrl = window.AbortController ? new AbortController() : null;
    if (ctrl) setTimeout(function () { ctrl.abort(); }, 6000);
    Promise.all(paths.map(function (p) {
      return fetch(base + '/counter/' + encodeURIComponent(p) + '.json',
                   ctrl ? { signal: ctrl.signal } : {})
        .then(function (r) {
          // 404 just means the path has no visits yet.
          if (r.status === 404) return 0;
          if (!r.ok) throw new Error(r.status);
          // Counts arrive as strings formatted with the account's thousands
          // separator ("1,234" or "1 234"); keep the digits only.
          return r.json().then(function (j) { return parseInt(String(j.count).replace(/\D/g, ''), 10) || 0; });
        });
    })).then(function (counts) {
      var total = counts.reduce(function (a, b) { return a + b; }, 0);
      if (!total) return;
      el.querySelector('[data-views-n]').textContent =
        total.toLocaleString(document.documentElement.lang || undefined);
      if (total === 1) {
        var label = el.querySelector('[data-views-label]');
        label.textContent = label.getAttribute('data-one');
      }
      el.hidden = false;
    }).catch(function () {});
  });

  void stored;
})();
