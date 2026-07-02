from pathlib import Path


machines = [
    ("Hamur ve Unlu Mamuller", [
        "El Yapımı Tip Bao Makinesi", "Çok Fonksiyonlu Bao Makinesi", "El Yapımı Tip Mantı Makinesi",
        "Wonton Makinesi", "Mantou Makinesi", "Erişte Makinesi", "Bıçak Kesim Erişte Makinesi",
        "Lamian Makinesi", "Mantı Hamuru Açma Makinesi", "Liangpi Makinesi", "Pirinç Eriştesi Makinesi",
    ]),
    ("Soya ve Bitkisel Protein", [
        "Kompakt Tofu Makinesi", "Fabrika Tipi Tofu Üretim Hattı", "Tofu Derisi Makinesi",
        "Fasulye Filizi Makinesi", "Soya Ürünleri Yardımcı Ekipmanları", "Soya Sütü Makinesi",
    ]),
    ("Sebze Hazırlama", [
        "Çok Fonksiyonlu Sebze Kesme Makinesi", "Yaprak Sebze Yıkama Makinesi",
        "Kök Sebze Soyma Makinesi", "Sebze Kurutma Makinesi",
    ]),
    ("Et İşleme", [
        "Kase Kesici / Parçalayıcı", "Et Kıyma Makinesi", "Et Şerit ve Dilim Kesme Makinesi",
        "Pişmiş Et Dilimleme Makinesi", "Et Küp Doğrama Makinesi", "Kemik Testere Makinesi",
        "Kaburga Doğrama Makinesi", "Koyun Eti Dilimleme Makinesi", "Dana Zarı Soyma Makinesi",
        "Tavuk ve Ördek Blok Kesme Makinesi", "Köfte Makinesi",
    ]),
    ("Yardımcı Mutfak Ekipmanları", [
        "Hamur Mikseri", "Hamur Yoğurma Makinesi", "Erişte Karıştırma Makinesi", "Mayalama Kabini",
        "Buhar Dolabı / Buhar Odası", "Hamur Yıkama Makinesi", "Ceketli Pişirme Kazanı",
        "Elektrikli Izgara", "Dolgu Karıştırma Makinesi", "Bulaşık Yıkama Makinesi",
        "Buhar Jeneratörü", "Pirinç Öğütme Makinesi", "Paketleme / Kapama Makinesi",
    ]),
]

images = [
    "assets/kivora-bun-line.jpg",
    "assets/kivora-dumpling-line.jpg",
    "assets/kivora-noodle-line.jpg",
    "assets/kivora-source-machine-18.jpg",
    "assets/kivora-source-machine-33.jpg",
    "assets/kivora-source-machine-42.jpg",
]


def slug(text: str) -> str:
    table = str.maketrans("çğıöşüÇĞİÖŞÜ/", "cgiosuCGIOSU-")
    out = text.translate(table).lower()
    return "-".join("".join(ch if ch.isalnum() else " " for ch in out).split())


flat = [(cat, name) for cat, names in machines for name in names]

directory_html = "\n".join(
    f"""        <div class="directory-col">
          <h3>{cat}</h3>
          <ul>
{chr(10).join(f'            <li><a href="#{slug(name)}">{name}</a></li>' for name in names)}
          </ul>
        </div>"""
    for cat, names in machines
)

cards_html = "\n".join(
    f"""        <article class="machine-card" id="{slug(name)}">
          <img src="{images[i % len(images)]}" alt="NJ GROUP {name} İstanbul" loading="lazy">
          <div>
            <span>{cat}</span>
            <h3>{name}</h3>
            <p>{name}, gıda üretimi, merkezi mutfak, restoran zinciri ve yemek fabrikası projeleri için NJ GROUP tarafından Türkiye pazarına sunulan profesyonel ekipman grubudur.</p>
            <ul>
              <li>İstanbul showroom ve proje görüşmesi</li>
              <li>Kapasiteye göre makine seçimi ve fiyat teklifi</li>
              <li>Kurulum, yedek parça ve satış sonrası destek</li>
            </ul>
            <a class="mini-cta" href="https://wa.me/905355727525?text=Merhaba%20NJ%20GROUP,%20{name.replace(' ', '%20')}%20hakk%C4%B1nda%20bilgi%20ve%20fiyat%20almak%20istiyorum.">WhatsApp ile fiyat iste</a>
          </div>
        </article>"""
    for i, (cat, name) in enumerate(flat)
)

schema_items = ",\n".join(
    f'      {{"@type":"Product","name":"{name}","brand":{{"@type":"Brand","name":"KIVORA"}},"category":"{cat}","areaServed":"Türkiye","url":"https://njgrup.com/kivora-gida-makineleri.html#{slug(name)}"}}'
    for cat, name in flat
)

html = f"""<!doctype html>
<html lang="tr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>KIVORA Gıda Makineleri | NJ GROUP Endüstriyel Mutfak Ekipmanları</title>
  <meta name="description" content="KIVORA gıda makineleri, endüstriyel mutfak ekipmanları, sebze yıkama, sebze kesme, et işleme, hamur, tofu ve merkezi mutfak çözümleri. NJ GROUP İstanbul.">
  <link rel="canonical" href="https://njgrup.com/kivora-gida-makineleri.html">
  <style>
    :root {{ --green:#0f3d31; --deep:#06271f; --gold:#d6a43a; --ink:#0b1f1a; --muted:#5c6f68; --line:#d9e3df; --soft:#f4f8f6; }}
    * {{ box-sizing:border-box; }}
    body {{ margin:0; font-family:Arial, Helvetica, sans-serif; color:var(--ink); background:#fff; line-height:1.6; }}
    a {{ color:inherit; }}
    .wrap {{ width:min(1180px, calc(100% - 32px)); margin:auto; }}
    header {{ position:sticky; top:0; z-index:20; background:var(--green); color:#fff; box-shadow:0 4px 18px rgba(0,0,0,.12); }}
    .head {{ min-height:72px; display:flex; align-items:center; justify-content:space-between; gap:22px; }}
    .brand {{ display:flex; align-items:center; gap:12px; text-decoration:none; font-weight:800; letter-spacing:.3px; }}
    .brand img {{ width:92px; height:auto; background:#fff; border-radius:4px; padding:6px; }}
    nav {{ display:flex; gap:18px; align-items:center; font-size:14px; font-weight:700; }}
    nav a {{ text-decoration:none; opacity:.94; }}
    .hero {{ background:linear-gradient(90deg,rgba(6,39,31,.92),rgba(15,61,49,.72)), url('assets/kivora-dumpling-machine.jpg') center/cover; color:#fff; }}
    .hero .wrap {{ min-height:560px; display:grid; align-content:center; padding:72px 0; max-width:1180px; }}
    .eyebrow {{ color:#ffd983; font-weight:800; text-transform:uppercase; font-size:13px; letter-spacing:.08em; }}
    h1 {{ font-size:clamp(38px, 6vw, 72px); line-height:1.02; margin:14px 0 18px; max-width:920px; }}
    .hero p {{ font-size:20px; max-width:760px; margin:0 0 28px; }}
    .cta-row {{ display:flex; flex-wrap:wrap; gap:14px; }}
    .btn {{ display:inline-flex; align-items:center; justify-content:center; min-height:46px; padding:12px 20px; border-radius:6px; text-decoration:none; font-weight:800; }}
    .btn.gold {{ background:var(--gold); color:#1a1609; }}
    .btn.light {{ border:1px solid rgba(255,255,255,.55); color:#fff; }}
    section {{ padding:64px 0; }}
    .section-head {{ max-width:850px; margin-bottom:28px; }}
    .section-head h2 {{ font-size:34px; line-height:1.15; margin:0 0 10px; color:var(--deep); }}
    .section-head p {{ margin:0; color:var(--muted); }}
    .directory {{ background:var(--soft); }}
    .directory-grid {{ display:grid; grid-template-columns:repeat(5, 1fr); gap:14px; }}
    .directory-col {{ background:#fff; border:1px solid var(--line); border-radius:8px; padding:18px; }}
    .directory-col h3 {{ margin:0 0 12px; color:var(--green); font-size:18px; }}
    .directory-col ul {{ list-style:none; margin:0; padding:0; display:grid; gap:8px; }}
    .directory-col a {{ font-weight:700; color:#0a362c; }}
    .cards {{ display:grid; gap:18px; }}
    .machine-card {{ display:grid; grid-template-columns:260px 1fr; gap:22px; border:1px solid var(--line); border-radius:8px; padding:16px; background:#fff; scroll-margin-top:90px; }}
    .machine-card img {{ width:100%; height:180px; object-fit:cover; border-radius:6px; background:#edf2f0; }}
    .machine-card span {{ color:var(--gold); font-weight:800; font-size:13px; text-transform:uppercase; }}
    .machine-card h3 {{ margin:4px 0 8px; font-size:24px; color:var(--deep); }}
    .machine-card p {{ margin:0 0 10px; color:#31443d; }}
    .machine-card ul {{ margin:0 0 14px; padding-left:20px; }}
    .mini-cta {{ display:inline-flex; align-items:center; min-height:38px; padding:8px 14px; border-radius:6px; background:var(--green); color:#fff; text-decoration:none; font-weight:800; }}
    .contact {{ background:var(--green); color:#fff; }}
    .contact-grid {{ display:grid; grid-template-columns:1.2fr .8fr; gap:28px; align-items:center; }}
    .contact h2 {{ color:#fff; font-size:42px; line-height:1.1; margin:0 0 14px; }}
    .contact p {{ margin:0 0 18px; color:#d8eee7; }}
    .contact-box {{ background:rgba(255,255,255,.08); border:1px solid rgba(255,255,255,.2); border-radius:8px; padding:22px; }}
    .contact-box strong {{ display:block; margin-top:10px; color:#ffd983; }}
    footer {{ background:var(--deep); color:#dcebe6; padding:28px 0; font-size:14px; }}
    .wa-fixed {{ position:fixed; right:18px; bottom:18px; z-index:30; background:#1faa59; color:#fff; width:58px; height:58px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-weight:900; text-decoration:none; box-shadow:0 8px 22px rgba(0,0,0,.22); }}
    @media (max-width:980px) {{ nav {{ display:none; }} .directory-grid {{ grid-template-columns:repeat(2,1fr); }} .machine-card {{ grid-template-columns:1fr; }} .contact-grid {{ grid-template-columns:1fr; }} }}
    @media (max-width:640px) {{ .directory-grid {{ grid-template-columns:1fr; }} h1 {{ font-size:38px; }} .hero .wrap {{ min-height:500px; }} }}
  </style>
  <script type="application/ld+json">
  {{
    "@context":"https://schema.org",
    "@graph":[
      {{"@type":"Organization","name":"NJ GROUP YEŞİL DÖNÜŞÜM TEKNOLOJİ SANAYİ VE DIŞ TİCARET LTD. ŞTİ.","url":"https://njgrup.com","telephone":"+90 535 572 7525","address":{{"@type":"PostalAddress","streetAddress":"İstoç 34. Ada No:82-84","addressLocality":"Bağcılar","addressRegion":"İstanbul","addressCountry":"TR"}}}},
      {{"@type":"Brand","name":"KIVORA","url":"https://njgrup.com/kivora-gida-makineleri.html"}},
{schema_items}
    ]
  }}
  </script>
</head>
<body>
  <header>
    <div class="wrap head">
      <a class="brand" href="index.html"><img src="assets/kivora-logo-transparent.png" alt="KIVORA NJ GROUP gıda makineleri logosu"><span>KIVORA<br><small>NJ GROUP GIDA MAKİNELERİ</small></span></a>
      <nav>
        <a href="#katalog">Katalog</a>
        <a href="#makineler">Makineler</a>
        <a href="gida-makinalari.html">Gıda Makinaları</a>
        <a href="#iletisim">İletişim</a>
      </nav>
    </div>
  </header>

  <main>
    <section class="hero">
      <div class="wrap">
        <div class="eyebrow">KIVORA Gıda Makineleri</div>
        <h1>Türkiye için endüstriyel mutfak ve gıda üretim makineleri</h1>
        <p>NJ GROUP; merkezi mutfak, yemek fabrikası, restoran zinciri, sebze hazırlama, et işleme, hamur işi, tofu ve paketleme projeleri için makine seçimi, teklif, kurulum ve servis desteği sağlar.</p>
        <div class="cta-row">
          <a class="btn gold" href="https://wa.me/905355727525?text=Merhaba%20NJ%20GROUP,%20g%C4%B1da%20makineleri%20i%C3%A7in%20fiyat%20ve%20proje%20g%C3%B6r%C3%BC%C5%9Fmesi%20istiyorum.">WhatsApp ile teklif al</a>
          <a class="btn light" href="tel:+905355727525">+90 535 572 7525</a>
        </div>
      </div>
    </section>

    <section id="katalog" class="directory">
      <div class="wrap">
        <div class="section-head">
          <h2>KIVORA tam ekipman kataloğu</h2>
          <p>Aşağıdaki tüm ürün adları Türkiye Google aramaları ve Google Maps görünürlüğü için Türkçe hazırlanmıştır. Her makine için günlük tanıtım, Google Post, reklam metni ve WhatsApp satış mesajı üretilebilir.</p>
        </div>
        <div class="directory-grid">
{directory_html}
        </div>
      </div>
    </section>

    <section id="makineler">
      <div class="wrap">
        <div class="section-head">
          <h2>Tanıtıma hazır makine sayfaları</h2>
          <p>Her makine, müşterinin ihtiyacına göre kapasite, ölçü, enerji, malzeme ve teslimat koşulları netleştirilerek tekliflendirilir.</p>
        </div>
        <div class="cards">
{cards_html}
        </div>
      </div>
    </section>

    <section id="iletisim" class="contact">
      <div class="wrap contact-grid">
        <div>
          <h2>Gıda makinesi projeniz için NJ GROUP ile görüşün</h2>
          <p>İstanbul İstoç showroom, ürün numunesi, kapasite planlaması, makine seçimi ve fiyat teklifi için doğrudan WhatsApp veya telefonla ulaşabilirsiniz.</p>
          <div class="cta-row">
            <a class="btn gold" href="https://wa.me/905355727525?text=Merhaba%20NJ%20GROUP,%20g%C4%B1da%20makinesi%20projem%20i%C3%A7in%20g%C3%B6r%C3%BC%C5%9Fmek%20istiyorum.">WhatsApp'tan yaz</a>
            <a class="btn light" href="tel:+905355727525">Hemen ara</a>
          </div>
        </div>
        <div class="contact-box">
          <strong>Firma</strong>
          NJ GROUP YEŞİL DÖNÜŞÜM TEKNOLOJİ SANAYİ VE DIŞ TİCARET LTD. ŞTİ.
          <strong>Adres</strong>
          İstoç 34. Ada No:82-84, Bağcılar / İstanbul, Türkiye
          <strong>Telefon / WhatsApp</strong>
          +90 535 572 7525
          <strong>Web</strong>
          www.njgrup.com
        </div>
      </div>
    </section>
  </main>

  <a class="wa-fixed" href="https://wa.me/905355727525?text=Merhaba%20NJ%20GROUP,%20g%C4%B1da%20makinesi%20hakk%C4%B1nda%20bilgi%20almak%20istiyorum." aria-label="WhatsApp">WA</a>
  <footer><div class="wrap">© 2018 NJ GROUP · KIVORA Gıda Makineleri · İstanbul, Türkiye</div></footer>
</body>
</html>
"""

Path("kivora-gida-makineleri.html").write_text(html, encoding="utf-8")
