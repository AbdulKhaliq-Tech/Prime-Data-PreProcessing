/**
 * App bootstrap for PrimeProcessing.com.
 *
 * Phase 00 scope: check backend health on load and reflect it in the
 * shell's status region, using truthful states rather than a fake
 * "always connected" indicator.
 */
document.addEventListener('DOMContentLoaded', function () {
  var statusEl = document.getElementById('pp-backend-status');
  if (!statusEl) return;

  function setStatus(tone, icon, text) {
    statusEl.className = 'pp-status pp-status--' + tone;
    statusEl.innerHTML =
      '<span class="pp-status__icon" aria-hidden="true">' + icon + '</span>' + text;
  }

  window.PrimeProcessingApi.getHealth()
    .then(function () {
      setStatus('success', '✓', 'Backend connected');
    })
    .catch(function () {
      setStatus('warning', '!', 'Backend unreachable');
    });
});
