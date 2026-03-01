import os
import glob
import re

html_files = glob.glob('*.html')

replacement = """<script>
    document.addEventListener("DOMContentLoaded", function () {
      function sendLeadEvent(channel) {
        gtag('event', 'generate_lead', {
          lead_channel: channel
        });
      }

      document.querySelectorAll("a[href^='tel:']").forEach(function (el) {
        el.addEventListener("click", function (e) {
          sendLeadEvent('call');
        });
      });

      document.querySelectorAll("a[href*='zalo.me']").forEach(function (el) {
        el.addEventListener("click", function (e) {
          e.preventDefault();
          sendLeadEvent('zalo');
          var url = el.getAttribute('href');
          setTimeout(function () {
            window.open(url, '_blank');
          }, 250);
        });
      });

      document.querySelectorAll("a[href*='facebook.com'], a[href*='m.me']").forEach(function (el) {
        el.addEventListener("click", function (e) {
          e.preventDefault();
          sendLeadEvent('messenger');
          var url = el.getAttribute('href');
          setTimeout(function () {
            window.open(url, '_blank');
          }, 250);
        });
      });
    });
  </script>"""

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Let's use a simpler regex to catch the block.
    # We will find everything strictly from the <script> where document.addEventListener("DOMContentLoaded"... to </script> at the end of body.
    old_script_pattern = re.compile(r'<script>\s*document\.addEventListener\("DOMContentLoaded", function \(\) \{\s*function sendCTAEvent.*?\}\);\s*\}\);\s*</script>', re.DOTALL)
    
    new_content = old_script_pattern.sub(replacement, content)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file_path}")
    else:
        print(f"Failed to find match in {file_path}")
