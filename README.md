# Socket commands

Allows you to send commands via websockets
main use is to send commands using Bitfocus companion
to a computer running an instalink cam (using v4l)
and sets ptz configuration

## Running

* Run `python main.py`
* Connect with a websocket client

```
{
	"operation": "move",
	"options": {
		"device": "/dev/video0",
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

## Future plans

* [] List devices
* [] Use device name instead of /in addition to path
* [] Relative movement option (ie: pan + 10, zoom - 30)
* [] Saving commands/Trigger saved commands
* [] Program arguments ( eg: listen address, port )
* [] Web interface to do all these things


