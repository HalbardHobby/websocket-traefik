import websockets
import asyncio

port = 8080

print("Listening on port " + str(port))

async def echo(ws, path):
    print("new connection")
    try:
        async for msg in ws:
            print("Received message from client: " + msg)
            await ws.send("Pong: " + msg)
    except websockets.exceptions.ConnectionClosed:
        print ("Client disconnected")

start_server = websockets.serve(echo, "0.0.0.0", port)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
