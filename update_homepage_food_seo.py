from pathlib import Path

path = Path("index.html")
text = path.read_text(encoding="utf-8")

text = text.replace(
    '<meta name="description" content="NJ GROUP YE&#350;&#304;L D&#214;N&#220;&#350;&#220;M TEKNOLOJ&#304; SANAY&#304; VE DI&#350; T&#304;CARET L&#304;M&#304;TED &#350;&#304;RKET&#304;, &#199;in, T&#252;rkiye ve Avrupa aras&#305;nda end&#252;striyel ticaret ve pazar giri&#351; platformudur." />',
    '<meta name="description" content="NJ GROUP, İstanbul İstoç merkezli gıda makinaları, endüstriyel mutfak ekipmanları, merkezi mutfak, sebze yıkama, sebze kesme, patates soyma, et kesme ve vakum paketleme çözümleri sunar." />',
)
text = text.replace(
    "<title>NJ GROUP | Eurasia Industrial Trade Platform</title>",
    "<title>NJ GROUP | Gıda Makinaları ve Endüstriyel Mutfak Ekipmanları</title>",
)
text = text.replace(
    '<a href="endustriyel-makine.html">End&#252;striyel Makine</a>',
    '<a href="gida-makinalari.html">Gıda Makinaları</a>\n            <a href="endustriyel-makine.html">End&#252;striyel Makine</a>',
)
text = text.replace(
    '<a class="quick-card" href="#business"><strong data-i18n="quick1Title">Faaliyetler</strong><span data-i18n="quick1Copy">Alt&#305; ana i&#351; kolu ve detay hizmet sayfalar&#305;.</span></a>',
    '<a class="quick-card" href="gida-makinalari.html"><strong>Gıda Makinaları</strong><span>Endüstriyel mutfak, merkezi mutfak ve gıda işleme ekipmanları.</span></a>',
)

food_card = """        <a class="business-card" href="gida-makinalari.html">
          <div class="business-image" style="--img:url('assets/endustriyel-makine.jpg')"></div>
          <div class="business-content"><small>00</small><h3>Gıda Makinaları</h3><p>Endüstriyel mutfak ekipmanları, merkezi mutfak, sebze yıkama, sebze kesme, patates soyma, et kesme ve vakum paketleme makineleri.</p><span class="read-more">Detayları Gör</span></div>
        </a>
"""
if "gida-makinalari.html" in text and "<small>00</small><h3>Gıda Makinaları</h3>" not in text:
    text = text.replace('      <div class="business-grid">\n', '      <div class="business-grid">\n' + food_card, 1)

path.write_text(text, encoding="utf-8")
print("Homepage food SEO entry updated.")
