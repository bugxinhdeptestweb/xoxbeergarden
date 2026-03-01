import json
import re

raw_data = """{
  "id": "long-non-xao-dua-chua",
  "name": "Lòng non xào dưa chua",
  "category": "an_nhe",
  "price": 39000,
  "isBestSeller": false
},
{
  "id": "pheo-chay-toi",
  "name": "Phèo cháy tỏi",
  "category": "an_nhe",
  "price": 39000,
  "isBestSeller": false
},
{
  "id": "salad-tron",
  "name": "Salad trộn",
  "category": "an_nhe",
  "price": 39000,
  "isBestSeller": false
},
{
  "id": "mang-xao-la-lot",
  "name": "Măng xào lá lốt",
  "category": "an_nhe",
  "price": 39000,
  "isBestSeller": false
},
{
  "id": "cha-ca-sot-mam",
  "name": "Chả cá sốt mắm",
  "category": "an_nhe",
  "price": 39000,
  "isBestSeller": false
},
{
  "id": "bap-xao-bo",
  "name": "Bắp xào bơ",
  "category": "an_nhe",
  "price": 39000,
  "isBestSeller": false
},
{
  "id": "sua-sot-thai",
  "name": "Sứa sốt Thái",
  "category": "an_nhe",
  "price": 49000,
  "isBestSeller": false
},
{
  "id": "goi-sua-sot-thai",
  "name": "Gỏi sứa sốt Thái",
  "category": "an_nhe",
  "price": 49000,
  "isBestSeller": false
},
{
  "id": "doi-sun-lac-pho-mai",
  "name": "Dồi sụn lắc phô mai",
  "category": "an_nhe",
  "price": 50000,
  "isBestSeller": false
}
{
  "id": "kho-quet-rau-cu",
  "name": "Kho quẹt rau củ",
  "category": "khai_vi",
  "price": 89000,
  "isBestSeller": false
},
{
  "id": "bi-nu-xao-toi",
  "name": "Bí nụ xào tỏi",
  "category": "khai_vi",
  "price": 79000,
  "isBestSeller": false
},
{
  "id": "bi-nu-xao-bo",
  "name": "Bí nụ xào bò",
  "category": "khai_vi",
  "price": 89000,
  "isBestSeller": false
},
{
  "id": "tom-chien-xu",
  "name": "Tôm chiên xù",
  "category": "khai_vi",
  "price": 129000,
  "isBestSeller": false
},
{
  "id": "tom-sot-mayonnaise",
  "name": "Tôm sốt mayonnaise",
  "category": "khai_vi",
  "price": 139000,
  "isBestSeller": false
},
{
  "id": "tom-sot-chanh-day",
  "name": "Tôm sốt chanh dây",
  "category": "khai_vi",
  "price": 149000,
  "isBestSeller": false
},
{
  "id": "kho-qua-cha-bong",
  "name": "Khổ qua chà bông",
  "category": "khai_vi",
  "price": 89000,
  "isBestSeller": false
},
{
  "id": "nam-thap-cam-xao-bo",
  "name": "Nấm thập cẩm xào bò",
  "category": "khai_vi",
  "price": 99000,
  "isBestSeller": false
},
{
  "id": "bo-xao-hanh-can",
  "name": "Bò xào hành cần",
  "category": "khai_vi",
  "price": 99000,
  "isBestSeller": false
},
{
  "id": "luon-ngong-ap-chao",
  "name": "Lườn ngỗng áp chảo",
  "category": "khai_vi",
  "price": 89000,
  "isBestSeller": false
},
{
  "id": "ca-lim-kim-chien-gion",
  "name": "Cá lìm kìm chiên giòn",
  "category": "khai_vi",
  "price": 89000,
  "isBestSeller": false
},
{
  "id": "com-chay-ca-lim-kim",
  "name": "Cơm cháy cá lìm kìm",
  "category": "khai_vi",
  "price": 109000,
  "isBestSeller": false
},
{
  "id": "goi-ca-lim-kim",
  "name": "Gỏi cá lìm kìm",
  "category": "khai_vi",
  "price": 99000,
  "isBestSeller": false
},
{
  "id": "goi-ngo-sen",
  "name": "Gỏi ngó sen",
  "category": "khai_vi",
  "price": 129000,
  "isBestSeller": false
},
{
  "id": "bong-cai-xanh-xao-toi",
  "name": "Bông cải xanh xào tỏi",
  "category": "khai_vi",
  "price": 79000,
  "isBestSeller": false
},
{
  "id": "bong-cai-xanh-xao-bo",
  "name": "Bông cải xanh xào bò",
  "category": "khai_vi",
  "price": 99000,
  "isBestSeller": false
},
{
  "id": "bao-tu-xao-rau",
  "name": "Bao tử xào rau",
  "category": "khai_vi",
  "price": 99000,
  "isBestSeller": false
},
{
  "id": "gio-heo-xong-khoi",
  "name": "Giò heo xông khói",
  "category": "khai_vi",
  "price": 109000,
  "isBestSeller": false
},
{
  "id": "coi-so-diep-sot-bo-toi",
  "name": "Còi sò điệp sốt bơ tỏi",
  "category": "khai_vi",
  "price": 119000,
  "isBestSeller": false
},
{
  "id": "coi-so-diep-xao-nam",
  "name": "Còi sò điệp xào nấm",
  "category": "khai_vi",
  "price": 119000,
  "isBestSeller": false
}
{
  "id": "rang-muc-chien-nuoc-mam",
  "name": "Răng mực chiên nước mắm",
  "category": "lai_rai",
  "price": 99000,
  "isBestSeller": false
},
{
  "id": "rang-muc-chien-gion",
  "name": "Răng mực chiên giòn",
  "category": "lai_rai",
  "price": 99000,
  "isBestSeller": false
},
{
  "id": "rang-muc-sot-bo-toi",
  "name": "Răng mực sốt bơ tỏi",
  "category": "lai_rai",
  "price": 99000,
  "isBestSeller": false
},
{
  "id": "canh-ga-sot-nuoc-mam",
  "name": "Cánh gà sốt nước mắm",
  "category": "lai_rai",
  "price": 99000,
  "isBestSeller": false
},
{
  "id": "ga-sot-mam-tac",
  "name": "Gà sốt mắm tắc",
  "category": "lai_rai",
  "price": 99000,
  "isBestSeller": false
},
{
  "id": "ca-trung-chien-gion",
  "name": "Cá trứng chiên giòn",
  "category": "lai_rai",
  "price": 79000,
  "isBestSeller": false
},
{
  "id": "muc-trung-chien-gion",
  "name": "Mực trứng chiên giòn",
  "category": "lai_rai",
  "price": 139000,
  "isBestSeller": false
},
{
  "id": "muc-trung-sot-nuoc-mam",
  "name": "Mực trứng sốt nước mắm",
  "category": "lai_rai",
  "price": 139000,
  "isBestSeller": false
},
{
  "id": "xuc-xich",
  "name": "Xúc xích",
  "category": "lai_rai",
  "price": 49000,
  "isBestSeller": false
},
{
  "id": "pho-mai-soi-hun-khoi",
  "name": "Phô mai sợi hun khói",
  "category": "lai_rai",
  "price": 69000,
  "isBestSeller": false
},
{
  "id": "chan-ga-sot-thai",
  "name": "Chân gà sốt Thái",
  "category": "lai_rai",
  "price": 89000,
  "isBestSeller": false
},
{
  "id": "hai-san-sot-thai",
  "name": "Hải sản sốt Thái",
  "category": "lai_rai",
  "price": 169000,
  "isBestSeller": false
},
{
  "id": "cha-ram-tom-dat",
  "name": "Chả ram tôm đất",
  "category": "lai_rai",
  "price": 79000,
  "isBestSeller": false
},
{
  "id": "ba-roi-heo-chien-gion",
  "name": "Ba rọi heo chiên giòn",
  "category": "lai_rai",
  "price": 99000,
  "isBestSeller": false
},
{
  "id": "ba-roi-heo-chien-nuoc-mam",
  "name": "Ba rọi heo chiên nước mắm",
  "category": "lai_rai",
  "price": 99000,
  "isBestSeller": false
},
{
  "id": "ba-roi-sot-mam-tac",
  "name": "Ba rọi sốt mắm tắc",
  "category": "lai_rai",
  "price": 99000,
  "isBestSeller": false
},
{
  "id": "dau-hu-sot-nuoc-mam",
  "name": "Đậu hũ sốt nước mắm",
  "category": "lai_rai",
  "price": 55000,
  "isBestSeller": false
},
{
  "id": "ca-thac-lac-chien-gion",
  "name": "Cá thác lác chiên giòn",
  "category": "lai_rai",
  "price": 99000,
  "isBestSeller": false
},
{
  "id": "ech-nup-lum",
  "name": "Ếch núp lùm",
  "category": "lai_rai",
  "price": 89000,
  "isBestSeller": false
},
{
  "id": "ech-xao-sa-ot",
  "name": "Ếch xào sả ớt",
  "category": "lai_rai",
  "price": 89000,
  "isBestSeller": false
},
{
  "id": "bo-luc-lac",
  "name": "Bò lúc lắc",
  "category": "lai_rai",
  "price": 149000,
  "isBestSeller": false
},
{
  "id": "khoai-tay-chien-gion",
  "name": "Khoai tây chiên giòn",
  "category": "lai_rai",
  "price": 55000,
  "isBestSeller": false
},
{
  "id": "khoai-tay-lac-pho-mai",
  "name": "Khoai tây lắc phô mai",
  "category": "lai_rai",
  "price": 60000,
  "isBestSeller": false
},
{
  "id": "ca-du-chien-gion",
  "name": "Cá đù chiên giòn",
  "category": "lai_rai",
  "price": 69000,
  "isBestSeller": false
}
{
  "id": "tom-nuong-muoi-ot",
  "name": "Tôm nướng muối ớt",
  "category": "nuong",
  "price": 169000,
  "isBestSeller": false
},
{
  "id": "tom-nuong-sa-te",
  "name": "Tôm nướng sa tế",
  "category": "nuong",
  "price": 169000,
  "isBestSeller": false
},
{
  "id": "vach-ngan-nuong-muoi-ot",
  "name": "Vách ngăn nướng muối ớt",
  "category": "nuong",
  "price": 99000,
  "isBestSeller": false
},
{
  "id": "rau-muc-nuong",
  "name": "Râu mực nướng",
  "category": "nuong",
  "price": 139000,
  "isBestSeller": false
},
{
  "id": "rau-tuoc-nuong",
  "name": "Râu tuộc nướng",
  "category": "nuong",
  "price": 169000,
  "isBestSeller": false
},
{
  "id": "mam-sua-nuong-chao",
  "name": "Mầm sữa nướng chao",
  "category": "nuong",
  "price": 99000,
  "isBestSeller": false
},
{
  "id": "mam-sua-nuong-muoi-ot",
  "name": "Mầm sữa nướng muối ớt",
  "category": "nuong",
  "price": 99000,
  "isBestSeller": false
},
{
  "id": "doi-sun-nuong",
  "name": "Dồi sụn nướng",
  "category": "nuong",
  "price": 79000,
  "isBestSeller": false
},
{
  "id": "oc-buu-nhoi-thit",
  "name": "Ốc bưu nhồi thịt",
  "category": "nuong",
  "price": 99000,
  "isBestSeller": false
},
{
  "id": "ba-chi-heo-nuong-muoi-ot",
  "name": "Ba chỉ heo nướng muối ớt",
  "category": "nuong",
  "price": 99000,
  "isBestSeller": false
},
{
  "id": "ba-chi-bo-cuon-nam",
  "name": "Ba chỉ bò cuộn nấm",
  "category": "nuong",
  "price": 99000,
  "isBestSeller": false
},
{
  "id": "ba-chi-bo-nuong-muoi-ot",
  "name": "Ba chỉ bò nướng muối ớt",
  "category": "nuong",
  "price": 99000,
  "isBestSeller": false
},
{
  "id": "loi-thanh-bo-nuong-tieu",
  "name": "Lõi thanh bò nướng tiêu",
  "category": "nuong",
  "price": 169000,
  "isBestSeller": false
},
{
  "id": "suon-bo-nuong",
  "name": "Sườn bò nướng",
  "category": "nuong",
  "price": 169000,
  "isBestSeller": false
},
{
  "id": "bao-ngu-nuong-sot-tieu",
  "name": "Bào ngư nướng sốt tiêu",
  "category": "nuong",
  "price": 139000,
  "isBestSeller": false
}
{
  "id": "lau-thai-lon",
  "name": "Lẩu Thái lớn",
  "category": "mon_chinh",
  "price": 250000,
  "isBestSeller": false
},
{
  "id": "lau-ca-lang",
  "name": "Lẩu cá lăng",
  "category": "mon_chinh",
  "price": 199000,
  "isBestSeller": false
},
{
  "id": "lau-ga-nam",
  "name": "Lẩu gà nấm",
  "category": "mon_chinh",
  "price": 199000,
  "isBestSeller": false
},
{
  "id": "lau-ca-thac-lac",
  "name": "Lẩu cá thác lác",
  "category": "mon_chinh",
  "price": 199000,
  "isBestSeller": false
},
{
  "id": "lau-pheo",
  "name": "Lẩu phèo",
  "category": "mon_chinh",
  "price": 150000,
  "isBestSeller": false
},
{
  "id": "bao-tu-ham-tieu",
  "name": "Bao tử hầm tiêu",
  "category": "mon_chinh",
  "price": 199000,
  "isBestSeller": false
},
{
  "id": "com-chien-ca-man",
  "name": "Cơm chiên cá mặn",
  "category": "mon_chinh",
  "price": 99000,
  "isBestSeller": false
},
{
  "id": "com-chien-trai-dua",
  "name": "Cơm chiên trái dứa",
  "category": "mon_chinh",
  "price": 129000,
  "isBestSeller": false
},
{
  "id": "com-chien-dua-bo",
  "name": "Cơm chiên dưa bò",
  "category": "mon_chinh",
  "price": 109000,
  "isBestSeller": false
},
{
  "id": "mi-xao-bo",
  "name": "Mì xào bò",
  "category": "mon_chinh",
  "price": 99000,
  "isBestSeller": false
},
{
  "id": "mi-xao-hai-san",
  "name": "Mì xào hải sản",
  "category": "mon_chinh",
  "price": 109000,
  "isBestSeller": false
},
{
  "id": "mi-xao-thap-cam",
  "name": "Mì xào thập cẩm",
  "category": "mon_chinh",
  "price": 139000,
  "isBestSeller": false
},
{
  "id": "mien-xao-trung-non",
  "name": "Miến xào trứng non",
  "category": "mon_chinh",
  "price": 129000,
  "isBestSeller": false
},
{
  "id": "lau-tokbokki",
  "name": "Lẩu tokbokki",
  "category": "mon_chinh",
  "price": 129000,
  "isBestSeller": false
},
{
  "id": "khau-nhuc",
  "name": "Khâu nhục",
  "category": "mon_chinh",
  "price": 180000,
  "isBestSeller": false
}
{
  "id": "tiger-bac",
  "name": "Tiger bạc",
  "category": "bia_nuoc_ngot",
  "price": 23000,
  "isBestSeller": false
},
{
  "id": "tiger-lun",
  "name": "Tiger lùn",
  "category": "bia_nuoc_ngot",
  "price": 21000,
  "isBestSeller": false
},
{
  "id": "saigon-xanh",
  "name": "Saigon xanh",
  "category": "bia_nuoc_ngot",
  "price": 17000,
  "isBestSeller": false
},
{
  "id": "heineken-nho",
  "name": "Heineken nhỏ",
  "category": "bia_nuoc_ngot",
  "price": 21000,
  "isBestSeller": false
},
{
  "id": "7up",
  "name": "7Up",
  "category": "bia_nuoc_ngot",
  "price": 15000,
  "isBestSeller": false
},
{
  "id": "sting",
  "name": "Sting",
  "category": "bia_nuoc_ngot",
  "price": 15000,
  "isBestSeller": false
},
{
  "id": "coca",
  "name": "Coca",
  "category": "bia_nuoc_ngot",
  "price": 15000,
  "isBestSeller": false
},
{
  "id": "pepsi",
  "name": "Pepsi",
  "category": "bia_nuoc_ngot",
  "price": 15000,
  "isBestSeller": false
},
{
  "id": "nuoc-suoi",
  "name": "Nước suối",
  "category": "bia_nuoc_ngot",
  "price": 10000,
  "isBestSeller": false
}
{
  "id": "ca-phe-den",
  "name": "Cà phê đen",
  "category": "do_uong",
  "price": 15000,
  "isBestSeller": false
},
{
  "id": "ca-phe-sua",
  "name": "Cà phê sữa",
  "category": "do_uong",
  "price": 20000,
  "isBestSeller": false
},
{
  "id": "bac-xiu",
  "name": "Bạc xỉu",
  "category": "do_uong",
  "price": 30000,
  "isBestSeller": false
},
{
  "id": "ca-phe-hanh-nhan",
  "name": "Cà phê hạnh nhân",
  "category": "do_uong",
  "price": 30000,
  "isBestSeller": false
}
{
  "id": "tra-dao-nho",
  "name": "Trà đào (nhỏ)",
  "category": "do_uong",
  "price": 30000,
  "isBestSeller": false
},
{
  "id": "tra-dao-lon",
  "name": "Trà đào (lớn)",
  "category": "do_uong",
  "price": 35000,
  "isBestSeller": false
},
{
  "id": "tra-lipton-nho",
  "name": "Trà Lipton (nhỏ)",
  "category": "do_uong",
  "price": 25000,
  "isBestSeller": false
},
{
  "id": "tra-lipton-lon",
  "name": "Trà Lipton (lớn)",
  "category": "do_uong",
  "price": 30000,
  "isBestSeller": false
},
{
  "id": "tra-sua-nho",
  "name": "Trà sữa (nhỏ)",
  "category": "do_uong",
  "price": 25000,
  "isBestSeller": false
},
{
  "id": "tra-sua-lon",
  "name": "Trà sữa (lớn)",
  "category": "do_uong",
  "price": 30000,
  "isBestSeller": false
},
{
  "id": "dao-sua-nho",
  "name": "Đào sữa (nhỏ)",
  "category": "do_uong",
  "price": 30000,
  "isBestSeller": false
},
{
  "id": "dao-sua-lon",
  "name": "Đào sữa (lớn)",
  "category": "do_uong",
  "price": 35000,
  "isBestSeller": false
},
{
  "id": "tra-sua-hanh-nhan-nho",
  "name": "Trà sữa hạnh nhân (nhỏ)",
  "category": "do_uong",
  "price": 30000,
  "isBestSeller": false
},
{
  "id": "tra-sua-hanh-nhan-lon",
  "name": "Trà sữa hạnh nhân (lớn)",
  "category": "do_uong",
  "price": 35000,
  "isBestSeller": false
},
{
  "id": "tra-sua-hat-de-nho",
  "name": "Trà sữa hạt dẻ (nhỏ)",
  "category": "do_uong",
  "price": 30000,
  "isBestSeller": false
},
{
  "id": "tra-sua-hat-de-lon",
  "name": "Trà sữa hạt dẻ (lớn)",
  "category": "do_uong",
  "price": 35000,
  "isBestSeller": false
}{
  "id": "nuoc-ep-cam",
  "name": "Nước ép cam",
  "category": "do_uong",
  "price": 30000,
  "isBestSeller": false
},
{
  "id": "nuoc-ep-dua-hau",
  "name": "Nước ép dưa hấu",
  "category": "do_uong",
  "price": 30000,
  "isBestSeller": false
},
{
  "id": "nuoc-ep-dua",
  "name": "Nước ép dứa",
  "category": "do_uong",
  "price": 35000,
  "isBestSeller": false
},
{
  "id": "nuoc-ep-chanh",
  "name": "Nước ép chanh",
  "category": "do_uong",
  "price": 25000,
  "isBestSeller": false
},
{
  "id": "nuoc-ep-tao",
  "name": "Nước ép táo",
  "category": "do_uong",
  "price": 35000,
  "isBestSeller": false
},
{
  "id": "nuoc-ep-oi",
  "name": "Nước ép ổi",
  "category": "do_uong",
  "price": 30000,
  "isBestSeller": false
},
{
  "id": "nuoc-ep-ca-rot",
  "name": "Nước ép cà rốt",
  "category": "do_uong",
  "price": 30000,
  "isBestSeller": false
}{
  "id": "sua-chua-da",
  "name": "Sữa chua đá",
  "category": "do_uong",
  "price": 30000,
  "isBestSeller": false
},
{
  "id": "sua-chua-viet-quat",
  "name": "Sữa chua việt quất",
  "category": "do_uong",
  "price": 35000,
  "isBestSeller": false
},
{
  "id": "sua-chua-dau",
  "name": "Sữa chua dâu",
  "category": "do_uong",
  "price": 35000,
  "isBestSeller": false
},
{
  "id": "sua-chua-xoai",
  "name": "Sữa chua xoài",
  "category": "do_uong",
  "price": 35000,
  "isBestSeller": false
}{
  "id": "soda-viet-quat",
  "name": "Soda việt quất",
  "category": "do_uong",
  "price": 30000,
  "isBestSeller": false
},
{
  "id": "soda-dau",
  "name": "Soda dâu",
  "category": "do_uong",
  "price": 30000,
  "isBestSeller": false
}{
  "id": "o-long-matcha-latte",
  "name": "Ô long matcha latte",
  "category": "do_uong",
  "price": 25000,
  "isBestSeller": false
},
{
  "id": "tra-xanh-matcha-latte",
  "name": "Trà xanh matcha latte",
  "category": "do_uong",
  "price": 25000,
  "isBestSeller": false
}{
  "id": "ca-phe-kem-cheese",
  "name": "Cà phê kem cheese",
  "category": "do_uong",
  "price": 25000,
  "isBestSeller": false
},
{
  "id": "ca-cao-kem-cheese",
  "name": "Ca cao kem cheese",
  "category": "do_uong",
  "price": 30000,
  "isBestSeller": false
},
{
  "id": "hong-tra-kem-cheese",
  "name": "Hồng trà kem cheese",
  "category": "do_uong",
  "price": 30000,
  "isBestSeller": false
},
{
  "id": "tra-sua-kem-cheese",
  "name": "Trà sữa kem cheese",
  "category": "do_uong",
  "price": 30000,
  "isBestSeller": false
},
{
  "id": "tra-xoai-kem-cheese",
  "name": "Trà xoài kem cheese",
  "category": "do_uong",
  "price": 35000,
  "isBestSeller": false
}{
  "id": "matcha-da-xay",
  "name": "Matcha đá xay",
  "category": "do_uong",
  "price": 30000,
  "isBestSeller": false
},
{
  "id": "viet-quat-da-xay",
  "name": "Việt quất đá xay",
  "category": "do_uong",
  "price": 30000,
  "isBestSeller": false
},
{
  "id": "xoai-da-xay",
  "name": "Xoài đá xay",
  "category": "do_uong",
  "price": 35000,
  "isBestSeller": false
},
{
  "id": "cam-dao-da-xay",
  "name": "Cam đào đá xay",
  "category": "do_uong",
  "price": 35000,
  "isBestSeller": false
},
{
  "id": "xoai-chanh-da-xay",
  "name": "Xoài chanh đá xay",
  "category": "do_uong",
  "price": 35000,
  "isBestSeller": false
},
{
  "id": "sua-chua-xoai-xay",
  "name": "Sữa chua xoài xay",
  "category": "do_uong",
  "price": 35000,
  "isBestSeller": false
},
{
  "id": "sua-chua-dao-xay",
  "name": "Sữa chua đào xay",
  "category": "do_uong",
  "price": 35000,
  "isBestSeller": false
},
{
  "id": "sua-chua-viet-quat-xay",
  "name": "Sữa chua việt quất xay",
  "category": "do_uong",
  "price": 35000,
  "isBestSeller": false
},
{
  "id": "sua-chua-dau-xay",
  "name": "Sữa chua dâu xay",
  "category": "do_uong",
  "price": 35000,
  "isBestSeller": false
}{
  "id": "sunrise-cam-dao",
  "name": "Sunrise cam đào",
  "category": "do_uong",
  "price": 30000,
  "isBestSeller": false
},
{
  "id": "thom-cam-soda",
  "name": "Thơm cam soda",
  "category": "do_uong",
  "price": 35000,
  "isBestSeller": false
},
{
  "id": "chanh-tuyet",
  "name": "Chanh tuyết",
  "category": "do_uong",
  "price": 25000,
  "isBestSeller": false
},
{
  "id": "blueberry-cloud",
  "name": "Blueberry cloud",
  "category": "do_uong",
  "price": 35000,
  "isBestSeller": false
}{
  "id": "whiskey-sour",
  "name": "Whiskey Sour",
  "category": "do_uong",
  "price": 50000,
  "isBestSeller": false
},
{
  "id": "old-fashioned",
  "name": "Old Fashioned",
  "category": "do_uong",
  "price": 50000,
  "isBestSeller": false
},
{
  "id": "negroni",
  "name": "Negroni",
  "category": "do_uong",
  "price": 40000,
  "isBestSeller": false
},
{
  "id": "black-white-russian",
  "name": "Black/White Russian",
  "category": "do_uong",
  "price": 50000,
  "isBestSeller": false
},
{
  "id": "jagerbomb",
  "name": "JagerBomb",
  "category": "do_uong",
  "price": 50000,
  "isBestSeller": false
}{
  "id": "tequila-sunrise",
  "name": "Tequila Sunrise",
  "category": "do_uong",
  "price": 50000,
  "isBestSeller": false
},
{
  "id": "malibu-sunrise",
  "name": "Malibu Sunrise",
  "category": "do_uong",
  "price": 65000,
  "isBestSeller": false
},
{
  "id": "clover-club",
  "name": "Clover Club",
  "category": "do_uong",
  "price": 50000,
  "isBestSeller": false
},
{
  "id": "ps-i-love-you",
  "name": "P.S I Love You",
  "category": "do_uong",
  "price": 70000,
  "isBestSeller": false
},
{
  "id": "pina-colada",
  "name": "Pina Colada",
  "category": "do_uong",
  "price": 50000,
  "isBestSeller": false
}{
  "id": "mojito",
  "name": "Mojito",
  "category": "do_uong",
  "price": 50000,
  "isBestSeller": false
},
{
  "id": "mojito-viet-quat",
  "name": "Mojito Việt quất",
  "category": "do_uong",
  "price": 55000,
  "isBestSeller": false
},
{
  "id": "mojito-dao",
  "name": "Mojito đào",
  "category": "do_uong",
  "price": 55000,
  "isBestSeller": false
},
{
  "id": "mojito-xoai",
  "name": "Mojito xoài",
  "category": "do_uong",
  "price": 55000,
  "isBestSeller": false
},
{
  "id": "ginlet",
  "name": "Ginlet",
  "category": "do_uong",
  "price": 50000,
  "isBestSeller": false
},
{
  "id": "midori-sour",
  "name": "Midori Sour",
  "category": "do_uong",
  "price": 60000,
  "isBestSeller": false
},
{
  "id": "margarita",
  "name": "Margarita",
  "category": "do_uong",
  "price": 50000,
  "isBestSeller": false
},
{
  "id": "daquiri",
  "name": "Daquiri",
  "category": "do_uong",
  "price": 40000,
  "isBestSeller": false
}"""

# Fix missing commas
fixed_content = re.sub(r'\}\s*\{', '},\n{', raw_data)
# Add the Best Sellers the user mentioned explicitly:
# Sụn gà chiên nước mắm
# Chả giò XOX
# Cơm chiên hải sản
# Lẩu Thái nhỏ
# Nướng thập cẩm
# Gỏi ngũ sắc thịt bò

# Add these core items provided from the new user prompt: 
added_items = [
  {
    "id": "sun-ga-chien-nuoc-mam",
    "name": "Sụn gà chiên nước mắm",
    "category": "khai_vi",
    "price": 99000,
    "isBestSeller": True
  },
  {
    "id": "cha-gio-xox",
    "name": "Chả giò XOX",
    "category": "khai_vi",
    "price": 69000,
    "isBestSeller": True
  },
  {
    "id": "com-chien-hai-san",
    "name": "Cơm chiên hải sản",
    "category": "mon_chinh",
    "price": 89000,
    "isBestSeller": True
  },
  {
    "id": "lau-thai-nho",
    "name": "Lẩu Thái nhỏ",
    "category": "mon_chinh",
    "price": 199000,
    "isBestSeller": True
  },
  {
    "id": "nuong-thap-cam",
    "name": "Nướng thập cẩm",
    "category": "nuong",
    "price": 299000,
    "isBestSeller": True
  },
  {
    "id": "goi-ngu-sac-thit-bo",
    "name": "Gỏi ngũ sắc thịt bò",
    "category": "khai_vi",
    "price": 119000,
    "isBestSeller": True
  }
]

# I need to handle that we shouldn't create duplicates. The raw_data the user gave might not contain all of them.
# The `isBestSeller` property of `Sụn gà chiên nước mắm` etc. is going to be set to true.

try:
    items = json.loads(f"[{fixed_content}]")
except Exception as e:
    print(f"Error parsing json: {e}")
    items = []

all_items = items + added_items

def slugify(s):
    # Removing accents
    s = re.sub(r'[áàảãạăắằẳẵặâấầẩẫậ]', 'a', s)
    s = re.sub(r'[ÁÀẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬ]', 'a', s)
    s = re.sub(r'[đĐ]', 'd', s)
    s = re.sub(r'[éèẻẽẹêếềểễệ]', 'e', s)
    s = re.sub(r'[ÉÈẺẼẸÊẾỀỂỄỆ]', 'e', s)
    s = re.sub(r'[íìỉĩị]', 'i', s)
    s = re.sub(r'[ÍÌỈĨỊ]', 'i', s)
    s = re.sub(r'[óòỏõọôốồổỗộơớờởỡợ]', 'o', s)
    s = re.sub(r'[ÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢ]', 'o', s)
    s = re.sub(r'[úùủũụưứừửữự]', 'u', s)
    s = re.sub(r'[ÚÙỦŨỤƯỨỪỬỮỰ]', 'u', s)
    s = re.sub(r'[ýỳỷỹỵ]', 'y', s)
    s = re.sub(r'[ÝỲỶỸỴ]', 'y', s)
    s = s.lower()
    s = re.sub(r'[^a-z0-9\s-]', '', s)
    s = re.sub(r'[\s-]+', '-', s).strip('-')
    return s

best_sellers = ["Sụn gà chiên nước mắm", "Chả giò XOX", "Cơm chiên hải sản", "Lẩu Thái nhỏ", "Nướng thập cẩm", "Gỏi ngũ sắc thịt bò"]

# Add formatting and fix fields safely
unique_dict = {}
for i in all_items:
    i['id'] = slugify(i['name'])
    i['isBestSeller'] = i['name'] in best_sellers
    unique_dict[i['id']] = i

with open('menu-data.json', 'w', encoding='utf-8') as f:
    json.dump(list(unique_dict.values()), f, ensure_ascii=False, indent=2)

print("Created menu-data.json")
