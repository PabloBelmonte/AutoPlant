import time
import json
import csv
import os
import numpy as np

def get_temperature():
    # mu, sigma = 25, 0.1 # mean and standard deviation
    mu, sigma = 25, 1 # mean and standard deviation
    temp = np.random.normal(mu, sigma, 1)
    temp = temp[0]
    return temp

def get_ph():
    # mu, sigma = 7, 0.1 # mean and standard deviation
    mu, sigma = 7, 1 # mean and standard deviation
    ph = np.random.normal(mu, sigma, 1)
    ph = ph[0]
    return ph

def get_humidity():
    # mu, sigma = 80, 0.1 # mean and standard deviation
    mu, sigma = 80, 1 # mean and standard deviation
    humidity = np.random.normal(mu, sigma, 1)
    humidity = humidity[0]
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

print('Sensors data ready!\n')

if os.path.isfile('uC_interface/sensorRecordData.csv'):
    # Apend data to csv file
    with open("uC_interface/sensorRecordData.csv", "a") as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([str(temperature), str(ph), str(humidity)])
else:
    with open("uC_interface/sensorRecordData.csv", "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['"temperature"', '"ph"', '"humidity"'])
        writer.writerow([str(temperature), str(ph), str(humidity)])
    


print('Sensors data ready!')
print('--------------------------')
