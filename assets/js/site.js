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

  void stored;
})();
