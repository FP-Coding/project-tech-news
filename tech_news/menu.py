import sys
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_category,
)
from tech_news.scraper import get_tech_news
from tech_news.analyzer.ratings import top_5_categories

STRING_OPTIONS = """
Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por categoria;
 4 - Listar top 5 categorias;
 5 - Sair.
"""


def handle_menu_option(option):
    funcs = [
        (get_tech_news, "Digite quantas notícias serão buscadas:"),
        (search_by_title, "Digite o título:"),
        (search_by_date, "Digite a data no formato aaaa-mm-dd:"),
        (search_by_category, "Digite a categoria:"),
        (top_5_categories, None),
    ]

    if option == 0:
        data = input(funcs[option][1])
        result = funcs[option][0](int(data))
        print(result)
    elif option == 5:
        print("Encerrando script")
    elif option in range(1, 4):
        data = input(funcs[option][1])
        result = funcs[option][0](data)
        print(result)
    else:
        print(funcs[option][0]())


# Requisitos 11 e 12
def analyzer_menu():
    try:
        option = int(input(STRING_OPTIONS))
        handle_menu_option(option)
    except (IndexError, ValueError):
        print("Opção inválida", file=sys.stderr)


analyzer_menu()
