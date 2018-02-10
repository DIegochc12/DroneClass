from dronekit import connect, VehicleMode, LocationGlobalRelative
import time 


#Vehicle connetion
drone = connect('127.0.0.1:14551', wait_ready=True)

while not drone. is_armable:
	print ('Vehicle is not armable, waiting....')
	time.sleep(1)

print('Ready to arm')
drone.mode = VehicleMode('GUIDED')
drone.armed = True
