
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
    drone.sendControlWhile(0, 0, 0, 0, 5000)

    print("플립")
    drone.sendFlightEvent(FlightEvent.FlipLeft)
    sleep(1)

    print("호버링")
    drone.sendControlWhile(0, 0, 0, 0, 3000)

    print("착륙")
    drone.sendLanding()
    sleep(0.01)
    drone.sendLanding()
    sleep(0.01)

    drone.close()
