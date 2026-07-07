(function () {
  window.NJGROUP_TRACKING_CONFIG = window.NJGROUP_TRACKING_CONFIG || {
    googleAdsId: "",
    enabled: true
  };

  function track(eventName, payload) {
    if (!window.NJGROUP_TRACKING_CONFIG.enabled) return;
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push({
      event: eventName,
      page: window.location.pathname,
      payload: payload || {}
    });
  }

  document.addEventListener("click", function (event) {
    const target = event.target.closest("[data-track], a[href^='tel:'], a[href^='mailto:']");
    if (!target) return;
    if (target.matches("a[href^='tel:']")) track("phone_click", { href: target.href });
    if (target.matches("a[href^='mailto:']")) track("email_click", { href: target.href });
    if (target.dataset.track) track(target.dataset.track, { href: target.href || "", label: target.textContent.trim() });
  });

  document.addEventListener("submit", function (event) {
    const form = event.target.closest("form[data-track-form]");
    if (!form) return;
    track("form_submit", { form: form.dataset.trackForm });
    const submittedAt = form.querySelector("input[name='submitted_at']");
    if (submittedAt) submittedAt.value = new Date().toISOString();
  });

  window.NJGROUPTrack = track;
})();
