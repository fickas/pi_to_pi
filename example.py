
from Comm import Comm
#import Server
import time


neighbor1_ip = Comm("192.168.0.105")
neighbor2_ip = Comm("192.168.0.100")


neighbor1_ip.send( {'message': 'fyi', 'value': "Test"} )

neighbor2_ip.send( {'message': 'fyi', 'value': "Test"} )

flag1 = True
flag2 = True

while flag1 and flag2:
    if flag1:
        table1 = neighbor1_ip.get_table()
        print('neighbor1 sent: ' + str( table1 ))
        flag1 = table1 == [] #if still empty then keep flag True

    if flag2:
        table2 = neighbor2_ip.get_table()
        print('neighbor2 sent: ' + str( table2 ))
        flag2 = table2 == [] #if still empty then keep flag True

    time.sleep( .5 )

print( 'got them both' )
