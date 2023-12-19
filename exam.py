#json

import json
import time
#from sense_hat import SenseHat

#sense = SenseHat()
start_time = time.time()

while True:
    #temp = sense.get_temperature()
    temp = 25
    current_time = time.time() - start_time

    python_dict = {"time": current_time, "home_city": "Munich", "temperature": temp}
    json_string = json.dumps(python_dict)
    print(json_string)
    time.sleep(5)

#2
hum = 20
temp = 25

dew_point = temp - (100 - hum)/5

while True:

    if temp == dew_point:
        print("dew_point_reached")

    else:
        print(dew_point)
        time.sleep(10)







if __name__ == "__main__":
    pass




