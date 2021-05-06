class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self._mass_1_kb_m_1_cm = 50

    def calculate_mass_asphalt(self, centimetr):
        mass = self._length * self._width * self._mass_1_kb_m_1_cm * centimetr
        print(f'{mass}T will be requierd')


road_1 = Road(15, 2)
road_1.calculate_mass_asphalt(5)
