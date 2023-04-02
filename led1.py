
import random
from time import sleep
from e_drone.drone import *
from e_drone.protocol import *
if __name__ == '__main__':
    drone = Drone(True, True, True, True, True)
    drone.open("com5")
    while True:
        drone.sendLightDefaultColor(LightModeDrone.BodyDimming, 1, 255, 0, 0) # 빨간색
        sleep(2)
        drone.sendLightDefaultColor(LightModeDrone.BodyDimming, 1, 0, 255, 0) # 녹색
        sleep(2)
        drone.sendLightDefaultColor(LightModeDrone.BodyDimming, 1, 0, 0, 255) # 파랑색
        sleep(2)
    drone.close()

