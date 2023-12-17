from sense_hat import SenseHat
import RPi.GPIO as GPIO
import sys
import time
import helper_functions as h
import threading
import time

sense = SenseHat()
done = False

'''Buttons'''
button_pin = pass


class garage_condition(threading.Thread):
    def __init__(self):
        self.garage = h.weather_parameters()

    def get_data(self):
        while not done:
            self.temperature = self.garage.get_temperature()
            self.humidity = self.garage.get_humidity()
            self.pressure = self.garage.get_pressure()
            time.sleep(30)


class distance_check(threading.Thread):
    def __init__(self):
        self.distance = 100

    def check(self):
        '''get distance here'''
        if self.distance < 50:
            # motor up
            pass
        else:
            # motor down
            pass

def manual_door_opener():
    button = GPIO.Button(button_pin)
    if button.is_pressed():
        if door_open = True:
            # motor down
            pass
        else:
            # motor up
            pass






if __name__ == "__main__":
    conditions = garage_condition()

    conditions.start()
    distance_check.start()

    input("press enter to stop")
    done = True