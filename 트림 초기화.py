from time import sleep
from e_drone.drone import *
from e_drone.protocol import *

def eventTrim(trim):
    print("{0}, {1}, {2}, {3}".format(trim.roll, trim.pitch, trim.yaw, trim.throttle))

if __name__ == '__main__':

    drone = Drone()
    drone.open("com5")
    drone.setEventHandler(DataType.Trim, eventTrim)
    drone.sendClearTrim()
    sleep(0.01)
    drone.sendRequest(DeviceType.Drone, DataType.Trim)
    sleep(0.1)
    
    i = 0
    while i < 5 :
        i += 1
        drone.sendRequest(DeviceType.Drone, DataType.Trim)
        sleep(0.1)
    drone.close()
   



