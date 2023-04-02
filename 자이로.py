from time import sleep
from e_drone.drone import *
from e_drone.protocol import *
def eventMotion(motion):
    print("eventMotion()")
    print("- Accel: {0}, {1}, {2}".format(motion.accelX, motion.accelY, motion.accelZ))
    print("- Gyro: {0}, {1}, {2}".format(motion.gyroRoll, motion.gyroPitch, motion.gyroYaw))
if __name__ == '__main__':
    drone = Drone()
    drone.open("com5")
    drone.setEventHandler(DataType.Motion, eventMotion)
    while True:
        drone.sendRequest(DeviceType.Drone, DataType.Motion)
        sleep(1)
    drone.close()



