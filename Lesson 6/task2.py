class Road:

    def __init__(self, lt, wi):
        self._lenght = lt
        self._width = wi

    def make_road(self, we, th):
        print(f'Нужно {int((we * th * self._lenght * self._width) / 1000)} тонн')


road = Road(5000, 20)
road.make_road(25, 5)
