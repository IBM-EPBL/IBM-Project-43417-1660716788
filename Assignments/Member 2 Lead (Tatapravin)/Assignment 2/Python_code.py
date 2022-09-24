import random

j = 0
while j<7:
    H = random.randint(0, 100)
    T = random.randint(35, 222)
    print("Humidity value is:", H, "\nTemperature value is:", T)
    if H <= 70 and T >= 80:
        print("Your field is Dry and Need Water!,please Catch Water.")
    else:
        print("Your Field is filled with full of  water !")
    j=j+1