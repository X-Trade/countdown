#!/usr/bin/env python3

from __future__ import print_function
from argparse import ArgumentParser
from time import sleep
from datetime import datetime as DateTime, timedelta as TimeDelta

start = DateTime.now()
UNIT_HOURS='h'
UNIT_MINUTES='m'
UNIT_SECONDS='s'

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
    parser.add_argument('TIME', default=10, type=int,
                        help="duration to count down (by default in seconds)")
    parser.add_argument('--unit', dest='UNIT', default=UNIT_SECONDS,
                        type=lambda s : s.lower(),
                        choices=[UNIT_HOURS, UNIT_MINUTES, UNIT_SECONDS],
                        help="specifies if TIME is in hours(h), minutes(m), or seconds(s)")
    parser.add_argument('--refresh', dest='INTERVAL', default=1, type=int,
                        help="how often to refresh the timer (in seconds)")
    parser.add_argument('--caffeinate', dest='CAFFEINE', default=False, action='store_true',
                        help="prevent sleep - requires the caffeine library to \
                        be installed")
    parser.add_argument('--text', dest='TEXT', default=None, type=str,
                        help="text to display with each refresh")
    parser.add_argument('--textfile', dest='TEXTFILE', default=None, type=str,
                        help="path to a file containing text to display with each refresh")
    args = parser.parse_args()

    if args.TIME <= 0 or args.INTERVAL <= 0:
        raise Exception("Negative time values are not supported")

    interval = TimeDelta(seconds=args.INTERVAL)
    duration = TimeDelta(seconds=timeunitmultiplier(args.TIME, args.UNIT))
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
        except ModuleNotFoundError:
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
