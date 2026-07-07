(function () {
  const lists = Array.from(document.querySelectorAll("[data-rubber-news-list]"));
  const stamps = Array.from(document.querySelectorAll("[data-rubber-news-updated]"));
  if (!lists.length) return;

  function formatDate(value) {
    if (!value) return "";
    const date = new Date(value);
    if (Number.isNaN(date.getTime())) return value;
    return date.toLocaleDateString("tr-TR", { year: "numeric", month: "short", day: "2-digit" });
  }

  function render(items) {
    lists.forEach(function (list) {
      if (list.hasAttribute("data-rubber-news-compact")) {
        renderCompact(list, items);
      } else {
        renderCards(list, items);
      }
    });
  }

  function renderCards(list, items) {
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

  function renderCompact(list, items) {
    list.innerHTML = "";
    const track = document.createElement("div");
    track.className = "hero-news-track";
    const loopItems = items.slice(0, 3);
    loopItems.concat(loopItems).forEach(function (item) {
      const link = document.createElement("a");
      link.className = "hero-news-item";
      link.href = item.url || "#";
      link.target = "_blank";
      link.rel = "noopener";
      link.dataset.track = "news_click";
      link.innerHTML = [
        "<span>" + (item.source || "Industry News") + " - " + formatDate(item.date) + "</span>",
        "<strong>" + (item.title || "Reclaimed rubber news") + "</strong>",
        "<small>" + (item.summary || "") + "</small>"
      ].join("");
      track.appendChild(link);
    });
    list.appendChild(track);
  }

  fetch("rubber-news.json?ts=" + Date.now(), { cache: "no-store" })
    .then(function (response) {
      if (!response.ok) throw new Error("News feed unavailable");
      return response.json();
    })
    .then(function (data) {
      render(Array.isArray(data.items) ? data.items : []);
      stamps.forEach(function (stamp) {
        if (data.updatedAt) stamp.textContent = "Son guncelleme: " + formatDate(data.updatedAt);
      });
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
