---
layout: null
title: "Menu | XOX Beer Garden"
permalink: /menu
---

<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{{ page.title }}</title>
  <meta name="description" content="Menu & Gallery XOX Beer Garden – nền đen/cam, slider kéo ngang, khung A4 dọc liền mạch." />
  <link rel="canonical" href="{{ '/menu' | relative_url }}" />
  <style>
    :root{
      --bg:#0b0f14;
      --card:#10161c;
      --ink:#e9eef2;
      --muted:#93a1ad;
      --accent:#ff7a1a;
      --bd:#1c2730;
    }
    html,body{margin:0}
    body.menu-page{background:var(--bg);color:var(--ink);font-family:Inter,system-ui,Roboto,Arial,sans-serif}
    a{color:var(--accent);text-decoration:none}
    .wrap{max-width:1200px;margin:0 auto;padding:18px 16px}
    header{border-bottom:1px solid var(--bd);background:linear-gradient(180deg,rgba(255,122,26,.06),rgba(255,122,26,0))}
    .brand{display:flex;justify-content:space-between;align-items:center;gap:12px}
    .brand h1{font-size:24px;margin:0}
    .brand .nav a{margin-left:14px;color:var(--ink);opacity:.85}
    .brand .nav a:hover{opacity:1;color:var(--accent)}
    h2.section{font-size:22px;margin:18px 0 8px;display:flex;align-items:center;gap:10px}
    h2.section::before{content:'';width:6px;height:24px;background:var(--accent);border-radius:3px}
    p.hint{color:var(--muted);margin:0 0 12px}
    /* Scroller */
    .scroller{position:relative}
    .rail{display:flex;gap:14px;overflow-x:auto;scroll-snap-type:x mandatory;padding:10px 6px;-webkit-overflow-scrolling:touch;background:transparent}
    .rail::-webkit-scrollbar{height:8px}
    .rail::-webkit-scrollbar-thumb{background:linear-gradient(90deg,var(--bd),#202d37);border-radius:8px}
    .tile{flex:0 0 85vw;scroll-snap-align:center;background:var(--card);border:1px solid var(--bd);border-radius:12px;overflow:hidden;box-shadow:0 8px 30px rgba(0,0,0,.25)}
    @media(min-width:720px){ .tile{ flex:0 0 460px } }
    @media(min-width:1080px){ .tile{ flex:0 0 520px } }
    .tile img.cover{display:block;width:100%;height:340px;object-fit:cover}
    .tile-a4{flex:0 0 85vw;scroll-snap-align:center;background:var(--card);border:1px solid var(--bd);border-radius:12px;overflow:hidden;box-shadow:0 8px 30px rgba(0,0,0,.25);display:flex;align-items:center;justify-content:center}
    @media(min-width:720px){ .tile-a4{ flex:0 0 460px } }
    @media(min-width:1080px){ .tile-a4{ flex:0 0 520px } }
    .frame-a4{width:100%;aspect-ratio:210/297;background:#0b0f14;display:flex;align-items:center;justify-content:center}
    .frame-a4 img.contain{max-width:100%;max-height:100%;object-fit:contain;display:block;background:#0b0f14}
    .ctrl{position:absolute;top:42%;transform:translateY(-50%);display:flex;align-items:center;justify-content:center;width:42px;height:42px;border-radius:50%;background:rgba(16,22,28,.7);border:1px solid var(--bd);backdrop-filter:blur(4px);cursor:pointer}
    .ctrl:hover{background:rgba(16,22,28,.9)}
    .ctrl svg{width:20px;height:20px;fill:var(--ink)}
    .prev{left:-6px} .next{right:-6px}
    .mid{background:linear-gradient(180deg,rgba(255,122,26,.08),rgba(255,122,26,0));border:1px solid var(--bd);border-radius:16px;padding:18px}
    .mid h3{margin:0 0 6px;color:var(--accent)}
    .mid p{margin:6px 0;color:var(--ink)}
    footer{border-top:1px solid var(--bd);color:var(--muted);text-align:center;padding:16px 0;margin-top:28px}
  </style>
</head>
<body class="menu-page">
  <header>
    <div class="wrap brand">
      <h1>XOX Beer Garden</h1>
      <nav class="nav">
        <a href="/">Trang chủ</a>
        <strong style="color:var(--accent)">Menu</strong>
        <a href="/gallery">Ảnh món</a>
      </nav>
    </div>
  </header>

  <main class="wrap">
    <h2 class="section">Ảnh món ăn nổi bật</h2>
    <p class="hint">Kéo ngang để xem thêm.</p>
    {% assign foods = site.static_files | where_exp:'f','f.path contains "/assets/food/"' | sort:'path' %}
    <section class="scroller">
      <div class="rail" id="foodRail">
        {% for f in foods %}
        <figure class="tile">
          <img class="cover" src="{{ f.path | relative_url }}" alt="Món {{ forloop.index }}" loading="lazy">
        </figure>
        {% endfor %}
      </div>
    </section>

    <section class="mid" style="margin:24px 0">
      <h3>Không gian & Ưu đãi</h3>
      <p>Không gian tối ấm, đèn vàng – phù hợp gia đình & nhóm bạn. Đặt tiệc sinh nhật/họp lớp (20–120 khách) – <strong>giảm 5%</strong> khi đặt trước.</p>
      <p>Địa chỉ: E16 Lô E, KDC Bàu Xéo, TT Trảng Bom • Hotline: <a href="tel:0975229739">0975 229 739</a></p>
    </section>

    <h2 class="section">Menu của quán (A4 dọc)</h2>
    <p class="hint">Kéo ngang để xem từng trang menu.</p>
    {% assign menus = site.static_files | where_exp:'f','f.path contains "/assets/menu/"' | sort:'path' %}
    <section class="scroller">
      <div class="rail" id="menuRail">
        {% for f in menus %}
        <figure class="tile-a4">
          <div class="frame-a4">
            <img class="contain" src="{{ f.path | relative_url }}" alt="Menu trang {{ forloop.index }}" loading="lazy">
          </div>
        </figure>
        {% endfor %}
      </div>
    </section>
  </main>

  <footer>© {{ 'now' | date: '%Y' }} XOX Beer Garden • Nền đen/cam đồng bộ thương hiệu</footer>

  <script>
    function enableDragScroll(rail){
      if(!rail) return;
      let isDown=false,startX,scrollLeft;
      rail.addEventListener('mousedown', e=>{isDown=true;startX=e.pageX;scrollLeft=rail.scrollLeft;rail.style.cursor='grabbing'});
      ['mouseleave','mouseup'].forEach(ev=> rail.addEventListener(ev, ()=>{isDown=false;rail.style.cursor=''}));
      rail.addEventListener('mousemove', e=>{
        if(!isDown) return;
        e.preventDefault();
        const walk=(e.pageX-startX)*1.2;
        rail.scrollLeft=scrollLeft-walk;
      });
    }
    enableDragScroll(document.getElementById('foodRail'));
    enableDragScroll(document.getElementById('menuRail'));
  </script>
</body>
</html>
