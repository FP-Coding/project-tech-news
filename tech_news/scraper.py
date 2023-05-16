from time import sleep
from bs4 import BeautifulSoup
from rich import print
import requests


# Requisito 1
def fetch(url):
    HEADERS = {"user-agent": "Fake user-agent"}
    try:
        sleep(1)
        response = requests.get(url=url, headers=HEADERS, timeout=3)
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    else:
        return response.text


# Requisito 2
def scrape_updates(html_content):
    selector = BeautifulSoup(html_content, "html.parser")
    articles = selector.find_all("article", {"class": "entry-preview"})
    links = [
        article.find("a", {"class": "cs-overlay-link"}).get("href")
        for article in articles
    ]
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = BeautifulSoup(html_content, "html.parser")
    try:
        return selector.find("a", {"class": "next"}).get("href")
    except AttributeError:
        return None


# Requisito 4
def scrape_news(html_content):
    selector = BeautifulSoup(html_content, "html.parser")
    url = selector.find("link", attrs={"rel": "canonical"})["href"]
    title = selector.find("h1", {"class": "entry-title"}).text.strip()
    timestamp = selector.find("li", {"class": "meta-date"}).text
    writer = selector.find("span", {"class": "author"}).a.text
    reading_time = selector.find(
        "li", {"class": "meta-reading-time"}
    ).text.split(" ")[0]
    summary = selector.find("div", {"class": "entry-content"}).p.text.strip()
    category = (
        selector.find("div", {"class": "meta-category"})
        .a.find("span", {"class": "label"})
        .text
    )
    news_info = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": int(reading_time),
        "summary": summary,
        "category": category,
    }
    return news_info


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
