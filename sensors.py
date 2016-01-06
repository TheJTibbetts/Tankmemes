import RPi.GPIO as GPIO
import time

class sensors():
  
    def __init__(self):
        self.sensor
  
    def leftsensor(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        
        if self.sensor == 0:
            GPIO.setup(10, GPIO.OUT)
            GPIO.setup(9, GPIO.IN)
            GPIO.setup(10, GPIO.LOW)
            
            time.sleep(0.3)
            
            GPIO.output(10, True)
            
            time.sleep(0.00001)
            
            GPIO.output(10, False)
            
            while GPIO.input(9) == 0:
                signaloff = time.time()
                
            while GPIO.input(9) == 1:
                signalon = time.time()
                
            timepassed = signalon - signaloff
            
            distance = timepassed * 17000
            
            return distance
            
            GPIO.cleanup()
            
        else:
            print("Incorrect ultrasonic() function variable.")
            
    def rightsensor(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        
        if self.sensor == 0:
        
            GPIO.setup(23, GPIO.OUT)
            GPIO.setup(24, GPIO.IN)
            GPIO.setup(23, GPIO.LOW)
            
            time.sleep(0.3)
            
            GPIO.setup(23, True)
            
            time.sleep(0.00001)
            
            GPIO.output(23, False)
            
            while GPIO.input(24) == 0:
                signaloff = time.time()
                
            while GPIO.input(24) == 1:
                signalon = time.time()
                
            timepassed = signalon - signaloff
            
            distance = timepassed * 17000
            
            return distance
            
            GPIO.cleanup()
            
        else:
            print("Incorrect usonic() function variable.")
