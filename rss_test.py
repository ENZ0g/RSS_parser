from pprint import pprint
from rss_to_parse import Lenta, Interfax, Kommersant, M24

# LENTA

lenta = Lenta()
news = lenta.news(limit=3)
pprint(news)

url = news[0]['link']
data = lenta.grub(url)
pprint(data)

# INTERFAX

interfax = Interfax()
news = interfax.news(limit=5)
pprint(news)

url = news[0]['link']
data = interfax.grub(url)
pprint(data)

# KOMMERSANT

kommersant = Kommersant()
news = kommersant.news(limit=2)
pprint(news)

url = news[0]['link']
data = kommersant.grub(url)
pprint(data)

# M24

m24 = M24()
news = m24.news(4)
pprint(news)

url = news[0]['link']
data = m24.grub(url)
pprint(data)
