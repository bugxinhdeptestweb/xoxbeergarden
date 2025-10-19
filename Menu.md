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
  <meta name="description" content="Menu & Gallery XOX Beer Garden – slider kéo ngang, nền đen/cam. Trên: ảnh món ăn. Giữa: mô tả. Dưới: menu A4 dọc." />
  <link rel="canonical" href="{{ '/menu' | relative_url }}" />
  <meta property="og:title" content="Menu | XOX Beer Garden" />
  <meta property="og:description" content="Ảnh món ăn & menu dạng A4 dọc, kéo ngang mượt, giao diện tối cam." />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="{{ '/menu' | absolute_url }}" />
  <meta property="og:image" content="{{ '/assets/images/og-menu.jpg' | relative_url }}" />
  <style>
    /* ====== THEME (đen/cam) ====== */
    :root{
      --bg:#0b0f14;        /* nền toàn trang */
      --card:#10161c;      /* khối tối */
      --ink:#e9eef2;       /* chữ sáng */
      --muted:#93a1ad;     /* chữ mờ */
      --accent:#ff7a1a;    /* cam thương hiệu */
      --bd:#1c2730;        /* viền */
    }
    html,body{margin:0}
    body.menu-page{background:var(--bg) !important;color:var(--ink) !important;font-family:Inter,system-ui,Roboto,Arial,sans-serif}
    a{color:var(--accent);text-decoration:none}
    .wrap{max-width:1200px;margin:0 auto;padding:18px 16px}

    header{position:sticky;top:0;z-index:5;border-bottom:1px solid var(--bd);background:linear-gradient(180deg,rgba(255,122,26,.06),rgba(255,122,26,0))}
    .brand{display:flex;justify-content:space-between;align-items:center;gap:12px}
    .brand h1{font-size:24px;margin:0}
    .brand .nav a{margin-left:14px;color:var(--ink);opacity:.85}
    .brand .nav a:hover{opacity:1;color:var(--accent)}

    h2.section{font-size:22px;margin:18px 0 8px;display:flex;align-items:center;gap:10px}
    h2.section::before{content:'';width:6px;height:24px;background:var(--accent);border-radius:3px}
    p.hint{color:var(--muted);margin:0 0 12px}

    /* ====== SCROLLER (kéo ngang) – bản ổn định ====== */
    .scroller{position:relative}
    .rail{display:flex;gap:14px;overflow-x:auto;scroll-snap-type:x mandatory;padding:10px 6px;-webkit-overflow-scrolling:touch;background:transparent}
    .rail::-webkit-scrollbar{height:10px}
    .rail::-webkit-scrollbar-thumb{background:linear-gradient(90deg,var(--bd),#202d37);border-radius:8px}

    /* Ô hiển thị ảnh món (tự do tỉ lệ, cover) */
    .tile{flex:0 0 85vw;scroll-snap-align:center;background:var(--card);border:1px solid var(--bd);border-radius:16px;overflow:hidden;box-shadow:0 8px 30px rgba(0,0,0,.25)}
    @media(min-width:720px){ .tile{ flex:0 0 460px } }
    @media(min-width:1080px){ .tile{ flex:0 0 520px } }
    .tile img.cover{display:block;width:100%;height:340px;object-fit:cover}
    .cap{display:flex;justify-content:space-between;align-items:center;padding:10px 12px;color:var(--muted);font-size:14px;border-top:1px solid var(--bd)}

    /* ====== FRAME A4 dọc cho menu ====== */
    .tile-a4{flex:0 0 85vw;scroll-snap-align:center;background:var(--card);border:1px solid var(--bd);border-radius:16px;overflow:hidden;box-shadow:0 8px 30px rgba(0,0,0,.25);display:flex;align-items:center;justify-content:center}
    @media(min-width:720px){ .tile-a4{ flex:0 0 460px } }
    @media(min-width:1080px){ .tile-a4{ flex:0 0 520px } }
    .frame-a4{position:relative;width:100%;aspect-ratio:210/297; background:#0b0f14; display:flex;align-items:center;justify-content:center}
    .frame-a4 img.contain{max-width:100%;max-height:100%;object-fit:contain;display:block;background:#0b0f14}

    .ctrl{position:absolute;top:42%;transform:translateY(-50%);display:flex;align-items:center;justify-content:center;width:42px;height:42px;border-radius:50%;background:rgba(16,22,28,.7);border:1px solid var(--bd);backdrop-filter:blur(4px);cursor:pointer}
    .ctrl:hover{background:rgba(16,22,28,.9)}
    .ctrl svg{width:20px;height:20px;fill:var(--ink)}
    .prev{left:-6px} .next{right:-6px}

    .mid{background:linear-gradient(180deg,rgba(255,122,26,.08),rgba(255,122,26,0));border:1px solid var(--bd);border-radius:16px;padding:18px}
    .mid h3{margin:0 0 6px;color:var(--accent)}
    .mid p{margin:6px 0;color:var(--ink)}

    footer{border-top:1px solid var(--bd);color:var(--muted)}
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
    <!-- ====== TOP: FOOD PHOTOS (kéo ngang) ====== -->
    <h2 class="section">Ảnh món ăn nổi bật</h2>
    <p class="hint">Kéo ngang để xem thêm. Bấm ảnh để tải.</p>

    {% assign foods = site.static_files | where_exp:'f','f.path contains "/assets/food/"' | sort:'path' %}
    <section class="scroller" id="foodScroller">
      <button class="ctrl prev" aria-label="Trước" data-for="foodRail"> 
        <svg viewBox="0 0 24 24"><path d="M15.41 7.41 14 6l-6 6 6 6 1.41-1.41L10.83 12z"/></svg>
      </button>
      <div class="rail" id="foodRail">
        {% for f in foods %}
        <figure class="tile">
          <img class="cover" src="{{ f.path | relative_url }}" alt="Món {{ forloop.index }}" loading="lazy" onclick="downloadImg('{{ f.path | relative_url }}')">
          <figcaption class="cap">
            <span>Món {{ forloop.index }}</span>
            <a href="{{ f.path | relative_url }}" download>Tải ảnh</a>
          </figcaption>
        </figure>
        {% endfor %}
      </div>
      <button class="ctrl next" aria-label="Sau" data-for="foodRail">
        <svg viewBox="0 0 24 24"><path d="M8.59 16.59 10 18l6-6-6-6-1.41 1.41L13.17 12z"/></svg>
      </button>
    </section>

    <!-- ====== MIDDLE TEXT ====== -->
    <section class="mid" style="margin:18px 0">
      <h3>Không gian & Ưu đãi</h3>
      <p>Không gian tối ấm, đèn vàng – phù hợp gia đình & nhóm bạn. Đặt tiệc sinh nhật/ họp lớp (20–120 khách) – <strong>giảm 5%</strong> khi đặt trước.</p>
      <p>Địa chỉ: E16 Lô E, KDC Bàu Xéo, TT Trảng Bom • Hotline: <a href="tel:0975229739">0975 229 739</a></p>
    </section>

    <!-- ====== BOTTOM: MENU A4 dọc (kéo ngang) ====== -->
    <h2 class="section">Menu của quán (A4 dọc)</h2>
    <p class="hint">Kéo ngang để xem từng trang. Khung A4 dọc giúp thấy trọn trang.</p>

    {% assign menus = site.static_files | where_exp:'f','f.path contains "/assets/menu/"' | sort:'path' %}
    <section class="scroller" id="menuScroller">
      <button class="ctrl prev" aria-label="Trước" data-for="menuRail"> 
        <svg viewBox="0 0 24 24"><path d="M15.41 7.41 14 6l-6 6 6 6 1.41-1.41L10.83 12z"/></svg>
      </button>
      <div class="rail" id="menuRail">
        {% for f in menus %}
        <figure class="tile-a4">
          <div class="frame-a4">
            <img class="contain" src="{{ f.path | relative_url }}" alt="Menu trang {{ forloop.index }}" loading="lazy" onclick="downloadImg('{{ f.path | relative_url }}')">
          </div>
          <figcaption class="cap">
            <span>Trang {{ forloop.index }}</span>
            <a href="{{ f.path | relative_url }}" download>Tải trang</a>
          </figcaption>
        </figure>
        {% endfor %}
      </div>
      <button class="ctrl next" aria-label="Sau" data-for="menuRail">
        <svg viewBox="0 0 24 24"><path d="M8.59 16.59 10 18l6-6-6-6-1.41 1.41L13.17 12z"/></svg>
      </button>
    </section>
  </main>

  <footer class="wrap" style="margin-top:22px">© {{ 'now' | date: '%Y' }} XOX Beer Garden • Nền đen/cam đồng bộ thương hiệu</footer>

  <script>
    // Cuộn mượt theo kích thước khung
    function getRail(id){ return document.getElementById(id); }
    function scrollById(railId, amount){ const el = getRail(railId); el?.scrollBy({left:amount, behavior:'smooth'}); }

    document.querySelectorAll('.ctrl').forEach(btn=>{
      btn.addEventListener('click', ()=>{
        const rail = btn.dataset.for;
        const dir = btn.classList.contains('prev') ? -1 : 1;
        const el = getRail(rail);
        const step = Math.round(el.clientWidth*0.9);
        scrollById(rail, dir*step);
      });
    });

    // Drag-scroll
    function enableDragScroll(rail){
      if(!rail) return;
      let isDown=false,startX,scrollLeft;
      rail.addEventListener('mousedown', (e)=>{isDown=true;startX=e.pageX;scrollLeft=rail.scrollLeft;rail.style.cursor='grabbing'});
      ['mouseleave','mouseup'].forEach(ev=> rail.addEventListener(ev, ()=>{isDown=false;rail.style.cursor=''}));
      rail.addEventListener('mousemove', (e)=>{ if(!isDown) return; e.preventDefault(); const walk=(e.pageX-startX)*1.2; rail.scrollLeft=scrollLeft-walk; });
    }
    enableDragScroll(document.getElementById('foodRail'));
    enableDragScroll(document.getElementById('menuRail'));

    // Tải ảnh khi click
    function downloadImg(src){ const a=document.createElement('a'); a.href=src; a.download=src.split('/').pop(); document.body.appendChild(a); a.click(); a.remove(); }

    // Keyboard trái/phải cho phần menu
    window.addEventListener('keydown', (e)=>{
      const railId = 'menuRail';
      if(e.key==='ArrowRight') scrollById(railId, window.innerWidth*0.9);
      if(e.key==='ArrowLeft')  scrollById(railId, -window.innerWidth*0.9);
    });
  </script>
</body>
</html>
