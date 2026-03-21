import asyncio
from pyppeteer import launch

async def get_textarea_content(note_name):
    browser = await launch()
    page = await browser.newPage()
    url = f'https://note.ms/{note_name}'
    try:
        await page.goto(url)
        await page.waitForSelector('textarea.content')
        content = await page.querySelectorEval('textarea.content', 'el => el.value')
        return content
    finally:
        await browser.close()

def get_text(note_name):
    return asyncio.get_event_loop().run_until_complete(get_textarea_content(note_name))

if __name__ == '__main__':
    note_name = input('note.ms/')
    print(get_text(note_name))
