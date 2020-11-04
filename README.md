# RSS_parser

Код позволяет парсить RSS ленты.

Для парсинга RSS достаточно определить класс с указанием url ленты, например:

```python
class Example(RssParser):
    url = "http://rss.feed.com"
```

Метод `news` возвращает список словарей с содержимым ленты. Опционально можно
определить количество возвращаемых словарей (`limit`, по умолчаню, возвращаются
все содержимое ленты):

```python
example = Example()
print(example.news(5))  # вернет 5 последних новостей
```

Формат возвращаемого значения:

```python
[
    {
        'title': 'Example title',
        'link' : 'http://rss.feed.com/1234/',
        'desc' : 'Short description of news',
        'published' : 'dd.mm.yyyy hh:mm'
    }, 
    ... 
]
```

Метод `grub` парсит саму новость. Для его использования необходимо
определить этот метод для каждого нового класса с указанием расположения необходимых элементов:

```python
def grub(self, url):
    tsoup = self.get_soup(url)
    if soup:
        return {'title': itself.get_title(insert bs4 title tag here),
                'image': self.get_img_src(insert bs4 img tag here),
                'content': self.get_p_list(insert list of bs4 p tags here)}
```

Формат возвращаемого значения:

```python
{
    'title' : 'Example title',
    'image' : 'http://rss.feed.com/1234/',
    'content' : [
            list,
            of,
            each,
            paragraph,
            content
        ]
}
```

- `rss_test.py` - примеры применения
- `rss_to_parse.py` - примеры определения классов