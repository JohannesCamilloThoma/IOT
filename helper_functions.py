from sense_hat import SenseHat
import RPi.GPIO as GPIO
import sys
import time


sense = SenseHat()

class weather_parameters():
    def __init__(self):
        self.humidity = float
        self.temperature = float
        self.pressure = float

        self.hum_list = []
        self.temp_list = []
        self.pres_list = []

    def get_humidity(self):
        self.humidity = sense.get_humidity()
        self.hum_list.append(self.humidity)
        return self.humidity

    def get_temperature(self):
        self.temperature = sense.get_temperature()
        self.temp_list.append(self.temperature)
        return self.temperature

    def get_pressure(self):
        self.pressure = sense.get_pressure()
        self.pres_list.append(self.pressure)
        return self.pressure

    def get_lists(self):
        return self.hum_list, self.temperature, self.pressure

# this def is maybe not needed because it is very short
def light(pin):
        # preferred option
        light = GPIO.LED(pin)

        return light
        '''
        # save option
        light = GPIO.setup(pin, GPIO.OUT)
        
        '''

def get_distance():
    pass

def motor_up():
    pass

def motor_down():
    pass










