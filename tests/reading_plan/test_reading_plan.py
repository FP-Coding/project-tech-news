import pytest
from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)  # noqa: F401, E261, E501


@pytest.fixture
def news():
    return [
        {
            "url": "https://blog.betrybe.com/tecnologia/site-responsivo/",
            "title": "Site responsivo: o que é e 10 dicas para aplicar",
            "timestamp": "10/05/2023",
            "writer": "Lucas Marchiori",
            "reading_time": 10,
            "summary": "Com o avanço da tecnologia, grande parte das pessoas possui um celular para realizar suas tarefas. Por isso, hoje em dia pessoas programadoras dificilmente fazem aplicações somente para desktops ou notebooks e criar um site responsivo passou a ser prioridade para as organizações.",  # noqa: E501
            "category": "Tecnologia",
        },
        {
            "url": "https://blog.betrybe.com/tecnologia/modelo-as-a-service/",
            "title": "SaaS, GaaS, IaaS, DaaS, PaaS: entenda o modelo as a service",  # noqa: E501
            "timestamp": "27/04/2023",
            "writer": "Cairo Noleto",
            "reading_time": 10,
            "summary": "Você sabe o que é computação em nuvem? Se você já usou armazenamento no Google Drive ou editou documentos em softwares on-line, já utilizou o modelo as a service, que é a base da distribuição de recursos de computação em nuvem no mercado.",  # noqa: E501
            "category": "Tecnologia",
        },
        {
            "url": "https://blog.betrybe.com/tecnologia/armazenamento-em-nuvem/",  # noqa: E501
            "title": "Armazenamento em nuvem: o que é e quais os 7 melhores?",
            "timestamp": "20/04/2023",
            "writer": "Cairo Noleto",
            "reading_time": 20,
            "summary": "Em algum momento você já se perguntou se é seguro manter seus dados armazenados dentro de um pendrive ou HD externo. Pois bem, supondo que você tem toda sua vida salva em um HD e ele queima, como ter seus dados em mãos novamente?",  # noqa: E501
            "category": "Tecnologia",
        },
        {
            "url": "https://blog.betrybe.com/tecnologia/componentizacao-tudo-sobre/",  # noqa: E501
            "title": "Componentização: o que é, por que usar e exemplo na prática!",  # noqa: E501
            "timestamp": "17/04/2023",
            "writer": "Cairo Noleto",
            "reading_time": 30,
            "summary": "Se você é uma pessoa programadora, desenvolvedora ou até mesmo deseja se tornar uma, provavelmente já ouviu falar sobre componentização.",  # noqa: E501
            "category": "Tecnologia",
        },
    ]


@pytest.fixture
def expected_result():
    return {
        "readable": [
            {
                "chosen_news": [
                    ("Site responsivo: o que é e 10 dicas para aplicar", 10)
                ],
                "unfilled_time": 10,
            },
            {
                "chosen_news": [
                    (
                        "SaaS, GaaS, IaaS, DaaS, PaaS: entenda o modelo as a service",  # noqa: E501
                        10,
                    )
                ],
                "unfilled_time": 10,
            },
            {
                "chosen_news": [
                    (
                        "Armazenamento em nuvem: o que é e quais os 7 melhores?",  # noqa: E501
                        20,
                    )
                ],
                "unfilled_time": 0,
            },
        ],
        "unreadable": [
            (
                "Componentização: o que é, por que usar e exemplo na prática!",
                30,
            )
        ],
    }


def test_reading_plan_group_news(mocker, news, expected_result):
    with pytest.raises(
        ValueError, match="Valor 'available_time' deve ser maior que zero"
    ):
        ReadingPlanService.group_news_for_available_time(0)

    mocker.patch.object(
        ReadingPlanService, "_db_news_proxy", return_value=news
    )

    class_reading = ReadingPlanService()

    result = class_reading.group_news_for_available_time(20)

    assert result == expected_result
