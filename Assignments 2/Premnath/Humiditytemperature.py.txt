import random
i=1
while i<=6:

    Humidity=random.randint(0,100)
    Temperature=random.randint(32,212)
    print("Humidity value is:",Humidity,"\nTemperature value is:",Temperature)

    if (Temperature>65)and(Humidity<50): #if temperature value is high,humidity value is low then ON motor
       print("Your plant Need water!,please switch ON Motor.")
    else:
       print("your plant has Enough water!")
    i=i+1