from dronekit import connect, VehicleMode, LocationGlobalRelative
import time 

#With this code we arm the drone ir order to prepare it for the take off
def arm_and_takeoff(TargetAltitude):
	print('Executing takeoff')

	while not drone.is_armable:
		print('Vehicle is not armable, waiting...')
		time.sleep(1)
#Here the drone is ready to be armed and changes his mode to GUIDED
	print('Ready to arm')
	drone.mode = VehicleMode('GUIDED')
	drone.armed = True

	while not drone.armed:
		print('Waiting for arming...')
		time.sleep(1)

	print('Ready for takeoff, taking off...')
	drone.simple_takeoff(TargetAltitude)
#With this code the drone can know the altitude it haves
	while True:
		Altitude = drone.location.global_relative_frame.alt 
		print("Altitude: ", Altitude)
		time.sleep(1)

		if Altitude >= TargetAltitude * 0.95:
			print('Altitude reached')
			break



#Here we connect the drone to the APM planner 
drone = connect('127.0.0.1:14551', wait_ready=True)
arm_and_takeoff(20)
#Here the spped of the drone is set
drone.airspeed = 10
#Those are the locations the drone is going to go 
a_location = LocationGlobalRelative(20.736148, -103.456896, 20)
b_location = LocationGlobalRelative(20.736162, -103.457285, 20)
c_location = LocationGlobalRelative(20.735798, -103.457306, 20)
d_location = LocationGlobalRelative(20.735791, -103.456968, 20)


#In this lines the battery of the drone is printed every 30 seconds
battery = drone.battery.voltage
print ("Battery Voltage:" , battery, " V")
time.sleep(30)
#Here the drone is heading to point A
print('Going to point A')
drone.simple_goto(a_location)
time.sleep(10)
#Here the drone is heading to point B
print('Going to point B')
drone.simple_goto(b_location)
time.sleep(10)
#Here the drone is heading to point C
print('Going to point C')
drone.simple_goto(c_location)
time.sleep(10)
#Here the drone is heading to point D
print('Going to point D')
drone.simple_goto(d_location)
time.sleep(10)
#Here the drone returns to point A in order to complete the square 
print('Returning to point A')
drone.simple_goto(a_location)
time.sleep(10)

#In this lines the drone returns home and turns itself off
print('Landing...')
drone.mode = VehicleMode("RTL")
print('Drone Landed')



