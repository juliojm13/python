from abc import ABC, abstractmethod


class Clothes(ABC):
    total = 0

    @abstractmethod
    def cloth(self):
        pass


class Palto(Clothes):
    def __init__(self, detail):
        self.detail = detail

    @property
    def cloth(self):
        need_cloth = self.detail / 6.5 + 0.5
        Clothes.total += need_cloth
        return need_cloth


class Costume(Clothes):
    def __init__(self, detail):
        self.detail = detail

    @property
    def cloth(self):
        need_cloth = 2 * self.detail + 0.3
        Clothes.total += need_cloth
        return need_cloth


palto_1 = Palto(10)
print(palto_1.cloth)
print(Clothes.total)
costume_1 = Costume(20)
print(costume_1.cloth)
print(Clothes.total)
palto_2 = Palto(10)
print(palto_2.cloth)
print(Clothes.total)
costume_2 = Costume(20)
print(costume_2.cloth)
print(Clothes.total)
