
#***************************************************************************
# Title        : Assignment2_template.py
#
# Description  : This file is a starting point for assignment 2 it contains
#                the main parts and pseudo code for you to complete with your 
#                own code.
#
# Environment  : Python 2.7 Code. 
#
# License      : GNU GPL version 3
#
# Editor Used  : Sublime Text
#
#****************************************************************************

#****************************************************************************
# Imported functions, classes and methods
#****************************************************************************
import time
from dronekit import connect, VehicleMode, LocationGlobalRelative, Command, LocationGlobal
from pymavlink import mavutil
import Tkinter as tk

#****************************************************************************
#   Method Name     : set_velocity_body
#
#   Description     : Sends a MAVLINK velocity command in body frame reference
#                     This means that the X, Y, Z axis will be in relation to the 
#                     vehicle. 
#                     Positive X values will move the drone forward
#                     Positive Y values will move the drone Right
#                     Positive Z values will move the drone down
#                     The values for vx, vy and vz are in m/s, so sending a value
#                     of say 5 in vx will move the drone forward at 5 m/s
#
#                     More information can be found here:
#                     http://ardupilot.org/dev/docs/copter-commands-in-guided-mode.html
#
#   Parameters      : vehicle:  vehicle instance to send the command to
#                     vx:       Velocity in the X axis 
#                     vy
#                     vz
#
#   Return Value    : None
#
#   Author           : tiziano fiorenzani
#
#****************************************************************************

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

#****************************************************************************
#   Method Name     : arm_and_takeoff
#
#   Description     : Add your takeoff function from your last assignment here
#
#   Parameters      : targetAltitude
#
#   Return Value    : None
#
#   Author           : You
#
#****************************************************************************
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



#### your code here #####

#****************************************************************************
#   Method Name     : key
#
#   Description     : Callback for TkInter Key events
#
#   Parameters      : Event: tkinter event containing the key that was pressed
#
#   Return Value    : None
#
#   Author           : You
#
#****************************************************************************
def key(event):
    if event.char == event.keysym: #-- standard keys
        if event.keysym == 'r': drone.mode = VehicleMode("RTL")
            ### Add your code for what you want to happen when you press r #####
            
    else: #-- non standard keys
        if event.keysym == 'Up': set_velocity_body(drone, 5, 0, 0)
            ### add your code for what should happen when pressing the up arrow ###
        elif event.keysym == 'Down': set_velocity_body(drone, -5, 0, 0)
            ### add your code for what should happen when pressing the down arrow ###
        elif event.keysym == 'Left': set_velocity_body(drone, 0, 5, 0)
            ### add your code for what should happen when pressing the Left arrow ###
        elif event.keysym == 'Right': set_velocity_body(drone, 0, -5, 0)
            ### add your code for what should happen when pressing the Right arrow ###

#****************************************************************************
#   MAIN CODE
#
#****************************************************************************

### add your code to connect to the drone here ###
drone = connect('127.0.0.1:14551', wait_ready=True)
# Take off to 10 m altitude
arm_and_takeoff(10)
 
# Read the keyboard with tkinter
root = tk.Tk()
print(">> Control the drone with the arrow keys. Press r for RTL mode")
root.bind_all('<Key>', key)
root.mainloop()
