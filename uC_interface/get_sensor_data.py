import time
import json

# Code to get sensor data on the uController


print()
print(f'Gettng all sensor data.')
print()

# temp
temperature = 25
# ph
ph = 7
# humidity
humidity = 80

# dump to json
dictionary ={ 
    "temperature" : temperature, 
    "ph" : ph, 
    "humidity" : humidity
}
json_object = json.dumps(dictionary, indent = 4)

with open("sensor.json", "w") as outfile:
    outfile.write(json_object)


print()
print('Sensors data ready!')
print()

# os.environ('TEMPERATURE') = str(temperature)
# os.environ('PH') = str(ph)
# os.environ('HUMIDITY') = str(humidity)

# exit()