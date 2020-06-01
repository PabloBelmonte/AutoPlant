import time
import json


def get_temperature():
    temp = 25
    return temp

def get_ph():
    ph = 7
    return ph

def get_humidity():
    humidity = 80
    return humidity

# Code to get sensor data on the uController


print('--------------------------')
print(f'Gettng all sensor data.\n')

# temp
temperature = get_temperature()
# ph
ph = get_ph()
# humidity
humidity = get_humidity()

# dict to json
dictionary ={ 
    "temperature" : temperature, 
    "ph" : ph, 
    "humidity" : humidity
}
# dump to json
json_object = json.dumps(dictionary, indent = 4)
with open("uC_interface/sensor.json", "w") as outfile:
    outfile.write(json_object)

print('Sensors data ready!')
print('--------------------------')

# os.environ('TEMPERATURE') = str(temperature)
# os.environ('PH') = str(ph)
# os.environ('HUMIDITY') = str(humidity)

# exit()