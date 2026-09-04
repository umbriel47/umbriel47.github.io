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

  void stored;
})();
