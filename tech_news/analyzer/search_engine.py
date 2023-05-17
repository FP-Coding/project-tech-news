from tech_news.database import search_news
from datetime import datetime
import re

DATA_REGEX = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def format_response(news):
    return [(new["title"], new["url"]) for new in news]


# Requisito 7
def search_by_title(title):
    news = search_news({"title": {"$regex": title, "$options": "i"}})
    return format_response(news)


# Requisito 8
def search_by_date(date):
    try:
        info_date = date.split("-")
        formated_date = (
            datetime(int(info_date[0]), int(info_date[1]), int(info_date[2]))
            .date()
            .strftime("%d/%m/%Y")
        )
    except ValueError:
        raise ValueError("Data inválida")
    else:
        news = search_news({"timestamp": formated_date})
        return format_response(news)


# Requisito 9
def search_by_category(category):
    news = search_news({"category": {"$regex": category, "$options": "i"}})
    return format_response(news)
