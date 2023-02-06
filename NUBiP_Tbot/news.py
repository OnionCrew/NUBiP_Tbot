import asyncio
import numpy as np
import requests
import aiohttp
from bs4 import BeautifulSoup as BS

BASE_URL = "https://nubip.edu.ua/news"


    
    async def main():
        async with aiohttp.ClientSession() as session:
            async with session.get(BASE_URL) as response:
                r = await aiohttp.StreamReader.read(response.content)
                soup = BS(r,"html.parser")

                items = soup.find_all("div",{"class": "item newslist"})
                
                addlist= []
                for item in items:

                    h2 = item.find('a').text
                    h4 = item.find('a').get('href')
                
                
                    addlist.append(h2)
                    addlist.append(h4)
                    
                 
                    np.save('ns',addlist)

    if __name__ == '__main__':
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())


