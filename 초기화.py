
from time import sleep
from e_drone.drone import *
from e_drone.protocol import *

def eventTrim(trim):
    print("{0}, {1}, {2}, {3}".format(trim.roll, trim.pitch, trim.yaw, trim.throttle))

def eventMotion(motion):
    print("eventMotion()")
    print("- Accel: {0:5}, {1:5}, {2:5}".format(motion.accelX, motion.accelY, motion.accelZ))
    print("-  Gyro: {0:5}, {1:5}, {2:5}".format(motion.gyroRoll, motion.gyroPitch, motion.gyroYaw))  
    print("- Angle: {0:5}, {1:5}, {2:5}".format(motion.angleRoll, motion.anglePitch, motion.angleYaw)) 

if __name__ == '__main__':

    drone = Drone()
    drone.open("com5")

    # drone.setEventHandler(DataType.Trim, eventTrim)
    # drone.setEventHandler(DataType.Motion, eventMotion)
    drone.sendClearBias()
    sleep(0.1)

    drone.sendRequest(DeviceType.Drone, DataType.Trim)
    sleep(0.1)

    drone.sendRequest(DeviceType.Drone, DataType.Motion)
    sleep(0.1)
    
    drone.close()

