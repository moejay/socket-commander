# MIT License
# 
# Copyright (c) 2023 Mouhammad Ali Al Jajeh
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# 
# !/usr/bin/env python

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
