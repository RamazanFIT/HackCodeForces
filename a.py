import asyncio
from pyppeteer import launch

async def getCode(url):
    browser = await launch(headless=True)
    page = await browser.newPage()
    
    # Открываем страницу
    await page.goto(url)

    # Находим элемент с идентификатором "#program-source-text" и получаем его содержимое
    source_element = await page.querySelector('#program-source-text')
    if source_element:
        # Используем innerText вместо textContent для сохранения форматирования
        copied_text = await page.evaluate('(element) => element.innerText', source_element)
        text = copied_text.strip()
        await browser.close()
        return text
        

# Пример вызова функции и получения отформатированного текста
# formatted_code = asyncio.run(getCode('https://codeforces.com/contest/1950/submission/253686995'))
# print(formatted_code)
