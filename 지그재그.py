
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

    print("오른쪽 회전")
    drone.sendControlWhile(0, 0, -30, 0, 600)

    print("지그재그")
    for i in range(4, 0, -1):
        drone.sendControlWhile(0, 60, 0, 0, 1000)
        drone.sendControlWhile(0, 0, 60, 0, 600)    
        drone.sendControlWhile(0, 60, 0, 0, 1000)
        drone.sendControlWhile(0, 0, -60, 0, 600)  

    print("왼쪽 회전")
    drone.sendControlWhile(0, 0, 30, 0, 600)       


    print("정지")
    drone.sendControlWhile(0, 0, 0, 0, 1000)

    print("착륙")
    drone.sendLanding()
    sleep(0.01)
    drone.sendLanding()
    sleep(0.01)

    drone.close()
