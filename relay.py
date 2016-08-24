#!/usr/bin/env python
import RPi.GPIO as GPIO  # @UnresolvedImport

RelayPin = 11    # pin11

class Switch():
    def on(self):
        print 'Power ON'
        GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
        GPIO.setup(RelayPin, GPIO.OUT)
        GPIO.output(RelayPin, GPIO.HIGH)
    
    def off(self):
        print 'Power OFF'
        GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
        GPIO.setup(RelayPin, GPIO.OUT)
        GPIO.output(RelayPin, GPIO.LOW)
        GPIO.cleanup()                     # Release resource
    