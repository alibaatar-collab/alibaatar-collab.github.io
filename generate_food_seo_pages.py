from pathlib import Path
import unicodedata

ROOT = Path(__file__).resolve().parent
SITE = "https://njgrup.com"
PHONE_DISPLAY = "+90 535 572 7525"
PHONE_TEL = "+905355727525"
WHATSAPP = "https://wa.me/905355727525"
ADDRESS = "İstoç 34. Ada No:82-84, Bağcılar / İstanbul, Türkiye"
COMPANY = "NJ GROUP YEŞİL DÖNÜŞÜM TEKNOLOJİ SANAYİ VE DIŞ TİCARET LTD. ŞTİ."

PRODUCTS = [
    ("Endüstriyel Mutfak Ekipmanları", "endustriyel-mutfak-ekipmanlari", "Restoran, otel, catering ve yemek fabrikaları için profesyonel endüstriyel mutfak ekipmanları."),
    ("Merkezi Mutfak Ekipmanları", "merkezi-mutfak-ekipmanlari", "Yüksek kapasiteli hazırlık, pişirme, soğutma ve paketleme süreçleri için merkezi mutfak çözümleri."),
    ("Sebze Yıkama Makinesi", "sebze-yikama-makinesi", "Sebze, meyve ve salata üretimi için hijyenik yıkama makineleri ve hazırlık hatları."),
    ("Sebze Kesme Makinesi", "sebze-kesme-makinesi", "Dilimleme, küp kesme, jülyen ve doğrama işlemleri için endüstriyel sebze kesme makineleri."),
    ("Patates Soyma Makinesi", "patates-soyma-makinesi", "Restoran, catering ve yemek fabrikaları için hızlı ve verimli patates soyma makineleri."),
    ("Et Kesme Makinesi", "et-kesme-makinesi", "Kasap, otel, restoran ve gıda üretim tesisleri için et kesme ve porsiyonlama çözümleri."),
    ("Vakum Paketleme Makinesi", "vakum-paketleme-makinesi", "Gıda raf ömrü, hijyen ve sevkiyat güvenliği için vakum paketleme makineleri."),
    ("Gıda İşleme Makinaları", "gida-isleme-makinalari", "Gıda hazırlık, işleme, üretim ve paketleme süreçleri için sanayi tipi makine çözümleri."),
]

CITIES = [
    "İstanbul", "Ankara", "İzmir", "Bursa", "Antalya", "Konya", "Gaziantep",
    "Adana", "Mersin", "Kayseri", "Kocaeli", "Sakarya", "Eskişehir",
    "Trabzon", "Diyarbakır",
]

CITY_TERMS = [
    ("Endüstriyel Mutfak Ekipmanları", "endustriyel-mutfak-ekipmanlari"),
    ("Merkezi Mutfak Ekipmanları", "merkezi-mutfak-ekipmanlari"),
    ("Gıda Makinaları", "gida-makinalari"),
]


def html_escape(value: str) -> str:
    return value.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def shell(title: str, description: str, canonical: str, body: str, schema: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html_escape(title)}</title>
  <meta name="description" content="{html_escape(description)}">
  <link rel="canonical" href="{canonical}">
  <meta name="robots" content="index, follow">
  <style>
    :root{{--forest:#173b36;--forest2:#20544a;--gold:#c8923e;--ink:#17211f;--muted:#5d6d68;--mist:#f2f6f4;--line:#d7e1dd}}
    *{{box-sizing:border-box}}body{{margin:0;color:var(--ink);font-family:Arial,'Noto Sans',sans-serif;line-height:1.65;background:#fff}}a{{color:inherit}}.shell{{width:min(1140px,calc(100% - 40px));margin:auto}}
    header{{position:sticky;top:0;z-index:5;background:#173b36;color:#fff;border-bottom:1px solid rgba(255,255,255,.12)}}.nav{{min-height:70px;display:flex;align-items:center;justify-content:space-between;gap:20px}}.logo{{font-weight:900;text-decoration:none;letter-spacing:.03em}}.navlinks{{display:flex;gap:18px;align-items:center;font-size:14px;font-weight:800}}.navlinks a{{text-decoration:none;color:#eff7f4}}
    .hero{{padding:92px 0 86px;color:#fff;background:linear-gradient(90deg,rgba(8,31,28,.96),rgba(8,31,28,.76)),url('assets/endustriyel-makine.jpg') center/cover no-repeat;border-bottom:5px solid var(--gold)}}.eyebrow{{margin:0 0 12px;color:#a8e4e1;font-size:13px;font-weight:900;text-transform:uppercase}}h1{{max-width:860px;margin:0;font-size:clamp(38px,5vw,66px);line-height:1.08}}.lead{{max-width:760px;margin:22px 0 0;font-size:20px;color:#edf7f3}}.actions{{display:flex;flex-wrap:wrap;gap:12px;margin-top:30px}}.btn{{display:inline-flex;align-items:center;justify-content:center;min-height:48px;padding:0 18px;border-radius:6px;background:var(--gold);color:#17211f;font-weight:900;text-decoration:none}}.btn.secondary{{background:rgba(255,255,255,.1);color:#fff;border:1px solid rgba(255,255,255,.35)}}
    section{{padding:76px 0}}section.mist{{background:var(--mist)}}h2{{margin:0 0 18px;color:var(--forest);font-size:clamp(28px,4vw,44px);line-height:1.16}}h3{{margin:0 0 8px;color:var(--forest)}}p{{margin:0 0 14px}}.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}}.card{{min-height:210px;padding:24px;border:1px solid var(--line);border-radius:6px;background:#fff}}.card a{{color:var(--forest);font-weight:900;text-decoration:none}}.muted{{color:var(--muted)}}.table{{overflow:auto;border:1px solid var(--line);border-radius:6px;background:#fff}}table{{width:100%;border-collapse:collapse;min-width:640px}}td,th{{padding:14px 16px;border-bottom:1px solid var(--line);text-align:left}}th{{background:var(--forest);color:#fff}}.contact{{display:grid;grid-template-columns:1fr 1fr;gap:22px;align-items:stretch}}iframe{{width:100%;min-height:320px;border:0;border-radius:6px}}footer{{padding:30px 0;color:#a8bbb4;background:#0b2622}}.whatsapp{{position:fixed;right:18px;bottom:18px;width:58px;height:58px;display:grid;place-items:center;border-radius:50%;background:#25d366;color:#fff;font-weight:900;text-decoration:none;box-shadow:0 12px 30px rgba(0,0,0,.2)}}
    @media(max-width:800px){{.navlinks{{display:none}}.grid,.contact{{grid-template-columns:1fr}}section{{padding:58px 0}}}}
  </style>
  <script type="application/ld+json">{schema}</script>
</head>
<body>
  <header><div class="shell nav"><a class="logo" href="index.html">NJ GROUP</a><nav class="navlinks"><a href="gida-makinalari.html">Gıda Makinaları</a><a href="#urunler">Ürünler</a><a href="#iletisim">İletişim</a><a href="{WHATSAPP}" target="_blank" rel="noopener">WhatsApp</a></nav></div></header>
  {body}
  <a class="whatsapp" href="{WHATSAPP}?text=G%C4%B1da%20makinalar%C4%B1%20hakk%C4%B1nda%20teklif%20almak%20istiyorum" target="_blank" rel="noopener" aria-label="WhatsApp">☎</a>
  <footer><div class="shell">© 2018 NJ GROUP · {PHONE_DISPLAY} · njgrup.com</div></footer>
</body>
</html>
"""


def schema(name: str, slug: str, description: str) -> str:
    return (
        '{"@context":"https://schema.org","@graph":['
        f'{{"@type":"Organization","name":"NJ GROUP","legalName":"{COMPANY}","url":"{SITE}","telephone":"{PHONE_TEL}","address":{{"@type":"PostalAddress","streetAddress":"İstoç 34. Ada No:82-84","addressLocality":"Bağcılar","addressRegion":"İstanbul","addressCountry":"TR"}}}},'
        f'{{"@type":"Product","name":"{name}","brand":{{"@type":"Brand","name":"NJ GROUP"}},"category":"FoodServiceEquipment","url":"{SITE}/{slug}.html","description":"{description}"}},'
        f'{{"@type":"FAQPage","mainEntity":[{{"@type":"Question","name":"{name} fiyatı nasıl belirlenir?","acceptedAnswer":{{"@type":"Answer","text":"Fiyat kapasite, model, paslanmaz kalite, otomasyon seviyesi ve teslimat kapsamına göre hazırlanır."}}}},{{"@type":"Question","name":"Türkiye geneline hizmet veriyor musunuz?","acceptedAnswer":{{"@type":"Answer","text":"NJ GROUP İstanbul İstoç merkezli olarak Türkiye genelinde proje, tedarik ve satış sonrası destek organize eder."}}}}]}}'
        ']}'
    )


def product_grid() -> str:
    return "\n".join(
        f'<article class="card"><h3><a href="{slug}.html">{name}</a></h3><p class="muted">{desc}</p></article>'
        for name, slug, desc in PRODUCTS
    )


def contact_section() -> str:
    return f"""<section id="iletisim">
  <div class="shell contact">
    <div>
      <p class="eyebrow">İletişim</p>
      <h2>Teklif ve proje görüşmesi için NJ GROUP ile iletişime geçin.</h2>
      <p>Adres: {ADDRESS}</p>
      <p>Telefon: <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p>
      <p>WhatsApp: <a href="{WHATSAPP}" target="_blank" rel="noopener">{PHONE_DISPLAY}</a></p>
      <div class="actions"><a class="btn" href="{WHATSAPP}" target="_blank" rel="noopener">WhatsApp ile Teklif Al</a><a class="btn secondary" href="tel:{PHONE_TEL}">Hemen Ara</a></div>
    </div>
    <iframe loading="lazy" allowfullscreen src="https://www.google.com/maps?q=NJ%20GROUP%20%C4%B0sto%C3%A7%2034.%20Ada%20No%3A82-84%20Ba%C4%9Fc%C4%B1lar%20%C4%B0stanbul&output=embed"></iframe>
  </div>
</section>"""


def write_hub() -> None:
    title = "Gıda Makinaları ve Endüstriyel Mutfak Ekipmanları | NJ GROUP"
    desc = "NJ GROUP İstanbul İstoç merkezli gıda makinaları, endüstriyel mutfak ekipmanları, merkezi mutfak, sebze yıkama, sebze kesme, patates soyma, et kesme ve vakum paketleme çözümleri."
    body = f"""<main>
  <section class="hero"><div class="shell"><p class="eyebrow">NJ GROUP · Gıda Makinaları</p><h1>Gıda Makinaları ve Endüstriyel Mutfak Ekipmanları</h1><p class="lead">Restoran, otel, catering firması, merkezi mutfak ve yemek fabrikaları için proje bazlı ekipman tedariki, kurulum ve satış sonrası destek.</p><div class="actions"><a class="btn" href="{WHATSAPP}" target="_blank" rel="noopener">WhatsApp ile Teklif Al</a><a class="btn secondary" href="#urunler">Ürünleri İncele</a></div></div></section>
  <section id="urunler"><div class="shell"><p class="eyebrow">Ürünler</p><h2>Aranan temel gıda makinaları ve mutfak ekipmanları</h2><div class="grid">{product_grid()}</div></div></section>
  <section class="mist"><div class="shell"><h2>Restoran, otel, catering ve yemek fabrikaları için tek iletişim noktası</h2><p class="muted">NJ GROUP, doğru makine seçimi, kapasite planlama, paslanmaz ekipman tedariki, kurulum ve satış sonrası destek süreçlerini birlikte değerlendirir. Amacımız müşterinin sadece ürün değil, çalışır bir üretim çözümü almasını sağlamaktır.</p></div></section>
  {contact_section()}
</main>"""
    (ROOT / "gida-makinalari.html").write_text(shell(title, desc, f"{SITE}/gida-makinalari.html", body, schema("Gıda Makinaları", "gida-makinalari", desc)), encoding="utf-8")


def write_product_pages() -> None:
    for name, slug, desc in PRODUCTS:
        title = f"{name} | İstanbul ve Türkiye Geneli | NJ GROUP"
        meta = f"{name} için NJ GROUP İstanbul İstoç merkezli proje, tedarik, kurulum ve satış sonrası destek sağlar. WhatsApp: {PHONE_DISPLAY}."
        body = f"""<main>
  <section class="hero"><div class="shell"><p class="eyebrow">NJ GROUP · {html_escape(name)}</p><h1>{html_escape(name)}</h1><p class="lead">{html_escape(desc)} Türkiye genelinde teklif ve proje desteği için WhatsApp üzerinden iletişime geçin.</p><div class="actions"><a class="btn" href="{WHATSAPP}?text={html_escape(name).replace(' ', '%20')}%20hakk%C4%B1nda%20teklif%20almak%20istiyorum" target="_blank" rel="noopener">WhatsApp ile Teklif Al</a><a class="btn secondary" href="tel:{PHONE_TEL}">Telefonla Ara</a></div></div></section>
  <section><div class="shell"><h2>{html_escape(name)} nedir?</h2><p class="muted">NJ GROUP, {html_escape(name)} alanında restoran, otel, merkezi mutfak, catering firması ve gıda üretim tesisleri için ürün seçimi, kapasite planlama ve tedarik desteği sunar.</p><div class="grid"><article class="card"><h3>Kullanım alanları</h3><p>Restoran, otel, catering, yemek fabrikası ve gıda üretim tesisi.</p></article><article class="card"><h3>Proje desteği</h3><p>Kapasite, ölçü, enerji ihtiyacı ve iş akışına göre uygun çözüm hazırlanır.</p></article><article class="card"><h3>Servis</h3><p>Kurulum, kullanıcı eğitimi, bakım ve yedek parça süreci proje bazında organize edilir.</p></article></div></div></section>
  <section class="mist"><div class="shell"><h2>Teknik bilgi</h2><div class="table"><table><tr><th>Alan</th><th>Değerlendirme</th></tr><tr><td>Kapasite</td><td>Saatlik veya günlük üretim ihtiyacına göre seçilir.</td></tr><tr><td>Malzeme</td><td>Gıda temasına uygun paslanmaz yüzeyler tercih edilir.</td></tr><tr><td>Enerji</td><td>Elektrik, gaz veya yardımcı ekipman ihtiyacı modele göre belirlenir.</td></tr><tr><td>Kurulum</td><td>Yerleşim, kullanım eğitimi ve satış sonrası destek planlanır.</td></tr></table></div></div></section>
  <section><div class="shell"><h2>Sık sorulan sorular</h2><div class="grid"><article class="card"><h3>Fiyat nasıl belirlenir?</h3><p>Kapasite, model, ölçü, otomasyon ve teslimat kapsamına göre hazırlanır.</p></article><article class="card"><h3>Türkiye geneline hizmet var mı?</h3><p>Evet, İstanbul İstoç merkezli olarak Türkiye genelinde destek verilir.</p></article><article class="card"><h3>Nasıl teklif alırım?</h3><p>WhatsApp üzerinden ürün, şehir, kapasite ve kullanım alanınızı gönderin.</p></article></div></div></section>
  {contact_section()}
</main>"""
        (ROOT / f"{slug}.html").write_text(shell(title, meta, f"{SITE}/{slug}.html", body, schema(name, slug, desc)), encoding="utf-8")


def city_slug(city: str) -> str:
    mapped = city.replace("İ", "I").replace("ı", "i")
    normalized = unicodedata.normalize("NFKD", mapped)
    ascii_only = normalized.encode("ascii", "ignore").decode("ascii")
    return ascii_only.lower().replace(" ", "-")


def write_city_pages() -> None:
    for city in CITIES:
        for term, term_slug in CITY_TERMS:
            slug = f"{city_slug(city)}-{term_slug}"
            title = f"{city} {term} | NJ GROUP"
            meta = f"{city} {term} arayan restoran, otel, catering ve yemek fabrikaları için NJ GROUP İstanbul İstoç merkezli tedarik ve proje desteği sağlar."
            body = f"""<main>
  <section class="hero"><div class="shell"><p class="eyebrow">NJ GROUP · {html_escape(city)}</p><h1>{html_escape(city)} {html_escape(term)}</h1><p class="lead">{html_escape(city)} bölgesinde {html_escape(term)} ihtiyacı olan restoran, otel, catering firması ve yemek fabrikaları için NJ GROUP ile iletişime geçin.</p><div class="actions"><a class="btn" href="{WHATSAPP}?text={html_escape(city).replace(' ', '%20')}%20{html_escape(term).replace(' ', '%20')}%20i%C3%A7in%20teklif%20istiyorum" target="_blank" rel="noopener">WhatsApp ile Teklif Al</a><a class="btn secondary" href="tel:{PHONE_TEL}">Hemen Ara</a></div></div></section>
  <section><div class="shell"><h2>{html_escape(city)} için gıda makinaları ve mutfak ekipmanları</h2><p class="muted">NJ GROUP, İstanbul İstoç merkezli yapısıyla {html_escape(city)} ve Türkiye geneline endüstriyel mutfak ekipmanları, merkezi mutfak ekipmanları ve gıda makinaları konusunda proje bazlı destek sunar.</p><div class="grid">{product_grid()}</div></div></section>
  {contact_section()}
</main>"""
            (ROOT / f"{slug}.html").write_text(shell(title, meta, f"{SITE}/{slug}.html", body, schema(f"{city} {term}", slug, meta)), encoding="utf-8")


def update_sitemap() -> None:
    urls = [
        "https://njgrup.com/",
        "https://njgrup.com/eko-donusum.html",
        "https://njgrup.com/endustriyel-makine.html",
        "https://njgrup.com/akilli-teknoloji.html",
        "https://njgrup.com/yapi-hirdavat.html",
        "https://njgrup.com/dijital-pazarlama.html",
        "https://njgrup.com/fuar-organizasyon.html",
        "https://njgrup.com/gida-makinalari.html",
    ]
    urls += [f"https://njgrup.com/{slug}.html" for _, slug, _ in PRODUCTS]
    urls += [f"https://njgrup.com/{city_slug(city)}-{term_slug}.html" for city in CITIES for _, term_slug in CITY_TERMS]
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    sitemap += "\n".join(f"  <url><loc>{url}</loc></url>" for url in urls)
    sitemap += "\n</urlset>\n"
    (ROOT / "sitemap.xml").write_text(sitemap, encoding="utf-8")


if __name__ == "__main__":
    write_hub()
    write_product_pages()
    write_city_pages()
    update_sitemap()
    print("Generated food machinery SEO pages and sitemap.")
