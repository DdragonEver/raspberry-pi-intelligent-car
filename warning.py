#!/usr/bin/env python


import RPi.GPIO as GPIO      
import time
#import python GPIO库

def init():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(8,GPIO.OUT)
	GPIO.setup(10,GPIO.IN)
	GPIO.setup(12,GPIO.OUT)
    pass
# 对GPIO接口进行初始化


def  beep():
 	while GPIO.input(10):
 		GPIO.output(8,GPIO.HIGH)
 		time.sleep(0.5)
 		GPIO.output(8,GPIO.LOW)
 		time.sleep(0.5)
 		
# 定义beep函数 当热释电红外传感检测到有移动物体时 8端口输出高电平

def detect():
 	for i in range(1,8888):
 		if GPIO.input(10)==1:
 			beep()
 			print"Someone is closing!!"
 		else:
 			GPIO.output(8,GPIO.LOW)
 			GPIO.Output(12,GPIO.LOW)
 			print"Nobody"
 		time.sleep(2)

# 定义检测函数

if __name__ == "__main__":
	init()
	detect()