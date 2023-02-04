#!/usr/bin/env python

import asyncio
import websockets
import json
import os 

async def echo(websocket, path):
    async for message in websocket:
        parsed = json.loads(message)
        dev = parsed["device"]
        pan = parsed["inputSettings"]["pan"]
        tilt = parsed["inputSettings"]["tilt"]
        zoom = parsed["inputSettings"]["zoom"]
        print(f"Setting dev {dev} pan: {pan} | tilt: {tilt} | zoom: {zoom}")
        # validate dev/pan/tilt/zoom values
        command = f"v4l2-ctl -c pan_absolute={pan},tilt_absolute={tilt},zoom_absolute={zoom} -d {dev}"
        print(os.system(command))
        #websocket.send(message)

async def main():
    async with websockets.serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())
