import json
import requests
from bs4 import BeautifulSoup


def get_first_anekdot():

    headers = {
        "user-agent": "Mozilla / 5.0(Windows NT 10.0; Win64;x64) AppleWebKit/537.36 (KHTML,likeGecko) "
                      "Chrome/111.0.0.0 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q = 0.9,image/avif,image/webp,image/apng,"
                  "*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
    }

    url = "https://www.anekdot.ru/last/good/"
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, 'lxml')

    articles_topicbox = soup.find_all("div", class_="topicbox")

    dict_for_anekdots = {}
    for article in articles_topicbox:
        anekdot_data = article.find("div", class_="text")
        anekdot_data = anekdot_data.text.strip() if anekdot_data else None

        article_id_data = article.find(attrs={"data-id": True})
        article_id_data = article_id_data["data-id"] if article_id_data else None

        print(f"{article_id_data} | {anekdot_data}")


        dict_for_anekdots[article_id_data] = {
            "article_anekdot": anekdot_data
        }

        if anekdot_data and article_id_data:
            with open("dict_for_anekdot.json", "w", encoding="utf-8") as file:
                json.dump(dict_for_anekdots, file, indent=4, ensure_ascii=False)


def check_new_anekdot():
    with open("dict_for_anekdot.json", encoding="utf-8") as file:
        dict_for_anekdots = json.load(file)

        headers = {
            "user-agent": "Mozilla / 5.0(Windows NT 10.0; Win64;x64) AppleWebKit/537.36 (KHTML,likeGecko) "
                          "Chrome/111.0.0.0 Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q = 0.9,image/avif,image/webp,image/apng,"
                      "*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
        }

        url = "https://www.anekdot.ru/last/good/"
        r = requests.get(url=url,headers=headers)

        soup = BeautifulSoup(r.text,'lxml')

        articles_topicbox = soup.find_all("div",class_="topicbox")

        fresh_anekdots = {}
        for article in articles_topicbox:
            article_id = article.find(attrs={"data-id": True})
            if article_id:
                article_id = article_id[ "data-id" ]

            if article_id in dict_for_anekdots:
                continue
            else:
                article_anekdot = article.find("div",class_="text")
                if article_anekdot:
                    article_anekdot = article_anekdot.text.strip()
                    # print(article_anekdot)

                article_id = article.find(attrs={"data-id": True})
                if article_id:
                    article_id = article_id[ "data-id" ]

                dict_for_anekdots[article_id] = {
                    "article_anekdot": article_anekdot
                }

                fresh_anekdots[article_id] = {
                    "article_anekdot": article_anekdot
                }

        with open("dict_for_anekdot.json", "w", encoding="utf-8") as file:
            json.dump(dict_for_anekdots, file, indent=4, ensure_ascii=False)

        return fresh_anekdots


def main():
    get_first_anekdot()
    # print(check_new_anekdot())


if __name__ == '__main__':
    main()