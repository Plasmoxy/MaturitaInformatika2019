from asyncio import sleep, run
import aiohttp
from tkinter import Canvas, Tk
from PIL import Image, ImageTk

host = "https://preview.redd.it/8onlqv5xpg941.jpg?width=640&crop=smart&auto=webp&s=0f5b5d3337e0fbea4c81b29d1737628568460857"

root = Tk()
canv = Canvas(root, width=300, height=300)
canv.pack()

async def fetch(session, url):
    async with session.get(url) as response:
        assert response.status == 200
        return await response.content.read()

def draw():
    global canv
    
    canv.update()
    canv.after(100, draw)

async def main():
    
    ss = aiohttp.ClientSession()
    img = await fetch(ss, host)
    print("ok")
    

    await ss.close()

draw()
run(main())
root.mainloop()