import time
import atexit
import sys
import RPi.GPIO as GPIO

from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)

class robots():
    def __init__(self):
        self.leftm
        self.rightm
    
    # recommended for auto-disabling motors on shutdown!
    def turnOffMotors(self):
        mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)
    
    def motors(self):
        
        atexit.register(turnOffMotors)

        self.leftm = mh.getMotor(1)
        self.rightm = mh.getMotor(3)

        # set the speed to start, from 0 (off) to 255 (max speed)
        self.leftm.setSpeed(150)
        self.rightm.setSpeed(150)

        while (True):
            print("Forward! ")
            self.leftm.run(Adafruit_MotorHAT.FORWARD)
            self.rightm.run(Adafruit_MotorHAT.FORWARD)
    
            print("\tSpeed up...")
            for i in range(255):
                self.leftm.setSpeed(i)
                self.rightm.setspeed(i)
                time.sleep(0.01)

            print("\tSlow down...")
            for i in reversed(range(255)):
                self.leftm.setSpeed(i)
                self.rightm.setspeed(i)
                time.sleep(0.01)

            print("Backward! ")
            self.leftm.run(Adafruit_MotorHAT.BACKWARD)
            self.rightm.run(Adafruit_MotorHAT.BACKWARD)

            print("\tSpeed up...")
                for i in range(255):
                self.leftm.setSpeed(i)
                self.rightm.setspeed(i)
                time.sleep(0.01)
    
            print("\tSlow down...")
                for i in reversed(range(255)):
                self.leftm.setSpeed(i)
                self.rightm.setspeed(i)
                time.sleep(0.01)

            print("Release")
                self.leftm.run(Adafruit_MotorHAT.RELEASE)
                self.rightm.run(Adafruit_MotorHAT.RELEASE)
                time.sleep(1.0)
            
            
    def leftSensor(self, sensor):
        # Disable any warning message such as GPIO pins in use
        GPIO.setwarnings(False)
        
        # use the values of the GPIO pins, and not the actual pin number
        # so if you connect to GPIO 25 which is on pin number 22, the
        # reference in this code is 25, which is the number of the GPIO
        # port and not the number of the physical pin
        GPIO.setmode(GPIO.BCM)
        
        if sensor == 0:
        
            # point the software to the GPIO pins the sensor is using
            # change these values to the pins you are using
            # GPIO output = the pin that's connected to "Trig" on the sensor
            # GPIO input = the pin that's connected to "Echo" on the sensor
            GPIO.setup(10,GPIO.OUT)
            GPIO.setup(9,GPIO.IN)
            GPIO.output(10, GPIO.LOW)
        
            # found that the sensor can crash if there isn't a delay here
            # no idea why. If you have odd crashing issues, increase delay
            time.sleep(0.3)
        
            # sensor manual says a pulse ength of 10Us will trigger the
            # sensor to transmit 8 cycles of ultrasonic burst at 40kHz and
            # wait for the reflected ultrasonic burst to be received
        
            # to get a pulse length of 10Us we need to start the pulse, then
            # wait for 10 microseconds, then stop the pulse. This will
            # result in the pulse length being 10Us.
        
            # start the pulse on the GPIO pin
            # change this value to the pin you are using
            # GPIO output = the pin that's connected to "Trig" on the sensor
            GPIO.output(10, True)
        
            # wait 10 micro seconds (this is 0.00001 seconds) so the pulse
            # length is 10Us as the sensor expects
            time.sleep(0.00001)
        
            # stop the pulse after the time above has passed
            # change this value to the pin you are using
            # GPIO output = the pin that's connected to "Trig" on the sensor
            GPIO.output(10, False)
        
            # listen to the input pin. 0 means nothing is happening. Once a
            # signal is received the value will be 1 so the while loop
            # stops and has the last recorded time the signal was 0
            # change this value to the pin you are using
            # GPIO input = the pin that's connected to "Echo" on the sensor
            while GPIO.input(9) == 0:
                signaloff = time.time()
        
            # listen to the input pin. Once a signal is received, record the
            # time the signal came through
            # change this value to the pin you are using
            # GPIO input = the pin that's connected to "Echo" on the sensor
            while GPIO.input(9) == 1:
                signalon = time.time()
        
            # work out the difference in the two recorded times above to
            # calculate the distance of an object in front of the sensor
            timepassed = signalon - signaloff
        
            # we now have our distance but it's not in a useful unit of
            # measurement. So now we convert this distance into centimetres
            distance = timepassed * 17000
        
            # return the distance of an object in front of the sensor in cm
            return distance
        
            # we're no longer using the GPIO, so tell software we're done
            GPIO.cleanup()
        
        else:
            print("Incorrect usonic() function varible.")
    
    
    def rightSensor(self, sensor):
        # Disable any warning message such as GPIO pins in use
        GPIO.setwarnings(False)
        
        # use the values of the GPIO pins, and not the actual pin number
        # so if you connect to GPIO 25 which is on pin number 22, the
        # reference in this code is 25, which is the number of the GPIO
        # port and not the number of the physical pin
        GPIO.setmode(GPIO.BCM)
        
        if sensor == 0:
        
            # point the software to the GPIO pins the sensor is using
            # change these values to the pins you are using
            # GPIO output = the pin that's connected to "Trig" on the sensor
            # GPIO input = the pin that's connected to "Echo" on the sensor
            GPIO.setup(23,GPIO.OUT)
            GPIO.setup(24,GPIO.IN)
            GPIO.output(23, GPIO.LOW)
        
            # found that the sensor can crash if there isn't a delay here
            # no idea why. If you have odd crashing issues, increase delay
            time.sleep(0.3)
        
            # sensor manual says a pulse ength of 10Us will trigger the
            # sensor to transmit 8 cycles of ultrasonic burst at 40kHz and
            # wait for the reflected ultrasonic burst to be received
        
            # to get a pulse length of 10Us we need to start the pulse, then
            # wait for 10 microseconds, then stop the pulse. This will
            # result in the pulse length being 10Us.
        
            # start the pulse on the GPIO pin
            # change this value to the pin you are using
            # GPIO output = the pin that's connected to "Trig" on the sensor
            GPIO.output(23, True)
        
            # wait 10 micro seconds (this is 0.00001 seconds) so the pulse
            # length is 10Us as the sensor expects
            time.sleep(0.00001)
        
            # stop the pulse after the time above has passed
            # change this value to the pin you are using
            # GPIO output = the pin that's connected to "Trig" on the sensor
            GPIO.output(23, False)
        
            # listen to the input pin. 0 means nothing is happening. Once a
            # signal is received the value will be 1 so the while loop
            # stops and has the last recorded time the signal was 0
            # change this value to the pin you are using
            # GPIO input = the pin that's connected to "Echo" on the sensor
            while GPIO.input(24) == 0:
                signaloff = time.time()
        
            # listen to the input pin. Once a signal is received, record the
            # time the signal came through
            # change this value to the pin you are using
            # GPIO input = the pin that's connected to "Echo" on the sensor
            while GPIO.input(24) == 1:
                signalon = time.time()
        
            # work out the difference in the two recorded times above to
            # calculate the distance of an object in front of the sensor
            timepassed = signalon - signaloff
        
            # we now have our distance but it's not in a useful unit of
            # measurement. So now we convert this distance into centimetres
            distance = timepassed * 17000
        
            # return the distance of an object in front of the sensor in cm
            return distance
        
            # we're no longer using the GPIO, so tell software we're done
            GPIO.cleanup()
        
        else:
            print("Incorrect usonic() function varible.")
    
