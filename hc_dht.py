#yujeong

import time
import sys
from pymata4 import pymata4

POLL_TIME = 5  # number of seconds between polls

# Callback data indices
CB_PIN_MODE = 0
CB_PIN = 1
CB_VALUE = 2
CB_TIME = 3


def the_callback(data):

    if not data[3]:
        tlist = time.localtime(data[6])
        ftime = f'{tlist.tm_year}-{tlist.tm_mon:02}-{tlist.tm_mday:02} ' \
                f'{tlist.tm_hour:02}:{tlist.tm_min:0}:{tlist.tm_sec:02}'

        print(f'Pin: {data[1]} DHT Type: {data[2]} Humidity:{data[4]}, '
              f'Temperature: {data[5]} Timestamp: {ftime}')


def dht(my_board, callback=None):

    # set the pin mode - for pin 6 differential is set explicitly
    my_board.set_pin_mode_dht(4, sensor_type=11, differential=.05, callback=callback)
    # my_board.set_pin_mode_dht(9, sensor_type=22, differential=.05, callback=callback)

    # my_board.set_pin_mode_dht(10, sensor_type=22, differential=.05, callback=callback)
    # my_board.set_pin_mode_dht(11, sensor_type=11, differential=.05, callback=callback)

    # a flag to change the differential value after the first 5 seconds
    changed = False
    while True:
        try:
            time.sleep(POLL_TIME)

            # poll the first dht
            value = board.dht_read(4)

            # format the time string and then print the data
            tlist = time.localtime(value[2])
            ftime = f'{tlist.tm_year}-{tlist.tm_mon:02}-{tlist.tm_mday:02} ' \
                    f'{tlist.tm_hour:02}:{tlist.tm_min:0}:{tlist.tm_sec:02}'
            print(f'poll pin 8: humidity={value[0]} temp={value[1]} '
                  f'time of last report: {ftime}')

            # poll the second DHT and print the values
            value = board.dht_read(9)
            tlist = time.localtime(value[2])
            ftime = f'{tlist.tm_year}-{tlist.tm_mon:02}-{tlist.tm_mday:02} ' \
                    f'{tlist.tm_hour:02}:{tlist.tm_min:0}:{tlist.tm_sec:02}'
            print(f'poll pin 9: humidity={value[0]} temp={value[1]} '
                  f'time of last report: {ftime}')

            # poll the third dht

            # value = board.dht_read(10)

            # format the time string and then print the data
            # tlist = time.localtime(value[2])
            # ftime = f'{tlist.tm_year}-{tlist.tm_mon:02}-{tlist.tm_mday:02} ' \
            #         f'{tlist.tm_hour:02}:{tlist.tm_min:0}:{tlist.tm_sec:02}'
            # print(f'poll pin 10: humidity={value[0]} temp={value[1]} '
            #       f'time of last report: {ftime}')

            # poll the fourth DHT
            # value = board.dht_read(11)
            # tlist = time.localtime(value[2])
            # ftime = f'{tlist.tm_year}-{tlist.tm_mon:02}-{tlist.tm_mday:02} ' \
            #         f'{tlist.tm_hour:02}:{tlist.tm_min:0}:{tlist.tm_sec:02}'
            # print(f'poll pin 11: humidity={value[0]} temp={value[1]} '
            #       f'time of last report: {ftime}')
            # if not changed:
                # explicitly change the differential values

            #     my_board.set_pin_mode_dht(8, sensor_type=11, differential=2.0,
            #                               callback=callback)
            #     my_board.set_pin_mode_dht(9, sensor_type=22, differential=20.0,
            #                               callback=callback)
            #     my_board.set_pin_mode_dht(10, sensor_type=22, differential=20.0,
            #                               callback=callback)
            #     my_board.set_pin_mode_dht(11, sensor_type=11, differential=2.0,
            #                               callback=callback)
            #     changed = True
        except KeyboardInterrupt:
            board.shutdown()
            sys.exit(0)


board = pymata4.Pymata4()

try:
    dht(board, the_callback)
except KeyboardInterrupt:
    board.shutdown()
