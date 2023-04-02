
from time import sleep
from e_drone.drone import *
from e_drone.protocol import *

if __name__ == '__main__':
    drone = Drone()
    drone.open("com4")

    print("이륙")
    drone.sendTakeOff()
    sleep(0.01)

    print("호버링")
    drone.sendControlWhile(0, 0, 0, 0, 4000)

    print("회오리 회전 원비행")
    drone.sendControlWhile(50, 0, -60, 25, 5000)

    print("정지")
    drone.sendControlWhile(0, 0, 0, 0, 1000)

    print("착륙")
    drone.sendLanding()
    sleep(0.01)
    drone.sendLanding()
    sleep(0.01)
    
    drone.close()
