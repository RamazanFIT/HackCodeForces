from bs4 import BeautifulSoup
import re
from h import getHtml

# html_content = getHtml('https://codeforces.com/contest/1950/status/E/page/133?order=BY_ARRIVED_DESC')

# # Создаем объект BeautifulSoup
# soup = BeautifulSoup(html_content, 'html.parser')

# # Находим все ссылки, которые подходят под указанный шаблон
# pattern = re.compile(r'/contest/1950/submission/\d+')
# links = soup.find_all('a', href=pattern)

# # Выводим найденные ссылки
# for link in links:
#     print(link['href'])

def getLinks(index):
    html_content = getHtml(f'https://codeforces.com/contest/1950/status/E/page/{index}?order=BY_ARRIVED_DESC')

    soup = BeautifulSoup(html_content, 'html.parser')

    # Находим все ссылки, которые подходят под указанный шаблон
    pattern = re.compile(r'/contest/1950/submission/\d+')
    links = soup.find_all('a', href=pattern)

    # Выводим найденные ссылки
    # for link in links:
    #     print(link['href'])
    return links

# print(getLinks('12')[0]['href'])
