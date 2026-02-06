#!/usr/bin/env python3

from __future__ import print_function
from argparse import ArgumentParser
from time import sleep
from datetime import datetime as DateTime, timedelta as TimeDelta

VERSION = '1.1'

start = DateTime.now()
UNIT_DAYS='d'
UNIT_HOURS='h'
UNIT_MINUTES='m'
UNIT_SECONDS='s'

UNIT_MULTIPLIERS = {
    UNIT_DAYS: 86400,
    UNIT_HOURS: 3600,
    UNIT_MINUTES: 60,
    UNIT_SECONDS: 1,
}

def parse_time_string(s):
    """Parse time string like '1d2h30m15s' into total seconds."""
    s = s.lower().strip()
    total_seconds = 0
    current_number = ''

    for char in s:
        if char.isdigit():
            current_number += char
        elif char in UNIT_MULTIPLIERS:
            if not current_number:
                raise ValueError("Missing number before '%s'" % char)
            total_seconds += int(current_number) * UNIT_MULTIPLIERS[char]
            current_number = ''
        else:
            raise ValueError("Invalid character: '%s'" % char)

    if current_number:
        raise ValueError("Time string must end with a unit (d/h/m/s)")

    if total_seconds == 0:
        raise ValueError("Time must be greater than zero")

    return total_seconds

def timeunitmultiplier(time, unit):
    if unit not in (UNIT_HOURS, UNIT_MINUTES, UNIT_SECONDS):
        raise Exception("Unsupported time unit: %s" % unit)
    time_seconds = time
    if unit != UNIT_SECONDS:
        time_seconds = time_seconds * 60
        if unit != UNIT_MINUTES:
            time_seconds = time_seconds * 60
    return time_seconds

def td2str(td):
    d = td.days
    h, r = divmod(td.seconds, 3600)
    m, s = divmod(r, 60)
    shortformat = '{:02}h{:02}m{:02}s'.format(h, m, s)
    if d != 0:
        return '{}d{}'.format(d, shortformat)
    else:
        return shortformat

def clear_screen():
    from os import name as system_type, system
    if system_type == 'nt':
        _ = system('cls')
    elif system_type == 'posix':
        _ = system('clear')
    else:
        raise Exception("System type %s not supported" % system_type)

def main():
    parser = ArgumentParser(description = 'a simple countdown timer')
    parser.add_argument('--version', action='version', version='%(prog)s ' + VERSION)
    parser.add_argument('TIME', default='10s', type=str,
                        help="duration to count down (e.g. 1d2h30m15s, 90m, 30) "
                        "- plain numbers use --unit")
    parser.add_argument('--unit', dest='UNIT', default=None,
                        type=lambda s : s.lower(),
                        choices=[UNIT_HOURS, UNIT_MINUTES, UNIT_SECONDS],
                        help="specifies if TIME is in hours(h), minutes(m), or "
                        "seconds(s) - cannot be used with time strings like 1h30m")
    parser.add_argument('--refresh', dest='INTERVAL', default=1, type=int,
                        help="how often to refresh the timer (in seconds)")
    parser.add_argument('--caffeinate', dest='CAFFEINE', default=False,
                        action='store_true',
                        help="prevent sleep - requires the caffeine library")
    parser.add_argument('--text', dest='TEXT', default=None, type=str,
                        help="text to display along with the timer")
    parser.add_argument('--textfile', dest='TEXTFILE', default=None, type=str,
                        help="path to a file containing text to display")
    args = parser.parse_args()

    if args.INTERVAL <= 0:
        raise Exception("Negative time values are not supported")

    interval = TimeDelta(seconds=args.INTERVAL)

    # Support both "1d2h30m15s" format and plain integer with --unit
    if args.TIME.isdigit():
        unit = args.UNIT if args.UNIT is not None else UNIT_SECONDS
        duration_seconds = timeunitmultiplier(int(args.TIME), unit)
    else:
        if args.UNIT is not None:
            raise ValueError(
                "--unit cannot be used with time strings like '%s'" % args.TIME)
        duration_seconds = parse_time_string(args.TIME)
    duration = TimeDelta(seconds=duration_seconds)
    td_zero = TimeDelta(seconds=0)
    end = start + duration
    current = start

    text = ""

    if args.TEXT is not None:
        text = args.TEXT
    elif args.TEXTFILE is not None:
        with open(args.TEXTFILE, 'r') as f:
            text = f.read()

    if args.CAFFEINE is True:
        try:
            import caffeine
            caffeine.on(display=True)
        except ImportError:
            text = "ERROR: caffeine not found; try `pip3 install caffeine`\n\n" + text

    while current < end:
        clear_screen()
        current = DateTime.now()
        remaining = end - current
        if remaining < td_zero:
            break
        print("%s remaining of %s" % (td2str(remaining), td2str(duration)))
        if text:
            print("\n" + text)
        if interval >= remaining:
            sleep(1)
        else:
            sleep(interval.seconds)

    clear_screen()
    print("completed timer for %s seconds" % duration.seconds)
    if args.CAFFEINE is True:
        caffeine.off()

if __name__ == '__main__':
    main()
