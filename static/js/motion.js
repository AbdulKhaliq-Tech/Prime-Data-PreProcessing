/**
 * Reduced-motion utility.
 *
 * CSS handles most motion suppression via the `prefers-reduced-motion`
 * media query in tokens.css. This helper exists for JS-driven effects
 * later phases will add (mouse-tracking glow, radial motion on Import,
 * etc. per Master UI Guidelines) so they can check the same preference
 * before starting any animation loop.
 */
window.PrimeProcessingMotion = {
  prefersReducedMotion: function () {
    if (!window.matchMedia) return false;
    return window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  },
};
