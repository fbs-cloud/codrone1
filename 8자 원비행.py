
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

    print("오른쪽 시계방향 원비행")
    drone.sendControlWhile(30, 0, -100, 0, 3000)

    print("정지")
    drone.sendControlWhile(0, 0, 0, 0, 1000)

    print("왼쪽 시계방향 원비행")
    drone.sendControlWhile(-30, 0, 100, 0, 3000)

    print("정지")
    drone.sendControlWhile(0, 0, 0, 0, 1000)

    print("착륙")
    drone.sendLanding()
    sleep(0.01)
    drone.sendLanding()
    sleep(0.01)
    
    drone.close()

