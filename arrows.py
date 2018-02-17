#This lines are the libraries we need to import in order to be able of running the program
import time
from dronekit import connect, VehicleMode, LocationGlobalRelative, Command, LocationGlobal
from pymavlink import mavutil
import Tkinter as tk


#Here we set how the drone will move in order to the x, y, and z axis 
def set_velocity_body(vehicle, vx, vy, vz):
    msg = vehicle.message_factory.set_position_target_local_ned_encode(
            0,
            0, 0,
            mavutil.mavlink.MAV_FRAME_BODY_NED,
            0b0000111111000111, #-- BITMASK -> Consider only the velocities
            0, 0, 0,        #-- POSITION
            vx, vy, vz,     #-- VELOCITY
            0, 0, 0,        #-- ACCELERATIONS
            0, 0)
    vehicle.send_mavlink(msg)
    vehicle.flush()

#This is the same code we use in the past activity, and is for turn on the drone and take it off to a high of 10 meters 
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


#Here we set the arrows we are going to use in order to be able to move the drone on the air 
def key(event):
    if event.char == event.keysym: #-- standard keys
        if event.keysym == 'r': drone.mode = VehicleMode("RTL")
        print("On my way back to home")
            #Here we set a button to make the drone return to home
            
    else: #-- non standard keys
        if event.keysym == 'Up': set_velocity_body(drone, 5, 0, 0)
            #Here we set the up button to move the drone forward
        elif event.keysym == 'Down': set_velocity_body(drone, -5, 0, 0)
            #Here we set the down button to move the drone backwards
        elif event.keysym == 'Left': set_velocity_body(drone, 0, -5, 0)
            #Here we set a key in order to make the drone move to the left 
        elif event.keysym == 'Right': set_velocity_body(drone, 0, 5, 0)
            #Here we set a key in order to move the drone to the right 
      

#Here twe connect the drone with the APM planner
drone = connect('127.0.0.1:14551', wait_ready=True)
# Here the drone take off to 10 m altitude
arm_and_takeoff(10)
 
# Here the TKinter is opened and also we print the instructions of how to move the drone 
root = tk.Tk()
print(">> Control the drone with the arrow keys. Press r for RTL mode")
root.bind_all('<Key>', key)
root.mainloop()

drone.close()