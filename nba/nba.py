import asyncio
from playwright.async_api import async_playwright
from settings import *
from data_fetch import *

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()

        tasks = []
        for key in URLS.keys():
            page = await context.new_page()
            tasks.append(FETCH_FUNC[key](page, URLS[key]))

        await asyncio.gather(*tasks)
        await browser.close()

asyncio.run(main())