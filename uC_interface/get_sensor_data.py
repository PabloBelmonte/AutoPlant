import time
import os

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

print()
print('Sensors ready!')
print()

os.environ('TEMPERATURE') = string(temperature)
os.environ('PH') = string(ph)
os.environ('HUMIDITY') = string(humidity)

# exit()