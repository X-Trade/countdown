# countdown
A simple CLI utility to sleep for a duration whilst providing a visible
 countdown timer.

## Help Message
```
usage: countdown.py [-h] [--version] [--unit {h,m,s}] [--refresh INTERVAL]
                    [--caffeinate] [--text TEXT] [--textfile TEXTFILE] TIME

a simple countdown timer

positional arguments:
  TIME                 duration to count down (e.g. 1d2h30m15s, 90m, 30)

optional arguments:
  -h, --help           show this help message and exit
  --version            show program's version number and exit
  --unit {h,m,s}       specifies if TIME is in hours(h), minutes(m), or
                       seconds(s) - cannot be used with time strings like 1h30m
  --refresh INTERVAL   how often to refresh the timer (in seconds)
  --caffeinate         prevent sleep (requires caffeine library)
  --text TEXT          text to display with each refresh
  --textfile TEXTFILE  path to a file containing text to display
```

## Examples
* `countdown.py 1h30m` counts down 1 hour 30 minutes
* `countdown.py 2d4h` counts down 2 days and 4 hours
* `countdown.py --unit h 4` counts down 4 hours
* `countdown.py 60` counts down for 60 seconds
* `countdown.py 10m --text "Take a break!"` displays a message with the timer
* `countdown.py --refresh 30 --unit m 10` counts 10 minutes, updating the
  display in 30 second intervals. NOTE: the last 30 seconds will count down at
  normal speed.
