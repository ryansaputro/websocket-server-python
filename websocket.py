import asyncio
import websockets

connected = set()

async def server(websocket, path):
    # Register.
    connected.add(websocket)
    try:
        print(f"Author Ryan Saputro");
        print(f"Email ryansaputro52@gmail.com");
        print(f"Versi Aplikasi v.1.1");
        async for message in websocket:
            for conn in connected:
                await conn.send(message)
                print(f"Receive Data > {message}")
    finally:
        # Unregister.
        connected.remove(websocket)

start_server = websockets.serve(server, "127.0.0.1", 5000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
