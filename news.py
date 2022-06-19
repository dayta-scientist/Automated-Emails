# Api key: eced2b38b971472f8eb0df8177b58400
import requests
import api_key
from pprint import pprint


class NewsFeed:
    """Representing multiple news titles and links as a single string"""
    base_url = "https://newsapi.org/v2/everything?"
    api_key = api_key.main()

    def __init__(self, interest, from_date, to_date, language='en'):
        self.language = language
        self.from_date = from_date
        self.to_date = to_date
        self.interest = interest

    def get(self):
        url = self._build_url()

        articles = self._get_articles(url)

        email_body = ''
        for article in articles:
            email_body = email_body + article['title'] + "\n" + article['url'] + "\n\n"

        return email_body

    def _get_articles(self, url):
        response = requests.get(url)
        # content = response.text
        content = response.json()
        # x = content['articles'][2]['url']
        articles = content['articles']
        # print(x)
        # pprint(content)
        return articles

    def _build_url(self):
        url = f"{self.base_url}" \
              f"qInTitle={self.interest}&" \
              f"from={self.from_date}&" \
              f"to={self.to_date}&" \
              f"language={self.language}&" \
              f"apiKey={self.api_key}"
        return url


if __name__ == "__main__":
    news_feed = NewsFeed(interest="bitcoin", from_date="2022-06-16", to_date="2022-06-17", language="en")
    print(news_feed.get())
