import sys
import time

from pymata4 import pymata4

"""
Setup a pin for digital output and output a signal
and toggle the pin. Do this 4 times.
"""

# some globals
DIGITAL_PIN = 13  # arduino pin number
#define DIGITAL_PIN 13

def blink(my_board, pin):
    """
    This function will to toggle a digital pin.

    :param my_board: an PymataExpress instance
    :param pin: pin to be controlled
    """

    # set the pin mode
    my_board.set_pin_mode_digital_output(pin)  #pymata4에 들어있는 함수
                                         #=> set_pin_mode_digital_output
    # toggle the pin 4 times and exit     => digital_write
    for x in range(100):
        print("x=",x)                  #반복 횟수
        print('ON')
        my_board.digital_write(pin, 1) #1은 켜라
        time.sleep(0.5)                #0.5초마다
        print('OFF')
        my_board.digital_write(pin, 0) #0은 꺼라
        time.sleep(0.5)

    my_board.shutdown() #shell에서 나와라

#board = my_board / DIGITAL_PIN = pin
board = pymata4.Pymata4()      #생성자를 통해서 객체 만
try:                           #코드블록에 오류가 있는지 테스트
    blink(board, DIGITAL_PIN)  #위에서 만든 board를 blink라는 함수의 파라미터로 사용
except KeyboardInterrupt:
    print("I am exciting")
    board.shutdown()   
    sys.exit(0)