import time


class TrafficLight:
    __color = ''

    def running(self):
        for i in range(1, 11):
            _TrafficLight__color = 'Red'
            print(f'Color: {_TrafficLight__color}')
            time.sleep(7)
            _TrafficLight__color = 'Yellow'
            print(f'Color: {_TrafficLight__color}')
            time.sleep(2)
            _TrafficLight__color = 'Green'
            print(f'Color: {_TrafficLight__color}')
            time.sleep(5)
            _TrafficLight__color = 'Yellow'
            print(f'Color: {_TrafficLight__color}')
            time.sleep(2)
            i += 1


auto = TrafficLight()
auto.running()
