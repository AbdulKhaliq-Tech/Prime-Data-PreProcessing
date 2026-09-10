/**
 * Theme switching for PrimeProcessing.com's four approved themes.
 *
 * The initial theme is already applied by an inline script in base.html
 * (to avoid a flash of the wrong theme before CSS loads). This file wires
 * up the select control so the user can change themes after page load,
 * and persists the choice for next time.
 */
(function () {
  var STORAGE_KEY = 'primeprocessing:theme';

  function applyTheme(themeId) {
    document.documentElement.setAttribute('data-theme', themeId);
    try {
      window.localStorage.setItem(STORAGE_KEY, themeId);
    } catch (e) {
      // Storage may be unavailable (private browsing, etc). Theme still
      // applies for this page load.
    }
  }

  document.addEventListener('DOMContentLoaded', function () {
    var select = document.getElementById('pp-theme-select');
    if (!select) return;

    var current = document.documentElement.getAttribute('data-theme') || 'arctic-blue';
    select.value = current;

    select.addEventListener('change', function (event) {
      applyTheme(event.target.value);
    });
  });
})();
