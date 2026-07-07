import email.utils
import html
import json
import re
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "rubber-news.json"

FEEDS = [
    "https://news.google.com/rss/search?q=reclaimed%20rubber%20OR%20rubber%20recycling%20OR%20devulcanization&hl=en-US&gl=US&ceid=US:en",
    "https://news.google.com/rss/search?q=at%C4%B1k%20lastik%20OR%20kau%C3%A7uk%20geri%20d%C3%B6n%C3%BC%C5%9F%C3%BCm%20OR%20geri%20d%C3%B6n%C3%BC%C5%9F%C3%BCm%20kau%C3%A7uk&hl=tr&gl=TR&ceid=TR:tr",
    "https://news.google.com/rss/search?q=circular%20economy%20sustainable%20materials%20rubber%20industry&hl=en-US&gl=US&ceid=US:en",
    "https://news.google.com/rss/search?q=Turkey%20environment%20recycling%20circular%20economy&hl=en-US&gl=US&ceid=US:en",
]

KEYWORDS = (
    "rubber",
    "reclaimed",
    "recycling",
    "devulcanization",
    "sustainable",
    "circular economy",
    "tire",
    "tyre",
    "kauçuk",
    "kaucuk",
    "lastik",
    "geri dönüşüm",
    "geri donusum",
    "sürdürülebilir",
    "surdurulebilir",
)


def clean_text(value):
    value = html.unescape(value or "")
    value = re.sub(r"<[^>]+>", " ", value)
    value = re.sub(r"\s+", " ", value).strip()
    value = repair_mojibake(value)
    return value


def repair_mojibake(value):
    if not value or not any(marker in value for marker in ("Ã", "Ä", "Å")):
        return value
    try:
        fixed = value.encode("latin-1").decode("utf-8")
    except UnicodeError:
        return value
    return fixed if fixed else value


def parse_date(value):
    if not value:
        return datetime.now(timezone.utc)
    parsed = email.utils.parsedate_to_datetime(value)
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def fetch_feed(url):
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "NJGROUP rubber news updater (+https://njgrup.com)",
            "Accept": "application/rss+xml, application/xml;q=0.9, */*;q=0.8",
        },
    )
    with urllib.request.urlopen(request, timeout=25) as response:
        return response.read()


def split_google_title(title):
    title = clean_text(title)
    if " - " in title:
        main, source = title.rsplit(" - ", 1)
        return main.strip(), source.strip()
    return title, "Industry News"


def entry_score(item):
    text = (item["title"] + " " + item["summary"]).lower()
    return sum(1 for keyword in KEYWORDS if keyword in text)


def build_summary(title, source, summary):
    compact_title = re.sub(r"\W+", "", title.lower())
    compact_summary = re.sub(r"\W+", "", summary.lower())
    if not summary or compact_title in compact_summary or len(summary) < 45:
        return f"{source} kaynağında yayınlanan bu gelişme, NJGROUP'un sürdürülebilir malzeme, geri dönüşüm ve rejenere kauçuk gündemi kapsamında takip ettiği haberler arasındadır."
    return summary[:220].rstrip(" ,.;") + ("..." if len(summary) > 220 else "")


def collect_items():
    items = []
    seen = set()
    for feed_index, feed_url in enumerate(FEEDS, start=1):
        try:
            root = ET.fromstring(fetch_feed(feed_url))
        except Exception as exc:
            print(f"Feed {feed_index} failed: {type(exc).__name__}")
            continue
        for entry in root.findall(".//item"):
            raw_title = entry.findtext("title", "")
            title, source = split_google_title(raw_title)
            url = clean_text(entry.findtext("link", ""))
            summary = clean_text(entry.findtext("description", ""))
            published = parse_date(entry.findtext("pubDate", ""))
            key = re.sub(r"\W+", "", title.lower())[:90]
            if not title or key in seen:
                continue
            seen.add(key)
            item = {
                "title": title,
                "source": source,
                "date": published.date().isoformat(),
                "summary": build_summary(title, source, summary),
                "url": url,
                "_published": published.isoformat(),
            }
            score = entry_score(item)
            if score > 0:
                item["_score"] = score
                items.append(item)
    items.sort(key=lambda item: (item["_published"], item["_score"]), reverse=True)
    return [{k: v for k, v in item.items() if not k.startswith("_")} for item in items[:3]]


def main():
    items = collect_items()
    if not items and OUTPUT.exists():
        print("No fresh news items found; keeping existing file.")
        return
    payload = {
        "updatedAt": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "items": items,
    }
    OUTPUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(items)} news items to {OUTPUT}")


if __name__ == "__main__":
    main()
