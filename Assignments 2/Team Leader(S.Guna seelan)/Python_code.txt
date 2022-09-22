import random
import time
x=0
for x in range(100) :
   h=random.randint(1, 100)
   t=random.randint(32, 212)
   print("Now the humidity is:", h, "% RH")   
   print("Now the temperature is:", t, " °F")
   if(h<30) and (t>72):
      print("Motor is switched on ,to water the plant")
   else:
      print("No need to water the plant now")
   time.sleep(1000)