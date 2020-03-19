# countdown
A simple CLI utility to sleep for a duration whilst providing a visible
 countdown timer.

## Help Message
```
usage: countdown.py [-h] [--unit {h,m,s}] [--refresh INTERVAL] TIME

a simple countdown timer

positional arguments:
  TIME                duration to count down (by default in seconds)

optional arguments:
  -h, --help          show this help message and exit
  --unit {h,m,s}      specifies if TIME is in hours(h), minutes(m), or
                      seconds(s)
  --refresh INTERVAL  how often to refresh the timer (in seconds)
```

## Examples
* `countdown.py --unit h 4` counts down 4 hours
* `countdown.py 60` counts down for 60 seconds
* `countdown.py --refresh 30 --unit m 10` counts 10 minutes, updating the
  display in 30 second intervals. NOTE: the last 30 seconds will count down at
  normal speed. 
