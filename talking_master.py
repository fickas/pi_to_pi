
from Comm import Comm
import time
import grovepi
import lcd

# Connect the Grove Button to digital port D2
button = 2

# Connect the Grove Buzzer to digital port D8
buzzer = 8

grovepi.pinMode(button,"INPUT")
grovepi.pinMode(buzzer,"OUTPUT")
        
lcd.setRGB(128,0,0) #red

worker1_ip = "192.168.0.105"
worker2_ip = "192.168.0.100"
worker1 = Comm(worker1_ip)
worker2 = Comm(worker2_ip)

time.sleep(2)

#Step 1. Wait for user to press button

button_flag = True
while button_flag:
    try:
        value = grovepi.digitalRead(button) # 0 not pressed, 1 pressed
        if value == 1:
            set button_flag False
        time.sleep(.5)
    except TypeError:
        print(TypeError)
    except IOError:
        print(IOError)
        
print('Got button press')

#Step 2. Tell both workers open for business

worker1.send( {'message': 'ready'} )
print('sent ready to ': + worker1_ip)
worker2.send( {'message': 'ready'} )
print('sent ready to ': + worker2_ip)

lcd.setRGB(0,128,128) # green

time.sleep(2) #long enough to see it go green

#Step 3. Wait until receive a signal from both workers

waiting_flag1 = True
waiting_flag2 = True

while waiting_flag1 and waiting_flag2:
    if waiting_flag1:
        table1 = worker1.get_table()
        print('worker1 sent me: ' + str( table1 ))
        
        waiting_flag1 = table1 == [] #if still empty then keep flag True

    if waiting_flag2:
        table2 = worker2.get_table()
        print('worker2 sent me: ' + str( table2 ))
        flag2 = table2 == [] #if still empty then keep flag True

    time.sleep( .5 )

print( 'got them both' )

#Step 4. Buzz then quit

grovepi.digitalWrite(buzzer,1) # write 1 means start buzzing
time.sleep(3)
grovepi.digitalWrite(buzzer,0) # write 0 means stop buzzing

lcd.setRGB(0,0,128)
time.sleep(2)
print( 'shutting down' )
