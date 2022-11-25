import time
import sys
import ibmiotf.application
import ibmiotf.device
import random
import requests,json

#Provide your IBM Watson Device Credentials
organization = "o18g4e"
deviceType = "rain"
deviceId = "12345"
authMethod = "token"
authToken = "RJXd1kAhbObGRo)U(p"
complete_url="https://api.openweathermap.org/data/2.5/weather?lat=10.069542&lon=78.7642445&appid=dff65ece7cd56e5609a961090c1815a5"


# Initialize GPIO
def myCommandCallback(cmd):
    print("Command received: %s" % cmd.data['command'])
    status=cmd.data['command']
    if status=="motoron":
        print ("Motor is on")
    elif status == "motoroff":
        print ("Motor is off")
    else :
        print ("please send proper command")


try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	#..............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

# Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect()

while True:
        
        motorstatus = ""
        waterlevel=random.randint(1,20)
        Waterusing=""
        if waterlevel < 2:
                waterusing =str(waterlevel) + " feet Water Level Low"
        else:
                waterusing =str(waterlevel) + " feet Using rain water"
        
        soilmoisture=random.randint(0,872)
        if soilmoisture <200:
                motorstatus="Motor on automatically"
               
        else:
                motorstatus="Motor off automatically"
                
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
                y=x["name"]
                z = x["weather"]
                weather_description = z[0]["description"]
        data = { 'Waterlevel' : waterusing, 'SoilMoisture': soilmoisture, 'MotorStatus':motorstatus, 'Area':str(y),'WeatherDescription':str(weather_description) }
        #print data
        def myOnPublishCallback():
            print ("Published Waterlevel = %s " % waterusing, "SoilMoisture = %s %%" % soilmoisture, "MotorStatus = %s" % motorstatus," Area="+str(y)," Weather description :" +str(weather_description), "to IBM Watson")

        success = deviceCli.publishEvent("event_1", "json", data, qos=0, on_publish=myOnPublishCallback)
        if not success:
            print("Not connected to IoTF")
        time.sleep(10)

        
        deviceCli.commandCallback = myCommandCallback
       

# Disconnect the device and application from the cloud
deviceCli.disconnect()
   
