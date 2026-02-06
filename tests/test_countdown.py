#!/usr/bin/env python
from __future__ import print_function
import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from datetime import timedelta as TimeDelta
from countdown import (
    parse_time_string,
    timeunitmultiplier,
    td2str,
    UNIT_HOURS,
    UNIT_MINUTES,
    UNIT_SECONDS,
)


class TestParseTimeString(unittest.TestCase):

    def test_seconds_only(self):
        self.assertEqual(parse_time_string('30s'), 30)

    def test_minutes_only(self):
        self.assertEqual(parse_time_string('5m'), 300)

    def test_hours_only(self):
        self.assertEqual(parse_time_string('2h'), 7200)

    def test_days_only(self):
        self.assertEqual(parse_time_string('1d'), 86400)

    def test_combined(self):
        self.assertEqual(parse_time_string('1d2h30m15s'), 86400 + 7200 + 1800 + 15)

    def test_partial_combined(self):
        self.assertEqual(parse_time_string('1h30m'), 5400)

    def test_uppercase(self):
        self.assertEqual(parse_time_string('1H30M'), 5400)

    def test_missing_number(self):
        with self.assertRaises(ValueError):
            parse_time_string('h')

    def test_invalid_character(self):
        with self.assertRaises(ValueError):
            parse_time_string('10x')

    def test_no_unit(self):
        with self.assertRaises(ValueError):
            parse_time_string('100')

    def test_zero_time(self):
        with self.assertRaises(ValueError):
            parse_time_string('0s')


class TestTimeUnitMultiplier(unittest.TestCase):

    def test_seconds(self):
        self.assertEqual(timeunitmultiplier(30, UNIT_SECONDS), 30)

    def test_minutes(self):
        self.assertEqual(timeunitmultiplier(5, UNIT_MINUTES), 300)

    def test_hours(self):
        self.assertEqual(timeunitmultiplier(2, UNIT_HOURS), 7200)

    def test_invalid_unit(self):
        with self.assertRaises(Exception):
            timeunitmultiplier(10, 'x')


class TestTd2Str(unittest.TestCase):

    def test_seconds_only(self):
        self.assertEqual(td2str(TimeDelta(seconds=45)), '00h00m45s')

    def test_minutes_and_seconds(self):
        self.assertEqual(td2str(TimeDelta(seconds=125)), '00h02m05s')

    def test_hours_minutes_seconds(self):
        self.assertEqual(td2str(TimeDelta(seconds=3661)), '01h01m01s')

    def test_with_days(self):
        self.assertEqual(td2str(TimeDelta(days=2, seconds=3600)), '2d01h00m00s')


if __name__ == '__main__':
    unittest.main()
