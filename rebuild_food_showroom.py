from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parent
WA = "https://wa.me/905355727525"


def slug(text: str) -> str:
    table = str.maketrans("çğıöşüÇĞİÖŞÜ&/", "cgiosuCGIOSU--")
    out = text.translate(table).lower()
    return "-".join("".join(ch if ch.isalnum() else " " for ch in out).split())


products = [
    {
        "category": "Sebze Hazırlama",
        "title": "Sebze Yıkama Makinesi",
        "subtitle": "Yüksek verim, derin temizlik ve hijyenik yıkama",
        "image": "assets/food-vegetable-washing.jpg",
        "intro": "Meyve ve sebzelerin yüzeyindeki toz, toprak ve tarım kalıntılarını balonlu su akışı ile temizlemek için tasarlanmış profesyonel yıkama çözümüdür.",
        "features": ["360° balonlu su yıkama", "Gıda sınıfı 304 paslanmaz çelik", "Hızlı drenaj sistemi", "Akıllı kontrol paneli", "Düşük enerji tüketimi"],
        "applications": ["Yemek fabrikaları", "Otel ve restoran mutfakları", "Sebze işleme tesisleri", "Market hazırlık alanları"],
        "specs": [("Malzeme", "304 paslanmaz çelik"), ("Yıkama sistemi", "Balonlu / sirkülasyonlu su akışı"), ("Kapasite", "Proje ihtiyacına göre belirlenir"), ("Kontrol", "Zaman ve çalışma ayarı yapılabilir")],
    },
    {
        "category": "Hamur & Makarna",
        "title": "Makarna Üretim Hattı",
        "subtitle": "Verimli, akıllı ve özelleştirilebilir üretim hattı",
        "image": "assets/food-pasta-production-line.jpg",
        "intro": "Taze makarna, noodle ve farklı hamur ürünleri için yoğurma, taşıma, şekillendirme ve kesim süreçlerini tek projede birleştiren üretim hattıdır.",
        "features": ["Paslanmaz çelik temas yüzeyi", "Akıllı kontrol sistemi", "Yüksek üretim verimliliği", "Farklı makarna tiplerine uyum", "İhtiyaca göre hat tasarımı"],
        "applications": ["Makarna üretim atölyeleri", "Merkezi mutfaklar", "Restoran zincirleri", "Gıda fabrikaları"],
        "specs": [("Hat yapısı", "Karıştırma, taşıma, şekillendirme ve kesim modülleri"), ("Ürün tipi", "İnce, orta, kalın ve geniş kesim seçenekleri"), ("Kapasite", "Üretim hedefi ve reçeteye göre projelendirilir")],
    },
    {
        "category": "Et & Dolgu Hazırlama",
        "title": "Et Doğrama & Karıştırma Makinesi",
        "subtitle": "Hızlı, güçlü ve homojen hazırlık",
        "image": "assets/food-bowl-cutter-mixer.jpg",
        "intro": "Dana eti, tavuk, balık ve sebzeleri kısa sürede doğrayarak kıyma, kuşbaşı, karışım ve püre kıvamına getiren profesyonel kase tipi doğrama çözümüdür.",
        "features": ["Yüksek hızlı bıçak sistemi", "Güçlü motor", "304 paslanmaz çelik gövde", "Kolay sökülebilir temizlik yapısı", "Koruyucu kapak ile güvenli kullanım"],
        "applications": ["Köfte ve dolgu hazırlığı", "Tavuk ve balık işleme", "Sebze doğrama", "Sos ve püre hazırlığı"],
        "specs": [("Bıçak hızı", "Yaklaşık 1500-3000 rpm aralığında seçenekler"), ("Malzeme", "Gıda sınıfı paslanmaz çelik"), ("Kapasite", "Model ve kazan hacmine göre belirlenir")],
    },
    {
        "category": "Et & Dolgu Hazırlama",
        "title": "Çift Kafa Et Doğrama Makinesi",
        "subtitle": "Et işlemede güçlü, hızlı ve verimli çözüm",
        "image": "assets/food-double-head-meat-cutter.jpg",
        "intro": "Dana eti, tavuk ve benzeri ürünlerde kıyma, şerit ve dilim kesim işlemlerini aynı üretim alanında yönetmek için çift kafa tasarımlı endüstriyel makinedir.",
        "features": ["Çift kafa kesim sistemi", "Farklı kesim seçenekleri", "Paslanmaz çelik gövde", "Düşük sesli çalışma", "Kolay kontrol paneli"],
        "applications": ["Kasaplar", "Restoranlar", "Et hazırlık mutfakları", "Gıda üretim tesisleri"],
        "specs": [("Kesim türleri", "Kıyma, et şeridi ve et dilimi"), ("Gövde", "Paslanmaz çelik"), ("Kapasite", "Kesim türü ve modele göre projelendirilir")],
    },
    {
        "category": "Sebze Hazırlama",
        "title": "Sebze Kurutma Santrifüj Makinesi",
        "subtitle": "Doğranmış sebzeler için hızlı su atma sistemi",
        "image": "assets/food-vegetable-centrifuge.jpg",
        "intro": "Yıkanmış ve doğranmış sebzelerde fazla suyu saniyeler içinde uzaklaştırarak tazeliği, doku kalitesini ve servis hazırlık hızını artırır.",
        "features": ["Yüksek hızlı santrifüj", "Hızlı su tahliyesi", "Paslanmaz çelik iç sepet", "Düşük ses seviyesi", "Kolay sökülür hijyenik tasarım"],
        "applications": ["Marul", "Lahana", "Havuç", "Salatalık", "Yeşil soğan"],
        "specs": [("Hız", "Yaklaşık 1000-1200 rpm"), ("Malzeme", "Paslanmaz çelik sepet"), ("Kapasite", "Sepet hacmine göre belirlenir")],
    },
    {
        "category": "Et & Dolgu Hazırlama",
        "title": "Endüstriyel Karıştırma Makinesi",
        "subtitle": "Homojen karışım ve lezzetli sonuçlar",
        "image": "assets/food-industrial-filling-mixer.jpg",
        "intro": "Dana eti, sebze, baharat ve dolgu malzemelerini homojen şekilde karıştırmak için merkezi mutfak ve gıda üretim tesislerine uygun profesyonel mikserdir.",
        "features": ["Çift yönlü karıştırma", "Güçlü motor", "Paslanmaz çelik gövde", "Düşük sesli çalışma", "Acil durdurma ile güvenli kullanım"],
        "applications": ["Köfte içi", "Mantı içi", "Börek içi", "Baozi / bun içi", "Lahmacun içi"],
        "specs": [("Karıştırma", "Homojen dolgu hazırlığı"), ("Gövde", "Paslanmaz çelik"), ("Kapasite", "Kazan hacmine göre seçilir")],
    },
    {
        "category": "Hamur & Makarna",
        "title": "Lahmacun & Noodle Makinesi",
        "subtitle": "Farklı noodle şekilleri ve profesyonel üretim",
        "image": "assets/food-lahmacun-noodle-machine.jpg",
        "intro": "Taze noodle, erişte ve lahmacun hamuru hazırlığında kesim kalınlığı ve üretim hızını kontrol ederek standart ürün kalitesi sağlar.",
        "features": ["Farklı noodle kalınlıkları", "Keskin paslanmaz bıçaklar", "Akıllı kontrol sistemi", "Ayarlanabilir hız", "Kolay temizlik ve bakım"],
        "applications": ["İnce noodle", "Orta kesim noodle", "Kalın noodle", "Geniş bıçak kesimi", "Lahmacun hamuru hazırlığı"],
        "specs": [("Kesim seçenekleri", "İnce, orta, kalın ve geniş"), ("Kontrol", "Hız ve kalınlık ayarı"), ("Kapasite", "Saatlik üretim hedefi ile belirlenir")],
    },
    {
        "category": "Sebze Hazırlama",
        "title": "Çift Kafa Sebze Doğrama Makinesi",
        "subtitle": "Dilim, küp, julienne, şerit ve blok kesim",
        "image": "assets/food-double-head-vegetable-cutter.jpg",
        "intro": "Profesyonel mutfaklarda sebzeleri standart ölçülerde dilim, küp, julienne, şerit ve blok formunda hazırlamak için çift kafa tasarımlı kesim makinesidir.",
        "features": ["Çift kafa tasarımı", "Ayarlanabilir kesim boyutu", "Dokunmatik / kullanıcı dostu kontrol", "Paslanmaz çelik gövde", "Yüksek verimli hijyenik temizlik"],
        "applications": ["Salatalık dilimleme", "Havuç küp kesim", "Julienne sebze", "Şerit kesim", "Blok kesim"],
        "specs": [("Kapasite", "Yaklaşık 500-1000 kg/saat seçenekleri"), ("Motor", "1.5 kW sınıfı güçlü motor seçenekleri"), ("Bıçak", "Paslanmaz ve değiştirilebilir kesim bıçakları")],
    },
    {
        "category": "Paketleme & Pişirme",
        "title": "Çift Hazneli Vakumlu Paketleme Makinesi",
        "subtitle": "Yüksek verim, güçlü vakum ve uzun raf ömrü",
        "image": "assets/food-double-chamber-vacuum-packaging.jpg",
        "intro": "Gıda ürünlerini vakumlayarak tazeliği korur, raf ömrünü uzatır ve hijyenik ambalajlama sağlar. Çift hazneli yapı kesintisiz çalışma için uygundur.",
        "features": ["Çift hazne ile yüksek verim", "Güçlü vakum sistemi", "Dijital kontrol paneli", "Paslanmaz çelik gövde", "Et, sebze, deniz ürünü ve kuru gıda için geniş kullanım"],
        "applications": ["Dana eti ürünleri", "Sebze ve meyveler", "Deniz ürünleri", "Kuru gıdalar"],
        "specs": [("Model", "DZ-600/2S"), ("Güç", "2200 W"), ("Voltaj", "380V / 50Hz"), ("Vakum pompası", "20 m³/h"), ("Hazne ölçüsü", "600 x 540 x 110 mm (x2)"), ("Maks. paket boyutu", "600 x 450 mm"), ("Kaynak uzunluğu", "600 mm (x2)"), ("Kaynak genişliği", "10 mm"), ("Makine boyutu", "1510 x 700 x 960 mm"), ("Ağırlık", "280 kg")],
    },
    {
        "category": "Sebze Hazırlama",
        "title": "Endüstriyel Sebze Soyma Makinesi",
        "subtitle": "Patates ve havuç için hızlı, verimli soyma",
        "image": "assets/food-root-vegetable-peeler.jpg",
        "intro": "Patates, havuç ve benzeri kök sebzelerin kabuklarını hızlı ve etkili şekilde soyarak iş gücü tasarrufu ve standart üretim kalitesi sağlar.",
        "features": ["Aşındırıcı iç yüzey", "Kısa sürede yüksek verim", "Sağlam paslanmaz çelik gövde", "Kolay kullanım ve bakım", "Su tasarruflu çalışma"],
        "applications": ["Patates", "Havuç", "Tatlı patates", "Pancar", "Turp ve kök sebzeler"],
        "specs": [("Model", "TP-1000"), ("Kapasite", "1000 kg/saat"), ("Güç", "1500 W"), ("Voltaj", "380V / 50Hz"), ("Soyma süresi", "1-3 dakika (ürüne göre)"), ("Dönüş hızı", "220 rpm"), ("İç yüzey", "Aşındırıcı zımpara kaplama"), ("Gövde malzemesi", "Paslanmaz çelik"), ("Su girişi", "1/2 inch"), ("Tahliye çıkışı", "1 inch"), ("Makine boyutu", "1100 x 700 x 1100 mm"), ("Ağırlık", "120 kg")],
    },
    {
        "category": "Hamur & Makarna",
        "title": "Endüstriyel Hamur Yoğurma Makinesi",
        "subtitle": "Güçlü performans ve mükemmel hamur kıvamı",
        "image": "assets/food-dough-kneader.jpg",
        "intro": "Ekmek, pide, pizza, börek, mantı ve benzeri hamur işleri için yüksek hacimli, homojen ve hijyenik yoğurma sağlar.",
        "features": ["Güçlü motor", "Paslanmaz çelik hazne", "Kolay kontrol paneli", "Kolay temizlik", "Düşük sesli çalışma"],
        "applications": ["Ekmek üretimi", "Pide ve pizza", "Börek ve katmer", "Mantı ve erişte", "Poğaça ve çörek"],
        "specs": [("Kapasite", "25 kg un"), ("Un kapasitesi", "25 kg"), ("Hamur kapasitesi", "40-50 kg"), ("Güç", "1.5 kW"), ("Voltaj", "380V / 50Hz"), ("Karıştırma hızı", "40-45 rpm"), ("Kazan ölçüsü", "620 x 420 x 400 mm"), ("Makine ölçüsü", "930 x 580 x 900 mm"), ("Ağırlık", "120 kg")],
    },
    {
        "category": "Hamur & Makarna",
        "title": "Hamur Yoğurma Rulo Makinesi",
        "subtitle": "Pürüzsüz, esnek ve standart hamur yüzeyi",
        "image": "assets/food-dough-roller.jpg",
        "intro": "Hamurun gluten yapısını güçlendirir, yüzeyini pürüzsüz hale getirir ve pizza, börek, mantı, yufka, erişte ve dumpling hamurlarında standart sonuç verir.",
        "features": ["Çift yönlü yoğurma", "Ayarlanabilir kalınlık", "Paslanmaz çelik gövde", "Acil durdurma ve koruyucu kapak", "Kolay temizlenir yapı"],
        "applications": ["Ekmek hamuru", "Pizza hamuru", "Börek ve yufka", "Mantı ve erişte", "Dumpling hamuru"],
        "specs": [("Model", "YJ-520"), ("Güç", "1500 W"), ("Voltaj", "220V / 50Hz"), ("Yoğurma genişliği", "520 mm"), ("Konveyör uzunluğu", "1200 mm"), ("Yoğurma kalınlığı", "1-35 mm ayarlanabilir"), ("Yoğurma hızı", "60 rpm ileri / 42 rpm geri"), ("Makine ölçüleri", "1450 x 750 x 620 mm"), ("Ağırlık", "120 kg")],
    },
    {
        "category": "Filizlendirme",
        "title": "Otomatik Filizlendirme Makinesi",
        "subtitle": "Tam otomatik, temiz, verimli ve kolay kullanım",
        "image": "assets/food-sprout-machine.jpg",
        "intro": "Sarı soya fasulyesi, yeşil mung fasulyesi ve benzeri filiz ürünleri için sulama, temizlik, havalandırma ve sıcaklık kontrolünü otomatik yönetir.",
        "features": ["Otomatik zaman ayarlı sulama", "360° döner sprey başlıkları", "Güçlü havalandırma sistemi", "Dijital sıcaklık kontrolü", "Katlı tepsi sistemi"],
        "applications": ["Soya filizi", "Yeşil mung filizi", "Restoran ve oteller", "Gıda üretim tesisleri", "Market ve sağlıklı gıda üreticileri"],
        "specs": [("Model", "NJ-FLZ-200"), ("Kapasite", "200 kg kuru fasulye/gün"), ("Malzeme", "304 paslanmaz çelik"), ("Sulama sistemi", "Otomatik zaman ayarlı sprey sulama"), ("Temizleme sistemi", "360° döner sprey başlıkları"), ("Havalandırma", "Güçlü fan ile hava sirkülasyonu"), ("Sıcaklık kontrolü", "Dijital termostat 15-35°C"), ("Kat sayısı", "5 kat, isteğe bağlı özelleştirilebilir"), ("Tepsi ölçüsü", "600 x 400 mm"), ("Güç", "2.2 kW"), ("Voltaj", "380V / 50Hz"), ("Makine ölçüleri", "2000 x 800 x 1800 mm"), ("Ağırlık", "280 kg")],
    },
    {
        "category": "Paketleme & Pişirme",
        "title": "12 Katlı Buharlı Pişirici",
        "subtitle": "Çok amaçlı, yüksek verimli buharlı pişirme kabini",
        "image": "assets/food-steam-cabinet.jpg",
        "intro": "12 katlı tepsi sistemi ile buharda pişirme ihtiyaçlarını hijyenik, hızlı ve güvenilir şekilde karşılayan endüstriyel pişirme çözümüdür.",
        "features": ["Güçlü buhar sistemi", "12 katlı geniş kapasite", "Paslanmaz çelik kabin", "Enerji tasarruflu ısıtma", "Kolay temizlik ve bakım"],
        "applications": ["Bao ve buharda hamur işleri", "Pirinç", "Sebze", "Mantı / dumpling", "Balık ve dana eti ürünleri"],
        "specs": [("Kapasite", "12 tepsi"), ("Malzeme", "Paslanmaz çelik"), ("Isıtma yöntemi", "Buhar"), ("Güç", "18 kW"), ("Voltaj", "380V / 50Hz"), ("Tepsi ölçüsü", "400 x 600 mm"), ("Boyutlar", "700 x 850 x 1750 mm"), ("Ağırlık", "120 kg")],
    },
]


categories = []
for product in products:
    if product["category"] not in categories:
        categories.append(product["category"])


def wa_link(title: str) -> str:
    text = f"Merhaba NJ GROUP, {title} için bilgi ve fiyat teklifi almak istiyorum."
    return f"{WA}?text={quote(text)}"


def spec_table(specs):
    rows = "\n".join(f"<tr><th>{name}</th><td>{value}</td></tr>" for name, value in specs)
    return f"<table class=\"spec-table\"><tbody>{rows}</tbody></table>"


directory = "\n".join(
    f"""
        <section class="catalog-group">
          <h3>{category}</h3>
          <div class="catalog-links">
            {''.join(f'<a href="#{slug(p["title"])}">{p["title"]}</a>' for p in products if p["category"] == category)}
          </div>
        </section>"""
    for category in categories
)


cards = "\n".join(
    f"""
        <article class="product-card" id="{slug(product["title"])}">
          <div class="product-media">
            <img src="{product["image"]}" alt="NJ GROUP {product["title"]}" loading="lazy">
          </div>
          <div class="product-copy">
            <span class="category">{product["category"]}</span>
            <h3>{product["title"]}</h3>
            <p class="subtitle">{product["subtitle"]}</p>
            <p>{product["intro"]}</p>
            <div class="feature-list">
              {''.join(f'<span>{feature}</span>' for feature in product["features"])}
            </div>
            <div class="detail-grid">
              <div>
                <h4>Kullanım alanları</h4>
                <ul>{''.join(f'<li>{item}</li>' for item in product["applications"])}</ul>
              </div>
              <div>
                <h4>Teknik bilgiler</h4>
                {spec_table(product["specs"])}
              </div>
            </div>
            <a class="mini-cta" href="{wa_link(product["title"])}">WhatsApp ile teklif iste</a>
          </div>
        </article>"""
    for product in products
)


schema_products = ",\n".join(
    f"""      {{"@type":"Product","name":"{product["title"]}","brand":{{"@type":"Brand","name":"NJ GROUP"}},"category":"{product["category"]}","image":"https://njgrup.com/{product["image"]}","areaServed":"Türkiye","url":"https://njgrup.com/gida-makinalari.html#{slug(product["title"])}"}}"""
    for product in products
)


html = f"""<!doctype html>
<html lang="tr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>NJ GROUP Gıda Makineleri | Endüstriyel Mutfak ve Üretim Ekipmanları</title>
  <meta name="description" content="NJ GROUP gıda makineleri showroomu: sebze yıkama, sebze doğrama, et hazırlama, hamur yoğurma, makarna, vakum paketleme, filizlendirme ve buharlı pişirme çözümleri.">
  <link rel="canonical" href="https://njgrup.com/gida-makinalari.html">
  <style>
    :root {{ --ink:#10201c; --deep:#0b2f27; --green:#134c3d; --gold:#c79b3b; --paper:#f7f8f6; --muted:#60736d; --line:#dfe8e3; --white:#fff; }}
    * {{ box-sizing:border-box; }}
    html {{ scroll-behavior:smooth; }}
    body {{ margin:0; font-family:Inter, Arial, Helvetica, sans-serif; color:var(--ink); background:var(--paper); line-height:1.6; overflow-x:hidden; }}
    a {{ color:inherit; text-decoration:none; }}
    .wrap {{ width:min(1180px, calc(100% - 32px)); margin:auto; }}
    header {{ position:sticky; top:0; z-index:40; background:rgba(11,47,39,.96); color:#fff; border-bottom:1px solid rgba(255,255,255,.12); backdrop-filter:blur(14px); }}
    .head {{ min-height:76px; display:flex; align-items:center; justify-content:space-between; gap:18px; }}
    .brand {{ display:flex; align-items:center; gap:12px; font-weight:800; letter-spacing:.2px; }}
    .brand img {{ width:54px; height:54px; object-fit:contain; border-radius:6px; background:rgba(255,255,255,.06); padding:4px; }}
    .brand small {{ display:block; color:rgba(255,255,255,.72); font-size:12px; margin-top:2px; }}
    nav {{ display:flex; align-items:center; gap:20px; color:rgba(255,255,255,.82); font-size:14px; font-weight:700; }}
    nav a:hover {{ color:#fff; }}
    .lang {{ height:34px; border:1px solid rgba(255,255,255,.22); border-radius:6px; color:#fff; background:rgba(255,255,255,.08); padding:0 8px; }}
    .hero {{ position:relative; color:#fff; background:linear-gradient(90deg,rgba(7,28,24,.94),rgba(19,76,61,.78)), url('assets/food-vegetable-washing.jpg') center/cover; }}
    .hero .wrap {{ min-height:610px; display:grid; align-content:center; padding:86px 0; }}
    .eyebrow {{ color:#f2c96d; font-weight:900; letter-spacing:.12em; text-transform:uppercase; font-size:13px; }}
    h1 {{ margin:14px 0 18px; max-width:900px; font-size:clamp(38px,6vw,72px); line-height:1.02; }}
    h1 span {{ display:block; }}
    .hero p {{ max-width:760px; margin:0 0 28px; color:#e6f3ef; font-size:20px; }}
    .cta-row {{ display:flex; flex-wrap:wrap; gap:14px; }}
    .btn {{ display:inline-flex; align-items:center; justify-content:center; min-height:46px; padding:12px 20px; border-radius:6px; font-weight:900; }}
    .btn.gold {{ background:var(--gold); color:#171308; }}
    .btn.light {{ border:1px solid rgba(255,255,255,.55); color:#fff; }}
    .hero-stats {{ display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:12px; margin-top:44px; max-width:900px; }}
    .stat {{ border:1px solid rgba(255,255,255,.18); border-radius:8px; padding:14px; background:rgba(255,255,255,.08); }}
    .stat strong {{ display:block; color:#fff; font-size:22px; }}
    .stat span {{ color:#d4e6df; font-size:13px; }}
    section {{ padding:68px 0; }}
    .section-head {{ max-width:820px; margin-bottom:28px; }}
    .section-head h2 {{ margin:0 0 10px; color:var(--deep); font-size:clamp(30px,4vw,44px); line-height:1.1; }}
    .section-head p {{ margin:0; color:var(--muted); }}
    .catalog {{ background:#fff; }}
    .catalog-grid {{ display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:16px; }}
    .catalog-group {{ border:1px solid var(--line); border-radius:8px; padding:18px; background:#fbfdfc; }}
    .catalog-group h3 {{ margin:0 0 12px; color:var(--green); font-size:19px; }}
    .catalog-links {{ display:flex; flex-wrap:wrap; gap:8px; }}
    .catalog-links a {{ border:1px solid #d7e4dd; border-radius:999px; padding:7px 10px; color:#173d34; background:#fff; font-weight:800; font-size:13px; }}
    .products {{ background:#f4f7f5; }}
    .product-list {{ display:grid; gap:26px; }}
    .product-card {{ display:grid; grid-template-columns:minmax(320px,.92fr) minmax(0,1.08fr); gap:28px; align-items:start; border:1px solid var(--line); border-radius:8px; background:#fff; padding:18px; box-shadow:0 18px 46px rgba(13,49,41,.08); scroll-margin-top:96px; }}
    .product-card:nth-child(even) .product-media {{ order:2; }}
    .product-media img {{ width:100%; aspect-ratio:4/3; object-fit:cover; border-radius:6px; border:1px solid #edf2ef; background:#eef3f1; }}
    .product-copy {{ padding:8px 4px; }}
    .category {{ display:inline-flex; color:#8d671f; font-weight:900; text-transform:uppercase; letter-spacing:.08em; font-size:12px; }}
    .product-copy h3 {{ margin:8px 0 4px; color:var(--deep); font-size:clamp(26px,3vw,38px); line-height:1.1; }}
    .subtitle {{ margin:0 0 14px; color:var(--green); font-size:18px; font-weight:800; }}
    .feature-list {{ display:flex; flex-wrap:wrap; gap:8px; margin:16px 0 20px; }}
    .feature-list span {{ border:1px solid #d8e4df; border-radius:999px; padding:7px 10px; background:#f8fbfa; font-size:13px; font-weight:800; color:#183c34; }}
    .detail-grid {{ display:grid; grid-template-columns:.8fr 1.2fr; gap:18px; margin:18px 0; }}
    .detail-grid h4 {{ margin:0 0 8px; color:var(--deep); }}
    ul {{ margin:0; padding-left:18px; }}
    .spec-table {{ width:100%; border-collapse:collapse; font-size:14px; overflow:hidden; border-radius:6px; }}
    .spec-table th, .spec-table td {{ padding:8px 10px; border:1px solid #e0e9e5; text-align:left; vertical-align:top; }}
    .spec-table th {{ width:42%; background:#f3f7f5; color:#244139; }}
    .mini-cta {{ display:inline-flex; align-items:center; justify-content:center; min-height:40px; border-radius:6px; padding:9px 14px; background:var(--green); color:#fff; font-weight:900; }}
    .process {{ background:#fff; }}
    .process-grid {{ display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:14px; }}
    .process-card {{ border-left:3px solid var(--gold); background:#f7faf8; padding:18px; border-radius:6px; }}
    .process-card strong {{ display:block; color:var(--deep); margin-bottom:6px; }}
    .contact {{ color:#fff; background:linear-gradient(120deg,#0b2f27,#10201c); }}
    .contact-grid {{ display:grid; grid-template-columns:1.15fr .85fr; gap:30px; align-items:center; }}
    .contact h2 {{ margin:0 0 12px; font-size:clamp(32px,4vw,48px); line-height:1.08; }}
    .contact p {{ color:#dceee8; margin:0 0 20px; }}
    .contact-box {{ border:1px solid rgba(255,255,255,.18); background:rgba(255,255,255,.08); border-radius:8px; padding:22px; }}
    .contact-box strong {{ display:block; color:#f2c96d; margin-top:10px; }}
    footer {{ padding:28px 0; color:#dcebe6; background:#071b17; font-size:14px; }}
    .wa-fixed {{ position:fixed; right:18px; bottom:18px; z-index:50; display:flex; align-items:center; justify-content:center; width:58px; height:58px; border-radius:50%; color:#fff; background:#1faa59; font-weight:900; box-shadow:0 10px 26px rgba(0,0,0,.24); }}
    @media (max-width:980px) {{ nav a {{ display:none; }} .hero-stats,.catalog-grid,.process-grid,.contact-grid {{ grid-template-columns:1fr 1fr; }} .product-card,.product-card:nth-child(even) .product-media {{ grid-template-columns:1fr; order:initial; }} .detail-grid {{ grid-template-columns:1fr; }} }}
    @media (max-width:640px) {{ main,section,header,footer {{ max-width:100vw; overflow-x:hidden; }} .wrap {{ width:calc(100vw - 32px); max-width:calc(100vw - 32px); overflow:hidden; }} .head {{ min-height:66px; gap:10px; }} .brand {{ min-width:0; }} .brand img {{ width:46px; height:46px; }} .brand span {{ font-size:16px; }} .brand small {{ font-size:11px; }} .lang {{ width:64px; }} h1 {{ font-size:32px; line-height:1.1; max-width:100%; overflow-wrap:break-word; white-space:normal; }} .hero {{ overflow:hidden; }} .hero .wrap {{ min-height:auto; padding:58px 0 64px; }} .hero p,.section-head p,.product-copy p {{ width:100%; max-width:100%; font-size:16px; overflow-wrap:break-word; white-space:normal; }} .cta-row {{ display:grid; grid-template-columns:1fr; }} .btn {{ width:100%; text-align:center; white-space:normal; }} .hero-stats,.catalog-grid,.process-grid,.contact-grid {{ grid-template-columns:1fr; }} .product-card {{ padding:12px; }} }}
  </style>
  <script type="application/ld+json">
  {{
    "@context":"https://schema.org",
    "@graph":[
      {{"@type":"Organization","name":"NJ GROUP YEŞİL DÖNÜŞÜM TEKNOLOJİ SANAYİ VE DIŞ TİCARET LİMİTED ŞİRKETİ","url":"https://njgrup.com","telephone":"+90 535 572 7525","address":{{"@type":"PostalAddress","addressLocality":"İstanbul","addressCountry":"TR"}}}},
{schema_products}
    ]
  }}
  </script>
</head>
<body>
  <header>
    <div class="wrap head">
      <a class="brand" href="index.html">
        <img src="assets/nj-logo-mark.svg" alt="NJ GROUP">
        <span>NJ GROUP<small>Gıda Makineleri Showroom</small></span>
      </a>
      <nav>
        <a href="index.html#home">Home</a>
        <a href="index.html#production">Production</a>
        <a href="index.html#trade">Trade</a>
        <a href="index.html#services">Services</a>
        <a href="#contact">Contact</a>
        <select class="lang" aria-label="Language">
          <option>TR</option><option>EN</option><option>中文</option><option>FR</option><option>DE</option>
        </select>
      </nav>
    </div>
  </header>

  <main>
    <section class="hero">
      <div class="wrap">
        <div class="eyebrow">NJ GROUP Food Machinery</div>
        <h1><span>Endüstriyel</span><span>gıda makineleri</span></h1>
        <p>Sebze, et, hamur ve makarna.<br>Paketleme, filizlendirme ve pişirme.<br>Tüm makineleri tek sayfada inceleyin.</p>
        <div class="cta-row">
          <a class="btn gold" href="#catalog">Makineleri İncele</a>
          <a class="btn light" href="{WA}?text=Merhaba%20NJ%20GROUP,%20g%C4%B1da%20makineleri%20i%C3%A7in%20teklif%20almak%20istiyorum.">WhatsApp ile teklif al</a>
        </div>
        <div class="hero-stats">
          <div class="stat"><strong>14</strong><span>net ürün grubu</span></div>
          <div class="stat"><strong>304</strong><span>paslanmaz çelik seçenekleri</span></div>
          <div class="stat"><strong>TR</strong><span>Türkiye pazarına uygun sunum</span></div>
          <div class="stat"><strong>2018</strong><span>NJ GROUP işletme vizyonu</span></div>
        </div>
      </div>
    </section>

    <section id="catalog" class="catalog">
      <div class="wrap">
        <div class="section-head">
          <h2>Doğru makineyi hızlı bulun</h2>
          <p>Eski dağınık ürün listesi kaldırıldı. Aşağıdaki katalog yalnızca yeni NJ GROUP materyallerine göre düzenlenen, görseli ve açıklaması eşleşen makineleri gösterir.</p>
        </div>
        <div class="catalog-grid">
{directory}
        </div>
      </div>
    </section>

    <section id="machines" class="products">
      <div class="wrap">
        <div class="section-head">
          <h2>Makine tanıtımları</h2>
          <p>Her makine görseli, adı ve açıklaması aynı ürün grubuna aittir. Kapasite, ölçü ve enerji değerleri proje koşullarına göre son teklif aşamasında teyit edilir.</p>
        </div>
        <div class="product-list">
{cards}
        </div>
      </div>
    </section>

    <section class="process">
      <div class="wrap">
        <div class="section-head">
          <h2>NJ GROUP proje yaklaşımı</h2>
          <p>Gıda makinesi satışında sadece ürün listesi değil, doğru kapasite, hijyen standardı, yerleşim ve satış sonrası destek birlikte değerlendirilir.</p>
        </div>
        <div class="process-grid">
          <div class="process-card"><strong>1. İhtiyaç analizi</strong>Ürün tipi, günlük üretim hedefi ve çalışma alanı birlikte netleştirilir.</div>
          <div class="process-card"><strong>2. Makine seçimi</strong>Kapasite, malzeme, enerji ve bakım koşullarına göre uygun model hazırlanır.</div>
          <div class="process-card"><strong>3. Teklif ve teslimat</strong>Makine, aksesuar, yedek parça ve lojistik detayları tek teklifte düzenlenir.</div>
          <div class="process-card"><strong>4. Kurulum desteği</strong>Kullanım, temizlik, bakım ve satış sonrası destek planı oluşturulur.</div>
        </div>
      </div>
    </section>

    <section id="contact" class="contact">
      <div class="wrap contact-grid">
        <div>
          <div class="eyebrow">Project Quote</div>
          <h2>Gıda makinesi projeniz için NJ GROUP ile görüşün</h2>
          <p>Merkezi mutfak, restoran zinciri, yemek fabrikası, sebze işleme veya paketleme hattı için ihtiyacınızı paylaşın; uygun makine grubunu ve teklif sürecini birlikte netleştirelim.</p>
          <a class="btn gold" href="{WA}?text=Merhaba%20NJ%20GROUP,%20g%C4%B1da%20makinesi%20projem%20i%C3%A7in%20g%C3%B6r%C3%BC%C5%9Fmek%20istiyorum.">WhatsApp ile iletişim</a>
        </div>
        <div class="contact-box">
          <span>Telefon / WhatsApp</span>
          <strong>+90 535 572 7525</strong>
          <span>E-posta</span>
          <strong>info@njgrup.com</strong>
          <span>Web</span>
          <strong>www.njgrup.com</strong>
        </div>
      </div>
    </section>
  </main>

  <footer>
    <div class="wrap">© 2018 NJ GROUP · Gıda Makineleri · İstanbul, Türkiye</div>
  </footer>
  <a class="wa-fixed" href="{WA}?text=Merhaba%20NJ%20GROUP,%20g%C4%B1da%20makineleri%20hakk%C4%B1nda%20bilgi%20almak%20istiyorum." aria-label="WhatsApp">WA</a>
  <!-- Cloudflare Web Analytics --><script defer src="https://static.cloudflareinsights.com/beacon.min.js" data-cf-beacon='{{"token": "48d5c39378e14316b6745a5be6f213bb"}}'></script><!-- End Cloudflare Web Analytics -->
</body>
</html>
"""


def redirect_page(target: str, label: str = "NJ GROUP Gıda Makineleri") -> str:
    return f"""<!doctype html>
<html lang="tr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{label} | NJ GROUP</title>
  <meta name="robots" content="noindex, follow">
  <link rel="canonical" href="https://njgrup.com/gida-makinalari.html">
  <meta http-equiv="refresh" content="0; url={target}">
  <script>
    var target = '{target.split('#')[0]}' + window.location.search + '{('#' + target.split('#', 1)[1]) if '#' in target else ''}';
    window.location.replace(target);
  </script>
  <style>body{{margin:0;min-height:100vh;display:grid;place-items:center;font-family:Arial,Helvetica,sans-serif;background:#0b2f27;color:#fff}}a{{color:#f2c96d;font-weight:800}}</style>
</head>
<body>
  <p>Bu içerik yeni NJ GROUP gıda makineleri showroom sayfasına taşındı: <a href="{target}">gida-makinalari.html</a></p>
</body>
</html>
"""


(ROOT / "gida-makinalari.html").write_text(html, encoding="utf-8", newline="\n")

redirect_targets = {
    "kivora-gida-makineleri.html": "gida-makinalari.html",
    "endustriyel-mutfak-ekipmanlari.html": "gida-makinalari.html",
    "merkezi-mutfak-ekipmanlari.html": "gida-makinalari.html",
    "gida-isleme-makinalari.html": "gida-makinalari.html",
    "sebze-yikama-makinesi.html": "gida-makinalari.html#sebze-yikama-makinesi",
    "sebze-kesme-makinesi.html": "gida-makinalari.html#cift-kafa-sebze-dograma-makinesi",
    "patates-soyma-makinesi.html": "gida-makinalari.html#endustriyel-sebze-soyma-makinesi",
    "et-kesme-makinesi.html": "gida-makinalari.html#cift-kafa-et-dograma-makinesi",
    "vakum-paketleme-makinesi.html": "gida-makinalari.html#cift-hazneli-vakumlu-paketleme-makinesi",
}

for city_page in ROOT.glob("*-gida-makinalari.html"):
    redirect_targets[city_page.name] = "gida-makinalari.html"
for city_page in ROOT.glob("*-endustriyel-mutfak-ekipmanlari.html"):
    redirect_targets[city_page.name] = "gida-makinalari.html"
for city_page in ROOT.glob("*-merkezi-mutfak-ekipmanlari.html"):
    redirect_targets[city_page.name] = "gida-makinalari.html"

for name, target in redirect_targets.items():
    (ROOT / name).write_text(redirect_page(target), encoding="utf-8", newline="\n")

sitemap_urls = [
    "https://njgrup.com/",
    "https://njgrup.com/eko-donusum.html",
    "https://njgrup.com/endustriyel-makine.html",
    "https://njgrup.com/gida-makinalari.html",
    "https://njgrup.com/yapi-hirdavat.html",
    "https://njgrup.com/dijital-pazarlama.html",
    "https://njgrup.com/fuar-organizasyon.html",
    "https://njgrup.com/turkiye-rejenere-kaucuk-yatirim-plani.html",
]
sitemap = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">\n"
sitemap += "\n".join(f"  <url><loc>{url}</loc></url>" for url in sitemap_urls)
sitemap += "\n</urlset>\n"
(ROOT / "sitemap.xml").write_text(sitemap, encoding="utf-8", newline="\n")

print(f"Generated gida-makinalari.html with {len(products)} products")
print(f"Updated {len(redirect_targets)} redirect pages")
