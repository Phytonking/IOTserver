#!/usr/bin/env python

import asyncio
import websockets
import public_ip as ip
from command_manager import *


async def hello(websocket):
    command = await websocket.recv()
    print(f"<<< {command}")

    #greeting = f"Hello {name}!"
    x = command_center(command)

    await websocket.send(x)
    print(f">>> {x}")

async def main():
    port = 5000
    host = '192.168.86.29'
    async with websockets.serve(hello, host, port):
        print(f"Processor Server set to {host}:{port}")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
    