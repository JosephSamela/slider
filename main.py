#!/usr/bin/env python
import RPi.GPIO as GPIO, time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
totalSteps = 5800

def SpinMotor(direction, duration, speed):
	p = GPIO.PWM(16, speed) #Speed in Hz or steps/sec
	GPIO.output(18, direction)
	p.start(1)
	time.sleep(duration)
	p.stop()
	GPIO.cleanup()
	return True

#def SpinMotor(direction, duration):
#	GPIO.output(18, direction)
#	while duration > 0:
#		p.start(1)
#		time.sleep(0.001)
#		duration -= 1
#	p.stop()	
#	GPIO.cleanup()
#	return True

direction = raw_input('Please enter L or R for Left or Right: ')
duration = float(raw_input('Enter duration in seconds: '))
speed = (totalSteps/duration)*6 #Speed in Hz or steps/sec

if direction =='R':
	SpinMotor(False, duration, speed)
elif direction == 'L':
	SpinMotor(True, duration, speed)
else:
	print('Invalid Direction')


