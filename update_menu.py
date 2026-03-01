import os

with open('menu.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the data layer and rendering logic
# We need to remove the hardcoded menuItems array and comboSets (although combo sets weren't requested to be removed, we will just fetch menu-data.json)

new_script = """<script>
const comboSets = [
  { id:"combo_4", name:"Combo 4 Người Best Seller", price:750000, groupSize:4, marginLevel:"medium" },
  { id:"combo_10", name:"Combo Tiệc 10 Người", price:1300000, groupSize:10, marginLevel:"medium" }
];

document.addEventListener("DOMContentLoaded", async function () {
    function triggerGenerateLead(source, e, url) {
        if(e) e.preventDefault();
        gtag('event', 'generate_lead', { source: source });
        if(url) {
            setTimeout(function() { window.open(url, '_blank'); }, 250);
        }
    }

    gtag('event', 'view_item_list', { item_list_name: 'menu_page' });

    const formatPrice = (price) => new Intl.NumberFormat('vi-VN').format(price) + 'đ';

    const createMenuCard = (item, isBestSellerBlock = false) => {
        const bestSellerBadge = item.isBestSeller ? `<div class="absolute top-2 left-2 z-10 bg-accent text-white px-2 py-1 rounded text-[10px] uppercase font-bold shadow-sm">Best-seller</div>` : '';
        
        if (isBestSellerBlock) {
            return `
                <div class="group flex flex-col gap-3 bg-surface-white p-3 rounded-2xl shadow-sm hover:shadow-xl transition-shadow border border-transparent hover:border-primary/20 menu-item-card cursor-pointer" data-id="${item.id}" data-name="${item.name}" data-category="${item.category}" data-price="${item.price}">
                    <div class="relative w-full aspect-[4/3] rounded-xl overflow-hidden bg-gray-100">
                        ${bestSellerBadge}
                        <div class="w-full h-full bg-cover bg-center transition-transform duration-500 group-hover:scale-110" style="background-image: url('${item.image || 'https://lh3.googleusercontent.com/aida-public/AB6AXuArRcQQwHYJ_A_Rk6EeO1EUrGXgtiDuAG9jHNr2Hju-AevoBa0kSHFVtE8TMCf-PMXTCyeU2458foYrXRaBpZpaWWnIDvVkhPjNMhXdJXHCn7gM61sirVw2XFu6u1ydhPEPReoqPHWGpfYHmBmNR2CQAjS4Bjn2gpsBzXo22TGMoQU1OlhmGQrWTh8l47jt_mPMvgZCJl-lgG66t4ySb-sy_NiT6V4CUQ_wdRtHGVMS-AA7laYPrgQDw_sOCZ0vocSX4FFlg2LLx5Ik'}');"></div>
                    </div>
                    <div>
                        <p class="text-text-main text-base font-bold leading-tight group-hover:text-primary transition-colors">${item.name}</p>
                        <p class="text-primary text-sm font-bold mt-1">${formatPrice(item.price)}</p>
                    </div>
                </div>
            `;
        } else if (item.category === 'mon_chinh' || item.category === 'nuong') {
            return `
            <div class="col-span-2 md:col-span-2 group cursor-pointer bg-white p-3 rounded-xl border border-border-color menu-item-card" data-id="${item.id}" data-name="${item.name}" data-category="${item.category}" data-price="${item.price}">
                <div class="flex gap-4 items-center">
                    <div class="w-24 h-24 rounded-lg bg-gray-100 overflow-hidden shrink-0 relative">
                        ${bestSellerBadge}
                        <div class="w-full h-full bg-cover bg-center transition-transform duration-500 group-hover:scale-110" style="background-image: url('${item.image || 'https://lh3.googleusercontent.com/aida-public/AB6AXuAHml6kws6weo9ICmUNytMU1fq_IwRqriKpoXkWINjUvijDPhqXHgPGIp9wgKLgXHCOfcBOBULCqFm5ZmK2CgEFde-BjO6E3oYpiV1oLqdSPuFy_iY29zgffGcg0ATAGYsBJ6dkVWlbGglm06z29SnVpOzNL4U_bWbYsDqaerlY-t5DLV78fqtk1A4r2S33sief-rbwEgBPq1WEFRgE31Wys7ZEG2x65Cc-ndGnTldfDuAVbfosh60D13_tNLod_f8XvOVGqjDCawK-'}');"></div>
                    </div>
                    <div>
                        <h4 class="font-bold text-base group-hover:text-primary transition-colors">${item.name}</h4>
                        <p class="text-accent text-sm font-bold">${formatPrice(item.price)}</p>
                    </div>
                </div>
            </div>`;
        } else {
            return `
            <div class="group cursor-pointer menu-item-card" data-id="${item.id}" data-name="${item.name}" data-category="${item.category}" data-price="${item.price}">
                <div class="w-full aspect-square rounded-xl bg-gray-100 overflow-hidden mb-2 relative">
                    ${bestSellerBadge}
                    <div class="w-full h-full bg-cover bg-center transition-transform duration-500 group-hover:scale-110" style="background-image: url('${item.image || 'https://lh3.googleusercontent.com/aida-public/AB6AXuDN_VWn6-2g-TmPAPhyP_GiBE9z7kOn9rT1Dej01nu_J2KNs4CUn9cRcmvXXyk9jv99IMh5iJpsuhmW4b-C19wkfdij2sYLtyNQ8-zKZGrYn37ERuggFz5LVn32jNskbgvaGb1FtqrZuGmCWvB3TyGu1FfQmEv3zSdA98wgDXIAL8YRiJI_Cj1nBpxQFRvveKsPGUm3uQCYMdbFQxFDdaEwxPGOtfy74ofQqsDAuzVYXNkY7B3OEA2uz_tjx0xkAwVG5nYn2VgR0erP'}');"></div>
                </div>
                <h4 class="font-bold text-sm group-hover:text-primary transition-colors">${item.name}</h4>
                <p class="text-accent text-sm font-bold">${formatPrice(item.price)}</p>
            </div>`;
        }
    };

    try {
        const response = await fetch('menu-data.json');
        const menuItems = await response.json();

        const bestSellersContainer = document.getElementById('best-sellers-grid');
        if (bestSellersContainer) {
            bestSellersContainer.innerHTML = menuItems.filter(item => item.isBestSeller).map(item => createMenuCard(item, true)).join('');
        }

        const categories = [
            { id: 'an-nhe-grid', category: 'an_nhe' },
            { id: 'khai-vi-grid', category: 'khai_vi' },
            { id: 'lai-rai-grid', category: 'lai_rai' },
            { id: 'nuong-grid', category: 'nuong' },
            { id: 'mon-chinh-grid', category: 'mon_chinh' },
            { id: 'bia-nuoc-ngot-grid', category: 'bia_nuoc_ngot' },
            { id: 'do-uong-grid', category: 'do_uong' }
        ];

        categories.forEach(cat => {
            const catContainer = document.getElementById(cat.id);
            if (catContainer) {
                catContainer.innerHTML = menuItems.filter(item => item.category === cat.category).map(item => createMenuCard(item)).join('');
            }
        });

        const bannerHtml = `
            <div class="col-span-2 md:col-span-3 lg:col-span-3 mt-6 bg-accent/10 border border-accent/20 rounded-2xl p-4 flex flex-col md:flex-row items-center justify-between gap-4 w-full cursor-pointer hover:bg-accent/20 transition-colors" id="combo-cta-banner">
                <div>
                    <h4 class="font-bold text-accent text-lg">Gợi ý Combo 4 Người từ 750.000đ</h4>
                    <p class="text-text-secondary text-sm">Tiết kiệm hơn, đầy đủ món khai vị, nướng và lẩu.</p>
                </div>
                <button class="bg-accent text-white font-bold h-11 px-6 rounded-xl hover:bg-accent-light transition-colors shadow-md whitespace-nowrap">
                    Tư vấn Combo
                </button>
            </div>
        `;
        const bsGrid = document.getElementById('best-sellers-grid');
        if(bsGrid && !document.getElementById('combo-cta-banner')) {
            bsGrid.insertAdjacentHTML('afterend', bannerHtml);
            document.getElementById('combo-cta-banner').addEventListener('click', function(e) {
                triggerGenerateLead('menu_page', e, 'https://zalo.me/0975229739');
            });
        }

        document.querySelectorAll('.menu-item-card').forEach(card => {
            card.addEventListener('click', function() {
                gtag('event', 'select_item', {
                    item_id: this.dataset.id,
                    item_name: this.dataset.name,
                    item_category: this.dataset.category,
                    price: parseFloat(this.dataset.price)
                });
            });
        });
    } catch (error) {
        console.error('Error fetching menu data:', error);
    }

    // General Tracking Bindings
    document.querySelectorAll(".cta-zalo, a[href*='zalo.me']").forEach(function(el) {
        el.addEventListener("click", function(e) {
            triggerGenerateLead('menu_page', e, 'https://zalo.me/0975229739');
        });
    });
    document.querySelectorAll(".cta-call, a[href^='tel:'], button:contains('Đặt bàn')").forEach(function(el) {
        el.addEventListener("click", function(e) {
            triggerGenerateLead('menu_page', null, null); 
        });
    });
    document.querySelectorAll("a[href*='facebook.com'], a[href*='m.me']").forEach(function(el) {
        el.addEventListener("click", function(e) {
            triggerGenerateLead('menu_page', e, el.getAttribute('href'));
        });
    });
});
</script>"""

import re
# Replace the script block containing menuItems
content = re.sub(r'<script>\s*const menuItems = \[.*?\}\);.*?\}\);\s*</script>', new_script, content, flags=re.DOTALL)

# Update DOM elements mapping
content = content.replace('href="#hai-san"', 'href="#an-nhe"').replace('>HẢI SẢN<', '>ĂN NHẸ<')
content = content.replace('href="#mon-no"', 'href="#lai-rai"').replace('>MÓN NO<', '>LAI RAI<')
content = content.replace('href="#do-uong"', 'href="#mon-chinh"').replace('>ĐỒ UỐNG<', '>MÓN CHÍNH<')

# Let's cleanly replace the sections via regex or just rewrite the HTML sections string
sections_html = """
<section class="scroll-mt-32" id="best-sellers">
<div class="flex items-center justify-between pb-6 pt-2">
<h2 class="text-text-main text-2xl font-bold flex items-center gap-2">
<span class="material-symbols-outlined text-accent">verified</span>
                            Top Món Best-Seller
                        </h2>
</div>
<div class="grid grid-cols-2 md:grid-cols-3 gap-4 md:gap-6" id="best-sellers-grid">
</div>
</section>
<section class="scroll-mt-32" id="an-nhe">
<h3 class="text-xl font-bold border-l-4 border-primary pl-4 mb-6">Ăn Nhẹ</h3>
<div class="grid grid-cols-2 md:grid-cols-4 gap-4" id="an-nhe-grid">
</div>
</section>
<section class="scroll-mt-32" id="khai-vi">
<h3 class="text-xl font-bold border-l-4 border-primary pl-4 mb-6">Khai Vị</h3>
<div class="grid grid-cols-2 md:grid-cols-4 gap-4" id="khai-vi-grid">
</div>
</section>
<section class="scroll-mt-32" id="lai-rai">
<h3 class="text-xl font-bold border-l-4 border-primary pl-4 mb-6">Lai Rai</h3>
<div class="grid grid-cols-2 md:grid-cols-4 gap-4" id="lai-rai-grid">
</div>
</section>
<section class="scroll-mt-32" id="nuong">
<h3 class="text-xl font-bold border-l-4 border-primary pl-4 mb-6">Món Nướng</h3>
<div class="grid grid-cols-2 md:grid-cols-4 gap-4" id="nuong-grid">
</div>
</section>
<section class="scroll-mt-32" id="mon-chinh">
<h3 class="text-xl font-bold border-l-4 border-primary pl-4 mb-6">Món Chính</h3>
<div class="grid grid-cols-2 md:grid-cols-4 gap-4" id="mon-chinh-grid">
</div>
</section>
<section class="scroll-mt-32" id="bia-nuoc-ngot">
<h3 class="text-xl font-bold border-l-4 border-primary pl-4 mb-6">Bia - Nước Ngọt</h3>
<div class="grid grid-cols-2 md:grid-cols-4 gap-4" id="bia-nuoc-ngot-grid">
</div>
</section>
<section class="scroll-mt-32" id="do-uong">
<h3 class="text-xl font-bold border-l-4 border-primary pl-4 mb-6">Đồ Uống Khác</h3>
<div class="grid grid-cols-2 md:grid-cols-4 gap-4" id="do-uong-grid">
</div>
</section>
"""

# Replace all sections from <section id="best-sellers"> to right before <section id="combo">
# We can do this safely by splitting on the exact strings
start_idx = content.find('<section class="scroll-mt-32" id="best-sellers">')
end_idx = content.find('<section class="scroll-mt-32">', start_idx)

if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + sections_html + "\n" + content[end_idx:]

with open('menu.html', 'w', encoding='utf-8') as f:
    f.write(content)

