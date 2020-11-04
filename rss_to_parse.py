from rss_parser import RssParser


class Lenta(RssParser):
    url = 'http://lenta.ru/rss'

    def grub(self, url):
        soup = self.get_soup(url)
        if soup:
            return {'title': self.get_title(soup.find('h1')),
                    'image': self.get_img_src(soup.find('div', attrs={'class': 'b-topic__title-image'}).find('img')),
                    'content': self.get_p_list(soup.find('div', attrs={'itemprop': 'articleBody'}).find_all('p'))}


class Interfax(RssParser):
    url = 'http://www.interfax.ru/rss.asp'

    def grub(self, url):
        soup = self.get_soup(url)
        if soup:
            return {'title': self.get_title(soup.find('h1')),
                    'image': self.get_img_src(soup.find('article').find('figure', attrs={'class': 'inner'})),
                    'content': self.get_p_list(soup.find('article').find_all('p'))}


class Kommersant(RssParser):
    url = 'http://www.kommersant.ru/RSS/news.xml'

    def grub(self, url):
        soup = self.get_soup(url)
        if soup:
            return {'title': self.get_title(soup.find('h1')),
                    'image': 'no img',
                    'content': self.get_p_list(soup.find('div', attrs={'class': 'article_text_wrapper'}).find_all('p'))}


class M24(RssParser):
    url = 'http://www.m24.ru/rss.xml'

    def grub(self, url):
        soup = self.get_soup(url)
        if soup:
            return {'title': self.get_title(soup.find('h1')),
                    'image': self.get_img_src(soup.find('div', attrs={'class': 'b-material-incut-m-image'}).find('img')),
                    'content': self.get_p_list(soup.select('.js-mediator-article > p'))}
