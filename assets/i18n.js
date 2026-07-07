(function () {
  const names = {
    eco: ["EKO DÖNÜŞÜM", "ECO TRANSFORMATION", "生态循环", "ÉCO-TRANSFORMATION", "ÖKO-TRANSFORMATION"],
    tech: ["AKILLI TEKNOLOJİ", "SMART TECHNOLOGY", "智能科技", "TECHNOLOGIE INTELLIGENTE", "INTELLIGENTE TECHNOLOGIE"],
    build: ["YAPI & HIRDAVAT", "BUILDING & HARDWARE", "建材与五金", "BÂTIMENT & QUINCAILLERIE", "BAU & HARDWARE"],
    machine: ["ENDÜSTRİYEL MAKİNE", "INDUSTRIAL MACHINERY", "工业机械", "MACHINES INDUSTRIELLES", "INDUSTRIEMASCHINEN"],
    digital: ["DİJİTAL PAZARLAMA", "DIGITAL MARKETING", "数字营销", "MARKETING DIGITAL", "DIGITALES MARKETING"],
    fair: ["FUAR & ORGANİZASYON", "FAIR & ORGANIZATION", "展会与组织服务", "SALONS & ORGANISATION", "MESSEN & ORGANISATION"]
  };

  const langs = ["tr", "en", "zh", "fr", "de"];
  const pick = (arr, lang) => arr[langs.indexOf(lang)] || arr[0];
  const original = { productPs: [], subCards: [] };

  const t = {
    tr: {
      navBusiness: "Faaliyetler", navStrengths: "Güçlerimiz", navAbout: "Hakkımızda", navContact: "İletişim",
      badge: "Türkiye · Europe · China", heroTitle: "Çin Üretimini Türkiye ve Avrupa ile <span>Buluşturuyoruz</span>",
      heroText: "NJGROUP, Türkiye merkezli, Çin ile Avrupa pazarlarını birbirine bağlayan yerelleştirilmiş bir endüstriyel operasyon platformudur. Pazar geliştirme, kanal yönetimi, marka operasyonları ve yerel hizmet çözümleri sunuyoruz.",
      heroCta1: "Faaliyet Alanları", heroCta2: "İletişime Geç", panelTitle: "Platform Yapısı",
      panelText: "Çin tedarik zinciri + Türkiye yerel operasyonu + Avrupa pazar bağlantıları.",
      stat1: "Alan", stat2: "Pazar", stat3: "Platform", businessTitle: "NJGROUP Ana Faaliyet Yapısı",
      businessSub: "Pazar girişi, kanal geliştirme, dijital pazarlama, showroom yönetimi, ticari organizasyonlar ve yerel operasyon hizmetlerini bir araya getiren bölgesel bir sanayi iş birliği platformu oluşturuyoruz.",
      enterPage: "Detay Sayfasına Gir", sliderHint: "Sağa sola kaydırarak NJGROUP faaliyet yapısını gezebilirsiniz.",
      alt: "Alt hizmetler", strengthsTitle: "Operasyon Gücümüz",
      strengthsSub: "NJGROUP, Çin üretimini Türkiye operasyonları ve Avrupa pazarı ile birleştiren bölgesel bir ticari ekosistem oluşturmaktadır.",
      strengthCoreKicker: "NJGROUP PLATFORM", strengthCoreTitle: "Çin - Türkiye - Avrupa arasında yerelleştirilmiş operasyon gücü",
      strengthCoreText: "Tedarik, pazar girişi, dijital satış, showroom, fuar ve satış sonrası destek süreçlerini tek platform altında birleştiriyoruz.",
      companyTitle: "NJGROUP YEŞİL DÖNÜŞÜM TEKNOLOJİ",
      companyText: "NJGROUP YEŞİL DÖNÜŞÜM TEKNOLOJİ SANAYİ VE DIŞ TİCARET LİMİTED ŞİRKETİ'nin merkezi İstanbul'daki İSTOÇ ticaret bölgesinde bulunmaktadır. Türkiye'nin stratejik konumu ve ticari avantajları sayesinde Çin tedarik zinciri entegrasyonu, Türkiye yerel kanal ağı, Avrupa pazar bağlantıları, dijital pazarlama sistemleri ve showroom hizmetleri sunuyoruz.",
      companyLine: "Biz sadece bir dış ticaret şirketi değiliz.", companyKicker: "NJGROUP COMPANY PROFILE", companyVisualTitle: "EURASIA INDUSTRIAL PLATFORM", companyVisualText: "China supply chain, Türkiye local operation and European market connection.", companyCards: ["İstanbul merkezli yerel ticari operasyon", "Çin, Türkiye ve Avrupa arasında köprü", "Sanayi, teknoloji, dijital ve organizasyon çözümleri"], aboutTitle: "Hakkımızda",
      aboutText: "NJGROUP'un temel amacı yalnızca ürün ithalatı ve ihracatı yapmak değildir. Ana hedefimiz, Çin üretiminin Türkiye ve Avrupa pazarlarında yerelleştirilmiş operasyon sistemini kurmaktır.",
      visionTitle: "Vizyonumuz ve Misyonumuz",
      visionText1: "Vizyonumuz, Çinli şirketlerin Türkiye ve Avrupa pazarına girişinde en güçlü yerelleştirilmiş endüstriyel operasyon platformlarından biri olmaktır.",
      visionText2: "Misyonumuz; Çin üretimini uluslararası pazarlara taşımak, güçlü yerel operasyon sistemleri oluşturmak, Çin - Türkiye - Avrupa iş birliklerini geliştirmek ve sürdürülebilir ticari değer üretmektir.",
      contactTitle: "NJGROUP ile İletişime Geçin", contactText: "İş birliği, tedarik, distribütörlük veya proje görüşmeleri için bize ulaşın.", email: "E-posta Gönder",
      footer: "© 2018 NJGROUP. Tüm hakları saklıdır. · "
    },
    en: {
      navBusiness: "Business Areas", navStrengths: "Strengths", navAbout: "About", navContact: "Contact",
      badge: "Türkiye · Europe · China", heroTitle: "Connecting Chinese Manufacturing with <span>Türkiye and Europe</span>",
      heroText: "NJGROUP is a Türkiye-based localized industrial operations platform connecting China with European markets. We provide market development, channel management, brand operations and local service solutions.",
      heroCta1: "Business Areas", heroCta2: "Contact Us", panelTitle: "Platform Structure",
      panelText: "China supply chain + Türkiye local operations + European market connections.",
      stat1: "Areas", stat2: "Markets", stat3: "Platform", businessTitle: "NJGROUP Core Business Areas",
      businessSub: "We build a regional industrial collaboration platform combining market entry, channel development, digital marketing, showroom management, commercial events and local operations.",
      enterPage: "Open Detail Page", sliderHint: "Swipe left or right to explore the NJGROUP business structure.",
      alt: "Sub services", strengthsTitle: "Operating Strengths",
      strengthsSub: "NJGROUP creates a regional commercial ecosystem that connects Chinese manufacturing with Türkiye operations and the European market.",
      strengthCoreKicker: "NJGROUP PLATFORM", strengthCoreTitle: "Localized operational power between China, Türkiye and Europe",
      strengthCoreText: "We combine sourcing, market entry, digital sales, showroom, fairs and after-sales support under one platform.",
      companyTitle: "NJGROUP GREEN TRANSFORMATION TECHNOLOGY",
      companyText: "NJGROUP YEŞİL DÖNÜŞÜM TEKNOLOJİ SANAYİ VE DIŞ TİCARET LİMİTED ŞİRKETİ is headquartered in the İSTOÇ trade district of Istanbul. With Türkiye's strategic location and commercial advantages, we provide China supply chain integration, Türkiye local channels, European market connections, digital marketing systems and showroom services.",
      companyLine: "We are more than a foreign trade company.", companyKicker: "NJGROUP COMPANY PROFILE", companyVisualTitle: "EURASIA INDUSTRIAL PLATFORM", companyVisualText: "China supply chain, Türkiye local operation and European market connection.", companyCards: ["Istanbul-based local commercial operation", "A bridge between China, Türkiye and Europe", "Industrial, technology, digital and event solutions"], aboutTitle: "About Us",
      aboutText: "NJGROUP's purpose is not limited to product import and export. Our main goal is to establish a localized operating system for Chinese manufacturing in Türkiye and European markets.",
      visionTitle: "Vision and Mission",
      visionText1: "Our vision is to become one of the strongest localized industrial operation platforms for Chinese companies entering Türkiye and Europe.",
      visionText2: "Our mission is to bring Chinese manufacturing to international markets, build strong local operation systems, develop China - Türkiye - Europe cooperation and create sustainable commercial value.",
      contactTitle: "Contact NJGROUP", contactText: "Reach us for cooperation, sourcing, distribution or project discussions.", email: "Send Email",
      footer: "© 2018 NJGROUP. All rights reserved. · "
    },
    zh: {
      navBusiness: "业务板块", navStrengths: "核心优势", navAbout: "关于我们", navContact: "联系我们",
      badge: "土耳其 · 欧洲 · 中国", heroTitle: "连接中国制造与<span>土耳其及欧洲市场</span>",
      heroText: "NJGROUP 是一家位于土耳其的本地化工业运营平台，连接中国与欧洲市场，提供市场开发、渠道管理、品牌运营和本地服务解决方案。",
      heroCta1: "业务板块", heroCta2: "联系我们", panelTitle: "平台结构",
      panelText: "中国供应链 + 土耳其本地运营 + 欧洲市场连接。",
      stat1: "板块", stat2: "市场", stat3: "平台", businessTitle: "NJGROUP 核心业务板块",
      businessSub: "我们整合市场进入、渠道开发、数字营销、展厅管理、商务活动和本地运营服务，打造区域性工业合作平台。",
      enterPage: "进入详情页面", sliderHint: "左右滑动查看 NJGROUP 核心业务结构。",
      alt: "查看细分业务", strengthsTitle: "核心优势",
      strengthsSub: "NJGROUP 将中国制造、土耳其本地运营和欧洲市场连接起来，形成区域化商业生态。",
      strengthCoreKicker: "NJGROUP 平台", strengthCoreTitle: "连接中国、土耳其与欧洲的本地化运营能力",
      strengthCoreText: "我们把供应链、市场进入、数字销售、展厅、展会和售后支持整合在同一个平台中。",
      companyTitle: "NJGROUP 绿色转型科技",
      companyText: "NJGROUP YEŞİL DÖNÜŞÜM TEKNOLOJİ SANAYİ VE DIŞ TİCARET LİMİTED ŞİRKETİ 总部位于伊斯坦布尔 İSTOÇ 商贸区。依托土耳其的战略位置和商业优势，我们提供中国供应链整合、土耳其本地渠道、欧洲市场连接、数字营销系统和展厅服务。",
      companyLine: "我们不只是一家外贸公司。", companyKicker: "NJGROUP 公司介绍", companyVisualTitle: "欧亚工业平台", companyVisualText: "中国供应链、土耳其本地运营与欧洲市场连接。", companyCards: ["伊斯坦布尔本地商务运营", "连接中国、土耳其与欧洲", "工业、科技、数字与组织服务"], aboutTitle: "关于我们",
      aboutText: "NJGROUP 的目标不只是产品进出口。我们的核心目标是在土耳其和欧洲市场建立中国制造的本地化运营体系。",
      visionTitle: "愿景与使命",
      visionText1: "我们的愿景是成为中国企业进入土耳其和欧洲市场时最强的本地化工业运营平台之一。",
      visionText2: "我们的使命是把中国制造带向国际市场，建立强大的本地运营体系，推动中国、土耳其与欧洲之间的合作，并创造可持续商业价值。",
      contactTitle: "联系 NJGROUP", contactText: "如需合作、采购、代理或项目洽谈，请联系我们。", email: "发送邮件",
      footer: "© 2018 NJGROUP. 版权所有。 · "
    },
    fr: {
      navBusiness: "Activités", navStrengths: "Forces", navAbout: "À propos", navContact: "Contact",
      badge: "Türkiye · Europe · Chine", heroTitle: "Connecter la production chinoise à <span>la Türkiye et l'Europe</span>",
      heroText: "NJGROUP est une plateforme d'opérations industrielles localisée en Türkiye, reliant la Chine aux marchés européens. Nous proposons développement de marché, gestion des canaux, opérations de marque et services locaux.",
      heroCta1: "Domaines d'activité", heroCta2: "Nous contacter", panelTitle: "Structure de plateforme",
      panelText: "Chaîne d'approvisionnement chinoise + opérations locales en Türkiye + connexions européennes.",
      stat1: "Domaines", stat2: "Marchés", stat3: "Plateforme", businessTitle: "Domaines d'activité NJGROUP",
      businessSub: "Nous construisons une plateforme régionale de coopération industrielle réunissant entrée sur le marché, développement de canaux, marketing digital, showroom, événements commerciaux et opérations locales.",
      enterPage: "Ouvrir la page détail", sliderHint: "Faites défiler horizontalement pour explorer la structure d'activité NJGROUP.",
      alt: "Services détaillés", strengthsTitle: "Forces principales",
      strengthsSub: "NJGROUP crée un écosystème commercial régional reliant la production chinoise, les opérations en Türkiye et le marché européen.",
      strengthCoreKicker: "PLATEFORME NJGROUP", strengthCoreTitle: "Puissance opérationnelle localisée entre Chine, Türkiye et Europe",
      strengthCoreText: "Nous réunissons sourcing, entrée sur le marché, ventes digitales, showroom, salons et support après-vente dans une seule plateforme.",
      companyTitle: "NJGROUP TECHNOLOGIE DE TRANSFORMATION VERTE",
      companyText: "NJGROUP YEŞİL DÖNÜŞÜM TEKNOLOJİ SANAYİ VE DIŞ TİCARET LİMİTED ŞİRKETİ est basée dans la zone commerciale İSTOÇ à Istanbul. Grâce à la position stratégique de la Türkiye, nous fournissons intégration de chaîne d'approvisionnement chinoise, canaux locaux, connexions européennes, systèmes de marketing digital et services showroom.",
      companyLine: "Nous sommes plus qu'une société de commerce extérieur.", companyKicker: "PROFIL DE NJGROUP", companyVisualTitle: "PLATEFORME INDUSTRIELLE EURASIE", companyVisualText: "Chaîne d'approvisionnement chinoise, opérations locales en Türkiye et connexion européenne.", companyCards: ["Opération locale basée à Istanbul", "Pont entre Chine, Türkiye et Europe", "Solutions industrielles, technologiques, digitales et événementielles"], aboutTitle: "À propos",
      aboutText: "L'objectif de NJGROUP ne se limite pas à l'import-export. Notre but principal est de créer un système d'opérations localisées pour la production chinoise en Türkiye et en Europe.",
      visionTitle: "Vision et mission",
      visionText1: "Notre vision est de devenir l'une des plateformes industrielles localisées les plus fortes pour les entreprises chinoises entrant en Türkiye et en Europe.",
      visionText2: "Notre mission est d'amener la production chinoise vers les marchés internationaux, de créer des opérations locales solides, de développer la coopération Chine - Türkiye - Europe et de générer une valeur durable.",
      contactTitle: "Contacter NJGROUP", contactText: "Contactez-nous pour coopération, sourcing, distribution ou projets.", email: "Envoyer un e-mail",
      footer: "© 2018 NJGROUP. Tous droits réservés. · "
    },
    de: {
      navBusiness: "Geschäftsfelder", navStrengths: "Stärken", navAbout: "Über uns", navContact: "Kontakt",
      badge: "Türkiye · Europa · China", heroTitle: "Chinesische Produktion mit <span>Türkiye und Europa verbinden</span>",
      heroText: "NJGROUP ist eine in der Türkiye ansässige lokalisierte Industrieplattform, die China mit europäischen Märkten verbindet. Wir bieten Marktentwicklung, Kanalmanagement, Markenbetrieb und lokale Servicelösungen.",
      heroCta1: "Geschäftsfelder", heroCta2: "Kontakt", panelTitle: "Plattformstruktur",
      panelText: "Chinesische Lieferkette + lokale Operationen in Türkiye + europäische Marktverbindungen.",
      stat1: "Bereiche", stat2: "Märkte", stat3: "Plattform", businessTitle: "NJGROUP Kerngeschäftsfelder",
      businessSub: "Wir schaffen eine regionale Plattform für industrielle Zusammenarbeit mit Markteintritt, Kanalentwicklung, digitalem Marketing, Showroom-Management, Geschäftsevents und lokalen Operationen.",
      enterPage: "Detailseite öffnen", sliderHint: "Wischen Sie horizontal, um die NJGROUP Geschäftsstruktur zu entdecken.",
      alt: "Unterservices", strengthsTitle: "Kernstärken",
      strengthsSub: "NJGROUP schafft ein regionales Handelsökosystem, das chinesische Produktion mit Operationen in Türkiye und dem europäischen Markt verbindet.",
      strengthCoreKicker: "NJGROUP PLATTFORM", strengthCoreTitle: "Lokalisierte Betriebskraft zwischen China, Türkiye und Europa",
      strengthCoreText: "Wir verbinden Beschaffung, Markteintritt, digitalen Vertrieb, Showroom, Messen und After-Sales-Support auf einer Plattform.",
      companyTitle: "NJGROUP TECHNOLOGIE FÜR GRÜNE TRANSFORMATION",
      companyText: "NJGROUP YEŞİL DÖNÜŞÜM TEKNOLOJİ SANAYİ VE DIŞ TİCARET LİMİTED ŞİRKETİ hat seinen Sitz im İSTOÇ-Handelsgebiet in Istanbul. Dank der strategischen Lage der Türkiye bieten wir Integration chinesischer Lieferketten, lokale Kanäle, europäische Marktverbindungen, digitale Marketingsysteme und Showroom-Services.",
      companyLine: "Wir sind mehr als ein Außenhandelsunternehmen.", companyKicker: "NJGROUP UNTERNEHMENSPROFIL", companyVisualTitle: "EURASISCHE INDUSTRIEPLATTFORM", companyVisualText: "Chinesische Lieferkette, lokale Operationen in Türkiye und europäische Marktverbindung.", companyCards: ["Lokaler Geschäftsbetrieb in Istanbul", "Brücke zwischen China, Türkiye und Europa", "Industrie-, Technologie-, Digital- und Eventlösungen"], aboutTitle: "Über uns",
      aboutText: "Das Ziel von NJGROUP ist nicht nur Import und Export. Unser Hauptziel ist der Aufbau eines lokalisierten Betriebssystems für chinesische Produktion in Türkiye und Europa.",
      visionTitle: "Vision und Mission",
      visionText1: "Unsere Vision ist es, eine der stärksten lokalisierten Industrieplattformen für chinesische Unternehmen beim Eintritt in Türkiye und Europa zu werden.",
      visionText2: "Unsere Mission ist es, chinesische Produktion auf internationale Märkte zu bringen, starke lokale Betriebssysteme aufzubauen, die Zusammenarbeit China - Türkiye - Europa zu entwickeln und nachhaltigen kommerziellen Wert zu schaffen.",
      contactTitle: "NJGROUP kontaktieren", contactText: "Kontaktieren Sie uns für Kooperation, Beschaffung, Vertrieb oder Projektgespräche.", email: "E-Mail senden",
      footer: "© 2018 NJGROUP. Alle Rechte vorbehalten. · "
    }
  };

  const services = {
    eco: {
      desc: [
        "Çevre dostu malzemeler, geri dönüşüm ürünleri, sürdürülebilir çözümler ve döngüsel ekonomi projeleri üzerine çalışıyoruz.",
        "We work on eco-friendly materials, recycled products, sustainable solutions and circular economy projects.",
        "我们专注环保材料、回收产品、可持续解决方案和循环经济项目。",
        "Nous travaillons sur des matériaux écologiques, des produits recyclés, des solutions durables et l'économie circulaire.",
        "Wir arbeiten an umweltfreundlichen Materialien, Recyclingprodukten, nachhaltigen Lösungen und Kreislaufwirtschaft."
      ],
      media: ["Atıktan değere, geleceğe dönüşüm", "From waste to value, toward the future", "从废弃物到价值，迈向未来", "Des déchets à la valeur, vers l'avenir", "Vom Abfall zum Wert, in die Zukunft"],
      kicker: ["01 / Eko Dönüşüm", "01 / Eco Transformation", "01 / 生态循环", "01 / Éco-transformation", "01 / Öko-Transformation"],
      title: ["Geri dönüşüm odaklı ürün ve malzeme çözümleri", "Recycling-focused product and material solutions", "以回收为核心的产品与材料解决方案", "Solutions de produits et matériaux orientées recyclage", "Recyclingorientierte Produkt- und Materiallösungen"],
      detail: ["Atık lastik ve kauçuk bazlı geri dönüşüm süreçlerini, sürdürülebilir ürün geliştirme ve yeni kullanım alanlarıyla birleştiriyoruz. Amaç, çevresel sorumluluğu ticari değere dönüştüren ölçülebilir bir tedarik ve uygulama modeli kurmaktır.", "We combine waste tire and rubber recycling processes with sustainable product development and new application areas. The aim is to build a measurable supply and application model that converts environmental responsibility into commercial value.", "我们将废旧轮胎和橡胶回收流程与可持续产品开发、新应用场景结合，建立把环保责任转化为商业价值的可衡量供应与应用模式。", "Nous associons le recyclage des pneus et du caoutchouc au développement durable de produits et à de nouveaux usages, pour transformer la responsabilité environnementale en valeur commerciale mesurable.", "Wir verbinden Altreifen- und Gummirecycling mit nachhaltiger Produktentwicklung und neuen Anwendungen, um Umweltverantwortung in messbaren kommerziellen Wert zu verwandeln."],
      tags: [["Döngüsel ekonomi", "Düşük karbon", "Geri dönüşüm kauçuk", "Uygulama ürünleri"], ["Circular economy", "Low carbon", "Recycled rubber", "Application products"], ["循环经济", "低碳", "再生橡胶", "应用产品"], ["Économie circulaire", "Bas carbone", "Caoutchouc recyclé", "Produits d'application"], ["Kreislaufwirtschaft", "CO2-arm", "Recyclinggummi", "Anwendungsprodukte"]],
      subs: [
        [["Atık Lastik Toplama", "Kaynak tespiti, toplama organizasyonu ve ayrıştırmaya hazır stok yönetimi için operasyon planı oluşturulur."], ["Waste Tire Collection", "We plan source identification, collection organization and stock management ready for sorting."], ["废旧轮胎收集", "规划来源识别、收集组织和待分拣库存管理。"], ["Collecte de pneus usagés", "Planification des sources, de la collecte et du stock prêt au tri."], ["Altreifensammlung", "Planung von Quellen, Sammlung und sortierfähigem Bestand."]],
        [["Parçalama & Öğütme", "Lastiklerin parçalanması, granül hale getirilmesi ve kalite sınıflarına göre ayrılması süreçleri yönetilir."], ["Shredding & Grinding", "Tires are shredded, granulated and separated by quality classes."], ["破碎与研磨", "管理轮胎破碎、颗粒化和按质量等级分离。"], ["Broyage & granulation", "Gestion du broyage, de la granulation et du tri par qualité."], ["Zerkleinern & Mahlen", "Reifen werden zerkleinert, granuliert und nach Qualität getrennt."]],
        [["Geri Dönüşüm Kauçuk", "Zemin kaplama, spor alanı, trafik güvenlik ürünü ve teknik kauçuk uygulamaları için malzeme tedariki yapılır."], ["Recycled Rubber", "Materials are supplied for flooring, sports fields, traffic safety and technical rubber applications."], ["再生橡胶", "为地面铺装、运动场、交通安全和技术橡胶应用供应材料。"], ["Caoutchouc recyclé", "Fourniture pour sols, terrains de sport, sécurité routière et applications techniques."], ["Recyclinggummi", "Materialien für Böden, Sportflächen, Verkehrssicherheit und technische Anwendungen."]],
        [["Uygulama Alanları", "Çocuk oyun alanları, koşu pistleri, hayvancılık zeminleri, ayakkabı tabanları, hortum ve conta ürünleri geliştirilir."], ["Application Areas", "Products include playgrounds, running tracks, livestock flooring, soles, hoses and seals."], ["应用场景", "开发儿童游乐地面、跑道、畜牧地面、鞋底、软管和密封产品。"], ["Domaines d'application", "Aires de jeux, pistes, sols d'élevage, semelles, tuyaux et joints."], ["Anwendungsbereiche", "Spielplätze, Laufbahnen, Stallböden, Sohlen, Schläuche und Dichtungen."]],
        [["Kalite Kontrol", "Ürünlerin dayanım, kullanım ömrü ve performans değerleri hedef pazara göre kontrol edilir."], ["Quality Control", "Durability, service life and performance are checked according to target market needs."], ["质量控制", "根据目标市场检查耐久性、使用寿命和性能指标。"], ["Contrôle qualité", "Résistance, durée de vie et performance vérifiées selon le marché cible."], ["Qualitätskontrolle", "Haltbarkeit, Lebensdauer und Leistung werden marktgerecht geprüft."]],
        [["Ambalaj & Sevkiyat", "İhracata uygun paketleme, paletleme, etiketleme ve sevkiyat hazırlığı tek akışta planlanır."], ["Packaging & Shipping", "Export packaging, palletizing, labeling and shipment preparation are planned in one flow."], ["包装与发运", "统一规划出口包装、托盘、标签和发运准备。"], ["Emballage & expédition", "Emballage export, palettes, étiquetage et expédition en un seul flux."], ["Verpackung & Versand", "Exportverpackung, Palettierung, Etikettierung und Versandvorbereitung aus einer Hand."]]
      ]
    },
    tech: {
      desc: ["Robot teknolojileri, AI cihazları, otomasyon sistemleri ve akıllı ekipman çözümleri sunuyoruz.", "We provide robotics, AI devices, automation systems and smart equipment solutions.", "我们提供机器人技术、AI设备、自动化系统和智能设备解决方案。", "Nous proposons robotique, appareils IA, automatisation et équipements intelligents.", "Wir bieten Robotik, KI-Geräte, Automatisierung und intelligente Ausrüstung."],
      media: ["Otomasyon, robotik ve veri tabanlı akıllı sistemler", "Automation, robotics and data-driven smart systems", "自动化、机器人与数据驱动系统", "Automatisation, robotique et systèmes pilotés par les données", "Automatisierung, Robotik und datenbasierte Systeme"],
      kicker: ["02 / Akıllı Teknoloji", "02 / Smart Technology", "02 / 智能科技", "02 / Technologie intelligente", "02 / Intelligente Technologie"],
      title: ["Üretim, lojistik ve hizmet süreçleri için akıllı ekipmanlar", "Smart equipment for production, logistics and services", "面向生产、物流和服务流程的智能设备", "Équipements intelligents pour production, logistique et services", "Intelligente Ausrüstung für Produktion, Logistik und Service"],
      detail: ["Robot teknolojileri, yapay zeka destekli cihazlar ve otomasyon sistemleriyle işletmelerin verimlilik, takip ve operasyon kalitesini güçlendiren çözümler sunuyoruz.", "With robotics, AI-enabled devices and automation, we improve efficiency, tracking and operational quality.", "通过机器人、AI设备和自动化系统提升企业效率、追踪能力和运营质量。", "Avec la robotique, l'IA et l'automatisation, nous renforçons efficacité, suivi et qualité opérationnelle.", "Mit Robotik, KI-Geräten und Automatisierung stärken wir Effizienz, Nachverfolgung und Betriebsqualität."],
      tags: [["Robot teknolojileri", "AI cihazlar", "Otonom sistemler", "Veri analitiği"], ["Robotics", "AI devices", "Autonomous systems", "Data analytics"], ["机器人技术", "AI设备", "自主系统", "数据分析"], ["Robotique", "Appareils IA", "Systèmes autonomes", "Analyse de données"], ["Robotik", "KI-Geräte", "Autonome Systeme", "Datenanalyse"]],
      subs: [["Endüstriyel Otomasyon", "Lojistik & Depolama", "Yapay Zeka & Veri", "Sağlık & Biyoteknoloji", "Tarım & Akıllı Tarım", "Hizmet Robotları"].map((x, i) => [x, ["Üretim hatlarında robot kol, kontrol paneli, sensör ve otomasyon ekipmanları için çözüm eşleştirmesi yapılır.", "Depo içi taşıma, paket ayırma, rota yönetimi ve akıllı raf operasyonları için mobil robot çözümleri sunulur.", "Operasyon takibi, performans ölçümü, raporlama ve karar destek süreçleri için veri odaklı altyapılar kurgulanır.", "Laboratuvar otomasyonu, hassas ekipman ve süreç güvenliği gerektiren teknolojiler için tedarik kanalı geliştirilir.", "Seralar, sulama, izleme, hasat destek sistemleri ve tarımsal robot çözümleri için ürün portföyü hazırlanır.", "Karşılama, yönlendirme, temizlik, servis ve destek robotları için yerel kullanım senaryoları oluşturulur."][i]])][0]
    },
    build: {
      desc: ["Yapı malzemeleri, dekorasyon ürünleri, elektrik malzemeleri, mekanik sistemler ve mühendislik destek ürünleri alanında faaliyet gösteriyoruz.", "We operate in building materials, decoration products, electrical materials, mechanical systems and engineering support products.", "我们经营建材、装饰产品、电气材料、机械系统和工程配套产品。", "Nous opérons dans les matériaux de construction, la décoration, l'électricité, les systèmes mécaniques et les produits d'ingénierie.", "Wir arbeiten mit Baumaterialien, Dekoration, Elektromaterial, mechanischen Systemen und Engineering-Produkten."],
      media: ["Güçlü yapı, kaliteli malzeme, doğru tedarik", "Strong structures, quality materials, right sourcing", "坚固建筑、优质材料、精准供应", "Structure solide, matériaux de qualité, bon sourcing", "Starke Struktur, Qualitätsmaterial, richtige Beschaffung"],
      kicker: ["03 / Yapı & Hırdavat", "03 / Building & Hardware", "03 / 建材与五金", "03 / Bâtiment & quincaillerie", "03 / Bau & Hardware"],
      title: ["İnşaat, tesisat, elektrik ve dekorasyon ürünlerinde geniş tedarik ağı", "A broad sourcing network for construction, plumbing, electrical and decoration products", "覆盖建筑、管道、电气与装饰产品的广泛供应网络", "Un large réseau pour construction, plomberie, électricité et décoration", "Breites Beschaffungsnetz für Bau, Sanitär, Elektro und Dekoration"],
      detail: ["Yapı malzemelerinden el aletlerine, elektrik ekipmanlarından yalıtım ürünlerine kadar proje bazlı veya kanal bazlı ürün portföyleri hazırlıyoruz.", "From building materials and tools to electrical equipment and insulation products, we prepare project-based and channel-based portfolios.", "从建材、工具到电气设备和保温防水产品，我们按项目或渠道准备产品组合。", "Des matériaux aux outils, de l'électricité à l'isolation, nous préparons des portefeuilles par projet ou canal.", "Von Baumaterialien und Werkzeugen bis zu Elektro- und Dämmprodukten erstellen wir projekt- und kanalbezogene Portfolios."],
      tags: [["Yapı malzemeleri", "Elektrik", "Tesisat", "Dekorasyon"], ["Building materials", "Electrical", "Plumbing", "Decoration"], ["建材", "电气", "管道", "装饰"], ["Matériaux", "Électricité", "Plomberie", "Décoration"], ["Baumaterial", "Elektro", "Sanitär", "Dekoration"]],
      subs: null
    },
    machine: {
      desc: ["Gıda makineleri, madencilik ekipmanları, üretim hatları ve çeşitli endüstriyel makine çözümleri sunuyoruz.", "We supply food machinery, mining equipment, production lines and various industrial machinery solutions.", "我们提供食品机械、矿山设备、生产线及各类工业机械解决方案。", "Nous fournissons machines alimentaires, équipements miniers, lignes de production et solutions industrielles.", "Wir liefern Lebensmittelmaschinen, Bergbauausrüstung, Produktionslinien und Industriemaschinen."],
      media: ["Yüksek performanslı makine ve üretim çözümleri", "High-performance machinery and production solutions", "高性能机械与生产解决方案", "Machines et solutions de production haute performance", "Hochleistungsmaschinen und Produktionslösungen"],
      kicker: ["04 / Endüstriyel Makine", "04 / Industrial Machinery", "04 / 工业机械", "04 / Machines industrielles", "04 / Industriemaschinen"],
      title: ["Üretim hattından ağır ekipmana kadar endüstriyel çözüm merkezi", "An industrial solution hub from production lines to heavy equipment", "从生产线到重型设备的工业解决方案中心", "Un centre de solutions des lignes de production aux équipements lourds", "Ein Lösungszentrum von Produktionslinien bis zu schweren Anlagen"],
      detail: ["Çin üretim kaynaklarını Türkiye ve Avrupa pazarının ihtiyaçlarıyla eşleştirerek makine, ekipman, yedek parça ve teknik destek süreçlerini bir araya getiriyoruz.", "We match Chinese manufacturing resources with Türkiye and European market needs, covering machinery, equipment, spare parts and technical support.", "我们将中国制造资源与土耳其和欧洲市场需求匹配，覆盖机械、设备、备件与技术支持。", "Nous associons les ressources chinoises aux besoins de la Türkiye et de l'Europe: machines, équipements, pièces et support.", "Wir verbinden chinesische Produktionsressourcen mit Marktbedarf in Türkiye und Europa: Maschinen, Anlagen, Ersatzteile und Support."],
      tags: [["Üretim hattı", "Gıda makineleri", "Madencilik", "Teknik destek"], ["Production line", "Food machinery", "Mining", "Technical support"], ["生产线", "食品机械", "矿山", "技术支持"], ["Ligne de production", "Machines alimentaires", "Mines", "Support technique"], ["Produktionslinie", "Lebensmittelmaschinen", "Bergbau", "Technischer Support"]],
      subs: null
    },
    digital: {
      desc: ["TikTok, sosyal medya, canlı yayın satış sistemleri, bağımsız web sitesi yönetimi ve AI destekli dijital pazarlama çözümleri geliştiriyoruz.", "We develop TikTok, social media, live commerce, independent website management and AI-supported digital marketing solutions.", "我们开发 TikTok、社交媒体、直播销售、独立站运营和 AI 支持的数字营销方案。", "Nous développons TikTok, réseaux sociaux, live commerce, sites indépendants et marketing digital assisté par IA.", "Wir entwickeln TikTok-, Social-Media-, Live-Commerce-, Website- und KI-gestützte Marketinglösungen."],
      media: ["Dijital dünyada satış, büyüme ve marka operasyonu", "Sales, growth and brand operations in the digital world", "数字世界里的销售、增长与品牌运营", "Vente, croissance et opérations de marque dans le digital", "Vertrieb, Wachstum und Markenbetrieb in der digitalen Welt"],
      kicker: ["05 / Dijital Pazarlama", "05 / Digital Marketing", "05 / 数字营销", "05 / Marketing digital", "05 / Digitales Marketing"],
      title: ["Markalar için e-ticaret, içerik, reklam ve performans yönetimi", "E-commerce, content, advertising and performance management for brands", "为品牌提供电商、内容、广告和效果管理", "E-commerce, contenu, publicité et performance pour les marques", "E-Commerce, Content, Werbung und Performance für Marken"],
      detail: ["Çin menşeli ürün ve markaların Türkiye ile Avrupa pazarına dijital kanallardan girmesi için satış odaklı pazarlama altyapısı, içerik üretimi ve kampanya yönetimi kuruyoruz.", "We build sales-focused marketing infrastructure, content production and campaign management for Chinese products and brands entering Türkiye and Europe digitally.", "我们为中国产品和品牌进入土耳其及欧洲市场搭建销售导向的营销基础、内容生产和活动管理。", "Nous créons infrastructure marketing, contenu et campagnes pour l'entrée digitale des produits et marques chinois en Türkiye et en Europe.", "Wir bauen vertriebsorientierte Marketinginfrastruktur, Content und Kampagnen für chinesische Produkte und Marken in Türkiye und Europa."],
      tags: [["E-ticaret", "TikTok", "Canlı yayın satış", "Performans reklamı"], ["E-commerce", "TikTok", "Live commerce", "Performance ads"], ["电商", "TikTok", "直播销售", "效果广告"], ["E-commerce", "TikTok", "Live commerce", "Publicité performance"], ["E-Commerce", "TikTok", "Live-Commerce", "Performance Ads"]],
      subs: null
    },
    fair: {
      desc: ["Fuar stand kiralama, stant kurulumu, tercümanlık, ticari organizasyonlar ve B2B eşleştirme hizmetleri sunuyoruz.", "We provide fair stand rental, booth setup, interpreting, commercial events and B2B matchmaking.", "我们提供展位租赁、展台搭建、翻译、商务组织和 B2B 对接服务。", "Nous proposons location de stand, installation, interprétariat, événements commerciaux et matchmaking B2B.", "Wir bieten Messestand-Miete, Standbau, Dolmetschen, Geschäftsevents und B2B-Matching."],
      media: ["Profesyonel fuar, stand ve B2B bağlantı hizmetleri", "Professional fair, booth and B2B connection services", "专业展会、展台与 B2B 对接服务", "Services professionnels de salon, stand et connexion B2B", "Professionelle Messe-, Stand- und B2B-Services"],
      kicker: ["06 / Fuar & Organizasyon", "06 / Fair & Organization", "06 / 展会与组织服务", "06 / Salons & organisation", "06 / Messen & Organisation"],
      title: ["Uluslararası ticari görüşmeler için yerel organizasyon gücü", "Local organization power for international business meetings", "服务国际商务洽谈的本地组织能力", "Force locale pour rencontres commerciales internationales", "Lokale Organisationskraft für internationale Geschäftstreffen"],
      detail: ["Fuar katılımı, stand kurulumu, ürün tanıtımı, tercümanlık, ulaşım ve B2B eşleştirme hizmetlerini tek merkezden yöneterek ticari temasların verimli sonuçlara dönüşmesini sağlıyoruz.", "We manage fair participation, booth setup, product promotion, interpreting, transport and B2B matchmaking from one center to turn business contacts into results.", "我们统一管理参展、展台搭建、产品展示、翻译、交通和 B2B 对接，让商务接触转化为成果。", "Nous gérons salon, stand, promotion, interprétariat, transport et B2B depuis un centre unique pour transformer les contacts en résultats.", "Wir steuern Messe, Standbau, Produktpräsentation, Dolmetschen, Transport und B2B-Matching zentral, damit Kontakte Ergebnisse liefern."],
      tags: [["Fuar hizmetleri", "Stand kurulum", "B2B eşleştirme", "Tercüme"], ["Fair services", "Booth setup", "B2B matching", "Translation"], ["展会服务", "展台搭建", "B2B 对接", "翻译"], ["Services salon", "Installation stand", "Matchmaking B2B", "Traduction"], ["Messeservice", "Standbau", "B2B-Matching", "Übersetzung"]],
      subs: null
    }
  };

  const subFallback = {
    tech: [["Endüstriyel Otomasyon", "Lojistik & Depolama", "Yapay Zeka & Veri", "Sağlık & Biyoteknoloji", "Tarım & Akıllı Tarım", "Hizmet Robotları"], ["Industrial Automation", "Logistics & Warehousing", "AI & Data", "Health & Biotechnology", "Agriculture & Smart Farming", "Service Robots"], ["工业自动化", "物流与仓储", "AI 与数据", "医疗与生物科技", "农业与智慧农业", "服务机器人"], ["Automatisation industrielle", "Logistique & stockage", "IA & données", "Santé & biotechnologie", "Agriculture intelligente", "Robots de service"], ["Industrielle Automatisierung", "Logistik & Lager", "KI & Daten", "Gesundheit & Biotechnologie", "Landwirtschaft & Smart Farming", "Serviceroboter"]],
    build: [["Hırdavat & El Aletleri", "Elektrik & Aydınlatma", "Sıhhi Tesisat", "Yapı Malzemeleri", "Yalıtım & İklimlendirme", "Boya & Kimyasal"], ["Hardware & Tools", "Electrical & Lighting", "Plumbing", "Building Materials", "Insulation & HVAC", "Paint & Chemicals"], ["五金与工具", "电气与照明", "给排水管道", "建筑材料", "保温防水与暖通", "涂料与化工"], ["Quincaillerie & outils", "Électricité & éclairage", "Plomberie", "Matériaux", "Isolation & CVC", "Peinture & chimie"], ["Hardware & Werkzeuge", "Elektro & Beleuchtung", "Sanitär", "Baumaterialien", "Dämmung & Klima", "Farben & Chemie"]],
    machine: [["Üretim Hatları", "Gıda İşleme Makineleri", "Madencilik Ekipmanları", "Forklift & Taşıma", "Motor & Redüktör", "Kurulum & Servis"], ["Production Lines", "Food Processing Machines", "Mining Equipment", "Forklift & Handling", "Motors & Reducers", "Installation & Service"], ["生产线", "食品加工机械", "矿山设备", "叉车与搬运", "电机与减速机", "安装与服务"], ["Lignes de production", "Machines alimentaires", "Équipements miniers", "Chariots & manutention", "Moteurs & réducteurs", "Installation & service"], ["Produktionslinien", "Lebensmittelmaschinen", "Bergbauausrüstung", "Stapler & Handling", "Motoren & Getriebe", "Installation & Service"]],
    digital: [["E-Ticaret & Pazaryeri", "Bağımsız Web Mağazası", "Canlı Yayın & Influencer", "Dijital Reklam", "SEO & İçerik", "Raporlama"], ["E-commerce & Marketplaces", "Independent Web Store", "Live Commerce & Influencers", "Digital Advertising", "SEO & Content", "Reporting"], ["电商与平台店铺", "独立站", "直播与达人营销", "数字广告", "SEO 与内容", "数据报告"], ["E-commerce & marketplaces", "Boutique indépendante", "Live & influenceurs", "Publicité digitale", "SEO & contenu", "Reporting"], ["E-Commerce & Marktplätze", "Eigener Webshop", "Live & Influencer", "Digitale Werbung", "SEO & Content", "Reporting"]],
    fair: [["Fuar Hizmetleri", "Stand Tasarım & Kurulum", "B2B Görüşmeler", "Tanıtım Materyalleri", "Çeviri & Tercümanlık", "Karşılama & Transfer"], ["Fair Services", "Booth Design & Setup", "B2B Meetings", "Promotion Materials", "Translation & Interpreting", "Reception & Transfer"], ["展会服务", "展台设计与搭建", "B2B 洽谈", "宣传资料", "笔译与口译", "接待与接送"], ["Services salon", "Design & installation", "Rencontres B2B", "Supports promotionnels", "Traduction & interprétation", "Accueil & transfert"], ["Messeservice", "Standdesign & Aufbau", "B2B-Gespräche", "Werbematerial", "Übersetzen & Dolmetschen", "Empfang & Transfer"]]
  };

  const genericSubText = {
    en: "We plan sourcing, operations and local market use according to the target project.",
    zh: "根据目标项目规划供应、运营和本地市场应用。",
    fr: "Nous planifions sourcing, opérations et usage local selon le projet cible.",
    de: "Wir planen Beschaffung, Betrieb und lokale Anwendung passend zum Zielprojekt."
  };

  function text(selector, value, html) {
    const el = document.querySelector(selector);
    if (!el) return;
    if (html) el.innerHTML = value;
    else el.textContent = value;
  }

  function all(selector, values, html) {
    document.querySelectorAll(selector).forEach((el, index) => {
      if (values[index] === undefined) return;
      if (html) el.innerHTML = values[index];
      else el.textContent = values[index];
    });
  }

  function setLang(lang) {
    const dict = t[lang] || t.tr;
    document.documentElement.lang = lang === "zh" ? "zh-CN" : lang;
    text(".nav-item > a", dict.navBusiness);
    all(".submenu a", ["eco", "tech", "build", "machine", "digital", "fair"].map((k) => pick(names[k], lang)));
    all(".nav-links > a", [dict.navStrengths, dict.navAbout, dict.navContact]);
    text(".badge", dict.badge);
    text(".hero h1", dict.heroTitle, true);
    text(".hero p", dict.heroText);
    all(".hero .btn", [dict.heroCta1, dict.heroCta2]);
    text(".panel h3", dict.panelTitle);
    text(".panel p", dict.panelText);
    all(".stat", [`<strong>6</strong>${dict.stat1}`, `<strong>3</strong>${dict.stat2}`, `<strong>1</strong>${dict.stat3}`], true);
    text("#business .section-title", dict.businessTitle);
    text("#business .section-sub", dict.businessSub);
    all("#business .service h3", ["eco", "tech", "build", "machine", "digital", "fair"].map((k) => pick(names[k], lang)));
    all("#business .service p", ["eco", "tech", "build", "machine", "digital", "fair"].map((k) => pick(services[k].desc, lang)));
    all(".service-actions a", Array(6).fill(dict.alt));
    all(".slide-copy h3", ["eco", "tech", "build", "machine", "digital", "fair"].map((k) => pick(names[k], lang)));
    all(".slide-copy p", ["eco", "tech", "build", "machine", "digital", "fair"].map((k) => pick(services[k].desc, lang)));
    all(".slide-index", ["eco", "tech", "build", "machine", "digital", "fair"].map((k, i) => `${String(i + 1).padStart(2, "0")} / ${pick(names[k], lang)}`));
    all(".slide-copy .btn", Array(6).fill(dict.enterPage));
    text(".slider-hint", dict.sliderHint);

    ["eco", "tech", "build", "machine", "digital", "fair"].forEach((key, sectionIndex) => {
      const section = document.querySelectorAll(".detail-section")[sectionIndex];
      if (!section) return;
      text(`#${section.id} .detail-media span`, pick(services[key].media, lang));
      text(`#${section.id} .detail-kicker`, pick(services[key].kicker, lang));
      text(`#${section.id} .detail-copy h3`, pick(services[key].title, lang));
      text(`#${section.id} .detail-copy p:not(.detail-kicker)`, pick(services[key].detail, lang));
      all(`#${section.id} .detail-tags span`, services[key].tags[langs.indexOf(lang)] || services[key].tags[0]);
      const cards = section.querySelectorAll(".sub-card");
      cards.forEach((card, i) => {
        if (key === "eco") {
          const item = services.eco.subs[i][langs.indexOf(lang)] || services.eco.subs[i][0];
          card.querySelector("h4").textContent = item[0];
          card.querySelector("p").textContent = item[1];
        } else if (lang === "tr") {
          const saved = original.subCards[sectionIndex] && original.subCards[sectionIndex][i];
          if (saved) {
            card.querySelector("h4").textContent = saved.title;
            card.querySelector("p").textContent = saved.text;
          }
        } else {
          const titles = subFallback[key] ? subFallback[key][langs.indexOf(lang)] || subFallback[key][0] : null;
          if (titles) card.querySelector("h4").textContent = titles[i];
          if (lang !== "tr") card.querySelector("p").textContent = genericSubText[lang];
        }
      });
    });

    text("#products .section-title", dict.strengthsTitle);
    text("#products .section-sub", dict.strengthsSub);
    text(".strength-core .detail-kicker", dict.strengthCoreKicker);
    text(".strength-core h3", dict.strengthCoreTitle);
    text(".strength-core p:not(.detail-kicker)", dict.strengthCoreText);
    const strengthTitles = {
      tr: ["Yerel Operasyon Gücü", "Çin Tedarik Zinciri Gücü", "Dijital Pazarlama", "Showroom ve Ticari Ağ", "Avrupa Pazar Bağlantıları", "Satış Sonrası Destek"],
      en: ["Local Operation Power", "China Supply Chain Power", "Digital Marketing", "Showroom and Business Network", "European Market Connections", "After-sales Support"],
      zh: ["本地运营能力", "中国供应链能力", "数字营销", "展厅与商务网络", "欧洲市场连接", "售后支持"],
      fr: ["Force opérationnelle locale", "Force supply chain chinoise", "Marketing digital", "Showroom et réseau commercial", "Connexions européennes", "Support après-vente"],
      de: ["Lokale Betriebskraft", "Chinesische Lieferkettenkraft", "Digitales Marketing", "Showroom und Geschäftsnetz", "Europäische Marktverbindungen", "After-Sales-Support"]
    };
    all("#products .strength-item h3", strengthTitles[lang]);
    if (lang === "tr") {
      all("#products .strength-item p", original.productPs);
    } else {
      all("#products .strength-item p", Array(6).fill({ en: "A practical capability that helps brands enter, operate and grow in Türkiye and European markets.", zh: "帮助品牌进入、运营并拓展土耳其和欧洲市场的实用能力。", fr: "Une capacité concrète pour entrer, opérer et croître en Türkiye et en Europe.", de: "Eine praktische Fähigkeit für Markteintritt, Betrieb und Wachstum in Türkiye und Europa." }[lang]));
    }

    text(".company-profile .detail-kicker", dict.companyKicker);
    text(".company-profile h3", dict.companyTitle);
    all(".company-profile > p:not(.detail-kicker)", [dict.companyText, dict.companyLine]);
    text(".company-mark span:first-child", dict.companyVisualTitle);
    text(".company-mark span:last-child", dict.companyVisualText);
    all(".company-cards span", dict.companyCards);
    text("#about .section-title", dict.aboutTitle);
    text("#about .section-sub", dict.aboutText);
    text(".about-card h3", dict.visionTitle);
    all(".about-card p", [dict.visionText1, dict.visionText2]);
    text(".contact-box h2", dict.contactTitle);
    text(".contact-box p", dict.contactText);
    text(".contact-box .btn", dict.email);
    document.querySelector("footer").innerHTML = `${dict.footer}<a href="https://njgrup.com/">njgrup.com</a>`;
    localStorage.setItem("njLang", lang);
  }

  document.addEventListener("DOMContentLoaded", () => {
    const select = document.getElementById("languageSelect");
    original.productPs = Array.from(document.querySelectorAll("#products .strength-item p")).map((el) => el.textContent);
    original.subCards = Array.from(document.querySelectorAll(".detail-section")).map((section) => {
      return Array.from(section.querySelectorAll(".sub-card")).map((card) => ({
        title: card.querySelector("h4").textContent,
        text: card.querySelector("p").textContent
      }));
    });
    const saved = localStorage.getItem("njLang") || "tr";
    select.value = t[saved] ? saved : "tr";
    setLang(select.value);
    select.addEventListener("change", () => setLang(select.value));
  });
})();
