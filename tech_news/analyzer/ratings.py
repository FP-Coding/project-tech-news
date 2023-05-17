from tech_news.database import search_news
from collections import Counter


# Requisito 10
def top_5_categories():
    all_news = Counter([new["category"] for new in search_news({})])
    categories = [category for category in all_news.items()]
    categories.sort(key=lambda x: x[0])
    categories.sort(key=lambda x: x[1], reverse=True)
    list = [category[0] for category in categories]
    return list[:5]
