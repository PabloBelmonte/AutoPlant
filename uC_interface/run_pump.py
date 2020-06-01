import time
import os

# Code to run the pump on the uController

delay = float(os.getenv('DELAY_TIME'))

# delay = 5

print('--------------------------')
print(f'Running pump for time equal to: {delay} seconds...\n')

time.sleep(delay)

print('Pump ready!')
print('--------------------------')

# exit()