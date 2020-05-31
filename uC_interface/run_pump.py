import time
import os

# Code to run the pump on the uController

delay = int(os.getenv('DELAY_TIME'))

# delay = 5

print()
print(f'Running pump for time equal to: {delay} seconds...')
print()

time.sleep(delay)

print()
print('Pump ready!')
print()

# exit()