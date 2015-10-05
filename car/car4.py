#!/usr/bin/env python
# -*- coding: utf-8 -*-


import RPi.GPIO as GPIO
import sys
import time

state = 'stop'

def init():
    GPIO.setup(3,GPIO.OUT)
    GPIO.setup(5,GPIO.OUT)
    GPIO.setup(7,GPIO.OUT)
    GPIO.setup(11,GPIO.OUT)
    GPIO.setup(13,GPIO.OUT)
    GPIO.setup(15,GPIO.OUT)
    GPIO.setup(19,GPIO.OUT)
    GPIO.setup(21,GPIO.OUT)
 
def stop():
    global state
    if state == 'stop':
        return
    init()
    state = 'stop'
    GPIO.output(3,GPIO.LOW)
    GPIO.output(5,GPIO.LOW)
    GPIO.output(7,GPIO.LOW)
    GPIO.output(11,GPIO.LOW)
    GPIO.output(13,GPIO.LOW)
    GPIO.output(15,GPIO.LOW)
    GPIO.output(19,GPIO.LOW)
    GPIO.output(21,GPIO.LOW)


def go_forward():
    global state
    if state == 'forward':
        return
    init()
    state = 'forward'
    GPIO.output(3,GPIO.HIGH)
    GPIO.output(5,GPIO.LOW)
    GPIO.output(7,GPIO.HIGH)
    GPIO.output(11,GPIO.LOW)
    GPIO.output(13,GPIO.HIGH)
    GPIO.output(15,GPIO.LOW)
    GPIO.output(19,GPIO.HIGH)
    GPIO.output(21,GPIO.LOW)

def go_backward():
    global state
    if state == 'backward':
        return
    init()
    state = 'backward'
    GPIO.output(3,GPIO.LOW)
    GPIO.output(5,GPIO.HIGH)
    GPIO.output(7,GPIO.LOW)
    GPIO.output(11,GPIO.HIGH)
    GPIO.output(13,GPIO.LOW)
    GPIO.output(15,GPIO.HIGH)
    GPIO.output(19,GPIO.LOW)
    GPIO.output(21,GPIO.HIHG)

def turn_right():
    global state
    if state == 'right':
        return
    init()
    state = 'right'
    GPIO.output(3,GPIO.HIGH)
    GPIO.output(5,GPIO.LOW)
    GPIO.output(7,GPIO.HIGH)
    GPIO.output(11,GPIO.LOW)
    GPIO.output(13,GPIO.LOW)
    GPIO.output(15,GPIO.HIGH)
    GPIO.output(19,GPIO.LOW)
    GPIO.output(21,GPIO.HIGH)

def turn_left():
    global state
    if state == 'left':
        return
    init()
    state = 'left'
    GPIO.output(3,GPIO.LOW)
    GPIO.output(5,GPIO.HIGH)
    GPIO.output(7,GPIO.LOW)
    GPIO.output(11,GPIO.HIGH)
    GPIO.output(13,GPIO.HIGH)
    GPIO.output(15,GPIO.LOW)
    GPIO.output(19,GPIO.HIGH)
    GPIO.output(21,GPIO.LOW)

if __name__ == '__main__':
    print 'please import me ~_~ '
    turn_left()
    time.sleep(10)
    stop()


