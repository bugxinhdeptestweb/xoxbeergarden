  <script>
    document.addEventListener("DOMContentLoaded", function () {
      function sendCTAEvent(channel, url, target) {
        gtag('event', 'cta_click', {
          channel: channel,
          page_type: document.body.dataset.page || 'general',
          event_callback: function() {
            if (url && target !== '_blank') {
              window.location.href = url;
            }
          }
        });
        if (url && target !== '_blank') {
          // Fallback if gtag fails to load or blocks too long
          setTimeout(function() {
            window.location.href = url;
          }, 300);
        }
      }
      
      document.querySelectorAll("a[href^='tel:']").forEach(function (el) {
        el.addEventListener("click", function (e) {
          sendCTAEvent('call', el.getAttribute('href'), el.getAttribute('target'));
        });
      });
      document.querySelectorAll("a[href*='zalo.me']").forEach(function (el) {
        el.addEventListener("click", function (e) {
          sendCTAEvent('zalo', el.getAttribute('href'), el.getAttribute('target'));
        });
      });
      document.querySelectorAll("a[href*='facebook.com'], a[href*='m.me']").forEach(function (el) {
        el.addEventListener("click", function (e) {
          sendCTAEvent('messenger', el.getAttribute('href'), el.getAttribute('target'));
        });
      });
    });
  </script>
