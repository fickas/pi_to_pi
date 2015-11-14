
from Comm import Comm
import time
import grovepi
import lcd

lcd.setRGB(128,0,0) #green
time.sleep(2)

master_ip = "192.168.0.104"
master = Comm(master_ip)

# Connect the Grove Ultrasonic Ranger to digital port D4
ultrasonic_ranger = 4

#Step 1. Wait until get ready message from master

waiting_flag = True
while waiting_flag:
    table1 = master.get_table()
    print('master sent me: ' + str( table1 ))
    waiting_flag = table1 == [] #if still empty then keep flag True
        
print('Got ready message from master')
lcd.setRGB(0,128,0) #green

#Step 2. Wait until get unusual value and then send trigger

lower_sd = 
upper_sd =

loop_flag = True

while loop_flag:
    try:
        
        # Read distance value from Ultrasonic
        ultra = grovepi.ultrasonicRead(ultrasonic_ranger)
        if ultra < lower_sd or ultra > upper_sd:
            master.send( {'message': 'triggered'} )
            print('Sent my trigger to master')
            loop_flag = False
        time.sleep(1)
        
    except TypeError:
        print(TypeError)
    except IOError:
        print(IOError)
        
#Step 3. Done

lcd.setRGB(0,0,128)
time.sleep(2)
print( 'shutting down' )
