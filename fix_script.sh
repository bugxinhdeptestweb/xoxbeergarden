#!/bin/bash
for file in *.html; do
  sed -i '' -e '/<script>/,/<\/script>/{ 
    /function sendCTAEvent(channel) {/,/});/c\
      function sendCTAEvent(channel) {\
        gtag("event", "cta_click", {\
          channel: channel,\
          page_type: document.body.dataset.page || "general"\
        });\
      }\
      document.querySelectorAll("a[href^='\''tel:'\'']").forEach(function (el) {\
        el.addEventListener("click", function () {\
          sendCTAEvent("call");\
        });\
      });\
      document.querySelectorAll("a[href*='\''zalo.me'\'']").forEach(function (el) {\
        el.addEventListener("click", function () {\
          sendCTAEvent("zalo");\
        });\
      });\
      document.querySelectorAll("a[href*='\''facebook.com'\''], a[href*='\''m.me'\'']").forEach(function (el) {\
        el.addEventListener("click", function () {\
          sendCTAEvent("messenger");\
        });\
      });
  }' "$file"
done
