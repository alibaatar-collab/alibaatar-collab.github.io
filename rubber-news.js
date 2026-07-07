(function () {
  const list = document.querySelector("[data-rubber-news-list]");
  const stamp = document.querySelector("[data-rubber-news-updated]");
  if (!list) return;

  function formatDate(value) {
    if (!value) return "";
    const date = new Date(value);
    if (Number.isNaN(date.getTime())) return value;
    return date.toLocaleDateString("tr-TR", { year: "numeric", month: "short", day: "2-digit" });
  }

  function render(items) {
    list.innerHTML = "";
    items.slice(0, 3).forEach(function (item) {
      const article = document.createElement("article");
      article.className = "news-card";
      article.innerHTML = [
        '<div class="news-meta"><span>' + (item.source || "Industry News") + "</span><time>" + formatDate(item.date) + "</time></div>",
        "<h3>" + (item.title || "Reclaimed rubber news") + "</h3>",
        "<p>" + (item.summary || "") + "</p>",
        '<a href="' + (item.url || "#") + '" target="_blank" rel="noopener" data-track="news_click">Haberi Oku</a>'
      ].join("");
      list.appendChild(article);
    });
  }

  fetch("rubber-news.json?ts=" + Date.now(), { cache: "no-store" })
    .then(function (response) {
      if (!response.ok) throw new Error("News feed unavailable");
      return response.json();
    })
    .then(function (data) {
      render(Array.isArray(data.items) ? data.items : []);
      if (stamp && data.updatedAt) {
        stamp.textContent = "Son guncelleme: " + formatDate(data.updatedAt);
      }
    })
    .catch(function () {
      render([
        {
          title: "Guncel haber akisi hazirlaniyor",
          source: "NJGROUP",
          date: new Date().toISOString(),
          summary: "Surdurulebilirlik, atik lastik geri donusumu ve rejenere kaucuk haberleri gunluk olarak bu alanda yayinlanacaktir.",
          url: "https://news.google.com/search?q=reclaimed%20rubber%20rubber%20recycling"
        }
      ]);
    });
})();
