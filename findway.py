#!/usr/bin/env python
# -*- coding: utf-8 -*-

import car.car4 as car      
import RPi.GPIO as GPIO
import time

# car已经被封装成一个包

def initgpio():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(8,GPIO.IN)
	GPIO.setup(10,GPIO.IN)
	GPIO.setup(12,GPIO.IN)
	GPIO.setup(16,GPIO.IN)
	pass
# initgpio（）初始化接口

# 小车红外光电传感器根据地面的亮度情况返回探测值，经电压比较器处理器后一般返回0或者1，因此根据返回值确定小车传感器是否探测到黑线
def findway():
	while True:
		if GPIO.input(10)==0 or GPIO.input(12)==0:
			car.go_forward()
			while GPIO.input(10)==1:
				car.turn_right()
			while GPIO.input(12)==1:
				car.turn_left()
			pass
			if GPIO.input(10)==1 and GPIO.input(12)==1:
				while GPIO.input(10)==1 and GPIO.input(12)==1:
					car.go_forward()
			pass
		elif GPIO.input(8)==1 or GPIO.input(16)==1:
			while GPIO.input(8)==1:
				car.turn_right()
			while GPIO.input(16)==1:
				car.turn_left()
		elif GPIO.input(10)==1 or GPIO.input(12)==1:
			while GPIO.input(10)==1:
				car.turn_right()
			while GPIO.input(12)==1:
				car.turn_left()
		else:
			pass
# 如何更有效的根据地面灰度使小车更有效贴着线走，上面给出一种最基础(最笨)的方法

if __name__ == '__main__':
	initgpio()
	findway()
	GPIO.cleanup()
