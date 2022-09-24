import random
import winsound
import time
x=0
frequency=500
duration=3000
for x in range(50) :
   h=random.randint(1, 100) 
   t=random.randint(32, 212)
   print("Now the humidity is:", h, "% RH")   
   print("Now the temperature is:", t, " °F") 
   if (t>200):
      print("The temperature is high")
      winsound.Beep(frequency,duration)
   time.sleep(3)
