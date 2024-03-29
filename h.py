import requests

# URL-адрес веб-страницы
# url = 'https://example.com'

# response = requests.get(url)

# # Проверяем успешность запроса
# if response.status_code == 200:
#     # Получаем HTML-код страницы
#     html_content = response.text
#     print(html_content)
# else:
#     print('Произошла ошибка при загрузке страницы:', response.status_code)

def getHtml(url):
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
        # print(html_content)
        return html_content