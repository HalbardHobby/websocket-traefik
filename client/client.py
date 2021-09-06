from asyncio.tasks import sleep
import websockets
import asyncio

async def listen():
    url = "ws://localhost:8080"
    async with websockets.connect(url) as ws:
        await ws.send("hello, there!")

        while True:
            msg = await  ws.recv()
            print(msg)
            await sleep(1)

            await ws.send("hello, again!")

asyncio.get_event_loop().run_until_complete(listen())
