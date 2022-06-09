import asyncio
import aiohttp
from bs4 import BeautifulSoup


BASE_URL = 'http://127.0.0.1:8000/'


async def main():

    async with aiohttp.ClientSession(BASE_URL) as session:
        async with session.get('/') as resp:
            r_text = await resp.text()
            soup = BeautifulSoup(r_text, 'html.parser')
            categories = soup.select("a[href*=category]")
        for category in categories:
            async with session.get(category.get('href')) as response:
                print(category.getText())
                html = await response.text()
                with open(f'{category.getText()}.txt', 'w') as file:
                    file.write(html)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
