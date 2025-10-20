---
layout: null
title: "Menu | XOX Beer Garden"
permalink: /menu
---

<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{ page.title }}</title>
<meta name="description" content="Menu XOX Beer Garden — nền đen/cam, kéo ngang, A4 dọc, thứ tự 1→13 theo _data/menu.yml.">
<style>
  :root{ --bg:#0b0f14; --card:#10161c; --ink:#e9eef2; --muted:#93a1ad; --accent:#ff7a1a; --bd:#1c2730; }
  html,body{margin:0}
  body{background:var(--bg);color:var(--ink);font-family:Inter,system-ui,Roboto,Arial,sans-serif}
  .wrap{max-width:1200px;margin:0 auto;padding:18px 16px}
  header{border-bottom:1px solid var(--bd)}
  h1{font-size:24px;margin:0}
  h2.section{font-size:22px;margin:18px 0 8px;display:flex;gap:10px;align-items:center}
  h2.section::before{content:"";width:6px;height:24px;background:var(--accent);border-radius:3px}
  p.hint{color:var(--muted);margin:0 0 12px}
  /* scroller */
  .scroller{position:relative}
  .rail{display:flex;gap:14px;overflow-x:auto;scroll-snap-type:x mandatory;padding:10px 6px;-webkit-overflow-scrolling:touch}
  .rail::-webkit-scrollbar{height:8px}
  .rail::-webkit-scrollbar-thumb{background:linear-gradient(90deg,var(--bd),#202d37);border-radius:8px}
  /* A4 tile */
  .tile-a4{flex:0 0 85vw;scroll-snap-align:center;background:var(--card);border:1px solid var(--bd);border-radius:12px;overflow:hidden;box-shadow:0 8px 30px rgba(0,0,0,.25);display:flex;align-items:center;justify-content:center}
  @media(min-width:720px){ .tile-a4{ flex:0 0 460px } }
  @media(min-width:1080px){ .tile-a4{ flex:0 0 520px } }
  .frame-a4{width:100%;aspect-ratio:210/297;background:#0b0f14;display:flex;align-items:center;justify-content:center}
  .frame-a4 img{max-width:100%;max-height:100%;object-fit:contain;display:block;background:#0b0f14}
</style>
</head>
<body>
  <header>
    <div class="wrap">
      <h1>Menu XOX Beer Garden</h1>
    </div>
  </header>

  <main class="wrap">
    <h2 class="section">Menu của quán (A4 dọc)</h2>
    <p class="hint">Kéo ngang để xem từng trang. Thứ tự theo _data/menu.yml.</p>

    <section class="scroller">
      <div class="rail" id="menuRail">
        {% if site.data.menu and site.data.menu.menus %}
          {% for p in site.data.menu.menus %}
          <figure class="tile-a4">
            <div class="frame-a4">
              <img src="{{ p | relative_url }}" alt="Menu trang {{ forloop.index }}" loading="lazy">
            </div>
          </figure>
          {% endfor %}
        {% else %}
          <p>Chưa có danh sách menus trong <code>_data/menu.yml</code>.</p>
        {% endif %}
      </div>
    </section>
  </main>

  <script>
    // kéo-để-cuộn mượt
    (function(){
      const rail = document.getElementById('menuRail');
      if(!rail) return;
      let isDown=false,startX=0,scrollLeft=0;
      rail.addEventListener('mousedown', e=>{isDown=true;startX=e.pageX;scrollLeft=rail.scrollLeft;rail.style.cursor='grabbing'});
      ['mouseleave','mouseup'].forEach(ev=> rail.addEventListener(ev, ()=>{isDown=false;rail.style.cursor=''}));
      rail.addEventListener('mousemove', e=>{
        if(!isDown) return;
        e.preventDefault();
        const walk=(e.pageX-startX)*1.2;
        rail.scrollLeft=scrollLeft-walk;
      });
    })();
  </script>
</body>
</html>
