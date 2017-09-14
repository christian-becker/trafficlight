# trafficlight
build a traffic light with Raspberry Pi (Zero) and Pimoroni Blinkt! :vertical_traffic_light: - with or without Docker

Just a simple example of what you can do with Pimoroni Blinkt! on top of the GPIO pins of Raspberry Pi (Zero). 


## how it looks like 
![trafficlight running on Raspberry Pi Zero W with Pimoroni Blinkt!](https://raw.githubusercontent.com/christian-becker/trafficlight/master/trafficlight.gif "trafficlight running on Raspberry Pi Zero W with Pimoroni Blinkt!")


## how to use it

### directly on the device
![GitHub](https://github.com/christian-becker/trafficlight)
```
$ trafficlight/trafficlight.py
```
...if you have Blinkt! already working. (see ![pimoroni/blinkt](https://github.com/pimoroni/blinkt) for details)

### with Docker
![Docker Hub](https://hub.docker.com/r/christianbecker/trafficlight/)
```
$ docker run --rm --cap-add SYS_RAWIO --device /dev/mem christianbecker/trafficlight
```


## Authors
* **Christian Becker** - [christian-becker](https://github.com/christian-becker)

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/christian-becker/trafficlight/blob/master/LICENSE) file for details.

