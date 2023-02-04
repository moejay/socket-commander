# Socket commands

Allows you to send commands via websockets
main use is to send commands using Bitfocus companion
to a computer running an instalink cam (using v4l)
and sets ptz configuration

## Running

* Run `python main.py`
* Connect with a websocket client

```
.json
{
	"deviceName": "/dev/video0",
	"inputSettings": {
		"pan": 10000,
		"tilt": 10000,
		"zoom": 100
		}
}
```

## What about security

There isn't any atm, will prbably add websocket authentication
and input validation.

DO NOT USE THIS SOFTWARE
