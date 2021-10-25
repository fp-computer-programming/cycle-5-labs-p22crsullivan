# Author: CRS 10/25/21
import math
import time

seconds0 = time.process_time
print(math.pow(2, 2))
seconds1 = time.process_time
speed = seconds1 - seconds0
print(speed)

seconds2 = time.process_time
print(2 ** 2)
seconds3 = time.process_time
speed2 = seconds3 - seconds2
print(speed2)
