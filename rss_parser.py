from bs4 import BeautifulSoup
import feedparser
import requests
import validators
import unicodedata


class RssParser:
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:80.0) Gecko/20100101 Firefox/80.0'
    url = None

    @staticmethod
    def get_article_pub_date_time(article):
        date_time = article.get('published_parsed')
        if date_time:
            return "{1:02}.{2:02}.{0} {3:02}:{4:02}".format(*date_time)
        return

    def get_news_from_feed(self, feed, limit):
        news = []
        for article in feed.entries[:limit]:
            news.append({
                'title': article.get('title'),
                'link': article.get('link'),
                'desc': article.get('description'),
                'published': self.get_article_pub_date_time(article)
            })
        return news

    def news(self, limit=None):
        if not validators.url(self.url):
            print(f'NEWS: {self.__class__.__name__}: Not valid URL: {self.url}')
            return -1

        feed = feedparser.parse(self.url, agent=self.user_agent)
        if feed.status == 200 or feed.status == 302:
            return self.get_news_from_feed(feed, limit)
        elif feed.status == 301:
            self.url = feed.href
            return self.news(limit)
        elif feed.status == 410:
            print(f'NEWS: Permanently deleted: {self.url}')
            return -1
        else:
            print(f'NEWS: Something wrong with: {self.url}\nHttp status - {feed.status}')
            return -1

    def get_soup(self, url):
        if not validators.url(url):
            print(f'GRUB: {self.__class__.__name__}: Not valid URL: {url}')
            return
        html = requests.get(url, headers={'user-agent': self.user_agent})
        if html.status_code == 200:
            return BeautifulSoup(html.content, "html.parser")
        print(f'GRUB: Something wrong with: {self.url}\nHttp status - {html.status_code}')

    @staticmethod
    def get_img_src(bs4_image):
        if bs4_image:
            return bs4_image.get('src')
        return 'no img'

    @staticmethod
    def get_title(bs4_title):
        return unicodedata.normalize("NFKD", bs4_title.string)

    @staticmethod
    def get_p_list(bs4_p_list):
        return [p.text for p in bs4_p_list]

    def grub(self, url):
        return f"You must override method grab for {self.__class__.__name__}:\n"\
               "\tdef grub(self, url):\n"\
               "\t\tsoup = self.get_soup(url)\n"\
               "\t\tif soup:\n"\
               "\t\t\treturn {'title': itself.get_title(insert bs4 title tag here),\n"\
               "\t\t\t\t\t'image': self.get_img_src(insert bs4 img tag here),\n"\
               "\t\t\t\t\t'content': self.get_p_list(insert list of bs4 p tags here)}"
