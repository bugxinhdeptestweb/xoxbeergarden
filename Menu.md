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
  <meta name="description" content="Menu XOX Beer Garden – xem nhanh, phóng to rõ nét. Chỉ cần upload ảnh vào /assets/menu/, trang tự cập nhật." />
  <link rel="canonical" href="{{ '/menu' | relative_url }}" />
  <meta property="og:title" content="Menu | XOX Beer Garden" />
  <meta property="og:description" content="Menu XOX Beer Garden – bản menu ảnh, có nút xem thêm từng đợt." />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="{{ '/menu' | absolute_url }}" />
  <meta property="og:image" content="{{ '/assets/images/og-menu.jpg' | relative_url }}" />
  <style>
    :root{--bg:#fffdf8;--ink:#111;--muted:#666;--card:#fff;--bd:#eee}
    *{box-sizing:border-box}
    body{margin:0;font-family:system-ui,Inter,Roboto,Arial;background:var(--bg);color:var(--ink)}
    .wrap{max-width:1100px;margin:0 auto;padding:16px}
    header{padding:10px 0;border-bottom:1px solid var(--bd)}
    h1{margin:8px 0}
    .hint{color:var(--muted);margin:0 0 10px}

    .grid{display:grid;gap:14px;grid-template-columns:1fr}
    @media(min-width:760px){.grid{grid-template-columns:repeat(2,1fr)}}
    @media(min-width:1040px){.grid{grid-template-columns:repeat(3,1fr)}}

    .card{border:1px solid var(--bd);border-radius:14px;overflow:hidden;background:var(--card);box-shadow:0 6px 16px rgba(0,0,0,.04)}
    .card img{display:block;width:100%;height:auto;cursor:zoom-in}
    .cap{display:flex;justify-content:space-between;gap:8px;padding:10px 12px;border-top:1px solid var(--bd);font-size:14px;color:var(--muted)}

    .actions{display:flex;justify-content:center;gap:10px;margin:18px 0}
    .btn{appearance:none;border:1px solid var(--bd);background:#fff;padding:10px 14px;border-radius:12px;cursor:pointer}
    .btn:hover{border-color:#ddd}

    /* lightbox */
    .lb{position:fixed;inset:0;background:rgba(0,0,0,.85);display:none;align-items:center;justify-content:center;z-index:20}
    .lb.show{display:flex}
    .lb img{max-width:min(96vw,1200px);max-height:90vh;border-radius:8px}
    .lbbar{position:absolute;top:10px;left:0;right:0;display:flex;justify-content:space-between;padding:0 16px}
    .pill{background:#fff;border:0;border-radius:999px;padding:8px 12px;cursor:pointer}
  </style>
</head>
<body>
  <header>
    <div class="wrap">
      <h1>Menu chính của quán</h1>
      <p class="hint">Bản menu dạng ảnh (poster). Chỉ cần upload ảnh vào <code>/assets/menu/</code>; trang tự cập nhật. Mặc định hiển thị 3 ảnh trước, bấm "Xem thêm" để tải dần.</p>
    </div>
  </header>

  <main class="wrap">
    {% assign imgs = site.static_files | where_exp:'f','f.path contains "/assets/menu/"' | sort:'path' %}

    <!-- Mảng ảnh để JS điều khiển phân trang tải dần -->
    <script>
      window.MENU_IMAGES = [
        {% for f in imgs %}"{{ f.path | relative_url }}"{% unless forloop.last %},{% endunless %}{% endfor %}
      ];
    </script>

    <div id="grid" class="grid"></div>

    <div class="actions">
      <button id="btnMore" class="btn">Xem thêm</button>
      <button id="btnAll" class="btn">Hiển thị tất cả</button>
    </div>
  </main>

  <!-- Lightbox -->
  <div id="lb" class="lb" onclick="closeLB(event)">
    <div class="lbbar">
      <button class="pill" onclick="prev(event)">⟵ Trước</button>
      <button class="pill" onclick="next(event)">Sau ⟶</button>
      <button class="pill" onclick="hide(event)">✕ Đóng</button>
    </div>
    <img id="lbimg" alt="Menu">
  </div>

  <script>
    const BATCH = 3; // mỗi lần hiện thêm 3 ảnh
    const imgs = (window.MENU_IMAGES||[]).slice();
    const grid = document.getElementById('grid');
    const btnMore = document.getElementById('btnMore');
    const btnAll = document.getElementById('btnAll');

    let shown = 0;
    function makeCard(src, idx){
      const card = document.createElement('div');
      card.className = 'card';
      const fig = document.createElement('figure');
      const img = document.createElement('img');
      img.loading = 'lazy';
      img.src = src;
      img.alt = 'Menu trang ' + (idx+1);
      img.addEventListener('click',()=>openLB(idx));
      fig.appendChild(img);
      const cap = document.createElement('div');
      cap.className = 'cap';
      const left = document.createElement('span');
      left.textContent = 'Trang ' + (idx+1);
      const right = document.createElement('span');
      const a = document.createElement('a');
      a.href = src; a.download = src.split('/').pop(); a.textContent = 'Tải trang';
      right.appendChild(a);
      cap.append(left,right);
      card.append(fig,cap);
      return card;
    }

    function renderMore(n){
      const end = Math.min(shown+n, imgs.length);
      for(let i=shown;i<end;i++){
        grid.appendChild(makeCard(imgs[i], i));
      }
      shown = end;
      if(shown>=imgs.length){ btnMore.style.display='none'; }
    }

    btnMore.addEventListener('click', ()=> renderMore(BATCH));
    btnAll.addEventListener('click', ()=> { renderMore(imgs.length); btnAll.style.display='none'; });

    // Khởi tạo: hiện 3 ảnh đầu
    renderMore(BATCH);

    // Lightbox logic
    const lb = document.getElementById('lb');
    const lbimg = document.getElementById('lbimg');
    let cur = 0;
    function openLB(i){ cur=i; lbimg.src = imgs[cur]; lb.classList.add('show'); }
    function hide(e){ e.preventDefault(); lb.classList.remove('show'); }
    function closeLB(e){ if(e.target===lb) lb.classList.remove('show'); }
    function prev(e){ e.preventDefault(); if(cur>0){ openLB(cur-1); } }
    function next(e){ e.preventDefault(); if(cur<imgs.length-1){ openLB(cur+1); } }
    window.addEventListener('keydown', e=>{ if(!lb.classList.contains('show')) return; if(e.key==='Escape') lb.classList.remove('show'); if(e.key==='ArrowLeft') prev(e); if(e.key==='ArrowRight') next(e); });
  </script>
</body>
</html>
