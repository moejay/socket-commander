#!/usr/bin/env python

import asyncio
import websockets
import json
import os 

def _move_device(options):
    try:
        device = options['device']
        pan = options['pan']
        tilt = options['tilt']
        zoom = options['zoom']
    except KeyError as e:
        return "Missing data"

    command = f"v4l2-ctl -c pan_absolute={pan},tilt_absolute={tilt},zoom_absolute={zoom} -d {device}"
    return os.system(command)



OPERATION_MAP={
        "move": _move_device 
}

#
# main handler for incoming messages
# parse into json
# call operation function with options
async def _handle(websocket, path):
    async for message in websocket:
        parsed = json.loads(message)
        operation = parsed["operation"]
        options = parsed["options"]
        func_to_call = OPERATION_MAP[operation.lower()]
        if not func_to_call:
            websocket.send("ERROR")
            continue
        websocket.send(func_to_call(options))

    
async def main():
    async with websockets.serve(_handle, "0.0.0.0", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())
