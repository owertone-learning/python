import random


class Car:

    def __init__(self, name, color, is_police):
        self.color = color
        self.name = name
        self.is_police = bool

    def go(self):
        return f'Your car {self.color} {self.name} is moving'

    def show_speed(self, speed):
        if speed > 100:
            return f'with {speed} km/h. You have exceeded the speed limit over {speed - 100} km/h!'
        else:
            return f'with {speed} km/h'

    def stop(self):
        print(f'Your {self.name} stopped')

    def turn(self):
        direction_list = ['left', 'right', 'straight and left', 'straight and right']
        direction = random.choice(direction_list)
        return f'Your {self.color} {self.name} turn {direction}'


class TownCar(Car):

    def show_speed(self, speed):
        super().show_speed(speed)
        if speed > 60:
            return f'with {speed} km/h. You have exceeded the speed limit over {speed - 60} km/h!'
        else:
            return f'with {speed} km/h.'

    def turn(self):
        direction_list = ['left', 'right', 'straight and left', 'straight and right']
        direction = random.choice(direction_list)
        return f'Your {self.name} turn {direction}'

    def stop(self):
        return f'and stopped'


class SportCar(Car):
    def go(self):
        return f'You look like Dominic Toretto in your {self.color} {self.name}'


class WorkCar(Car):

    def show_speed(self, speed):
        super().show_speed(speed)
        if speed > 40:
            return f'with {speed} km/h. You have exceeded the speed limit over {speed - 40} km/h! Take easy!'
        else:
            return f'with {speed} km/h. Dont sleep!'



class PoliceCar(Car):

    def police(self, is_police):
        super().show_speed(is_police)
        if is_police == True:
            print(f'You just turned on the flashers on your {self.color} police {self.name} and never stopped!')

    def stop(self):
        return f'No, never stop! Never ever!'

run = Car(input('Input car brand:'), input('Input color:'), True)
print(run.go(), run.show_speed(int(input('Input speed:'))))
print(run.turn())
run.stop()

print('------')

town_run = TownCar('MINI Cooper', 'yellow', False)
print(town_run.go(), town_run.show_speed(int(input('Input speed:'))))
print(town_run.turn(), town_run.stop())

print('------')

work_run = WorkCar('sprinkler truck', 'brown', False)
print(work_run.go(), work_run.show_speed(int(input('Input speed:'))))

print('------')

sport_run = SportCar('Dodge Charger 1970', 'black', False)
print(sport_run.go())

print('------')

police_run = PoliceCar('Ford Focus', 'white & blue', False)
police_run.police(True)
print(police_run.stop())