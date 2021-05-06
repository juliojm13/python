import time


class TrafficLight:
    def __init__(self):
        self.__color = ['red','yellow','green']

    def running(self):
        print(self.__color[0])
        time.sleep(3)
        print(self.__color[1])
        time.sleep(2)
        print(self.__color[2])
        time.sleep(2)


traffic_light_1 = TrafficLight()
traffic_light_1.running()
traffic_light_1.running()
