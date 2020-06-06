#!/usr/bin/env python3
'''
This is a script that gives out how much time has passed in the past year or week or day.
'''
import sys
import time
from datetime import datetime, timedelta


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    ITALIC = '\033[3m'


def print_year(now):
    BOLDRED = color.BOLD + color.RED
    BOLDCYAN = color.BOLD + color.CYAN
    print(color.YELLOW+'YEAR: '+color.END, end='')
    print(BOLDRED+str(now.tm_yday)+color.END+' days passed, ', end='')
    print(BOLDRED+str(366-now.tm_yday)+color.END+' days left. ', end='')
    print(BOLDCYAN+f'{int(now.tm_yday/366*100)}%'+color.END+' used.')


def print_week(now):
    BOLDGREEN = color.BOLD + color.GREEN
    print(color.YELLOW+'WEEK: '+color.END, end='')
    print(BOLDGREEN+f'{now.tm_wday}'+color.END+' days '+BOLDGREEN+f'{now.tm_hour}'+color.END+' hours passed.')


def print_day(now):
    BB = color.BOLD + color.BLUE
    END = color.END
    tomorrow = time.strptime(f'{now.tm_year} {now.tm_yday+1}', '%Y %j')  # time of 00:00:00 of tomorrow
    dt_tomorrow = datetime.fromtimestamp(time.mktime(tomorrow))  # datetime of 00:00:00 of tomorrow
    delta = dt_tomorrow - datetime.now()  # time left for today
    left = str(delta).split('.')[0].split(':')  # ['h', 'm', 's']
    print(color.YELLOW+' DAY: '+END, end='')
    print(BB+f'{left[0]}'+END+' hours '+BB+f'{left[1]}'+END+' minutes '+BB+f'{left[2]}'+END+' seconds left.', end=' ')
    used_second = 3600 * int(left[0]) + 60 * int(left[1]) + int(left[2])
    propotion = 100 - int(used_second / 864)
    print(color.BOLD+color.CYAN+f'{propotion}%'+END+' used.')


def main():
    now = time.localtime()
    if '-y' in sys.argv or not sys.argv[1:]:
        print_year(now)
    if '-w' in sys.argv or not sys.argv[1:]:
        print_week(now)
    if '-d' in sys.argv or not sys.argv[1:]:
        print_day(now)


if __name__ == "__main__":
    main()
