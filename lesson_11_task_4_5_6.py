from abc import ABC, abstractmethod


class MyOwnError(Exception):
    def __init__(self, text):
        self.text = text


class OfficeStore:
    store_number = 0

    def __init__(self):
        OfficeStore.store_number += 1
        address = input(f"enter the address of the {OfficeStore.store_number}th store ")
        name = input(f"enter the name of the  {OfficeStore.store_number}th store")
        self.address = address
        self.name = name
        self.products = {'printers': 0, 'computers': 0, 'scanners ': 0}

    def __str__(self):
        return f'Store {self.name} at address: {self.address} with products: {self.products}'

    def get_equipment(self, equipment):
        equipment.location = self.name
        if equipment.__class__ == Printer:
            self.products['printers'] += 1
        elif equipment.__class__ == Computer:
            self.products['computers'] += 1
        elif equipment.__class__ == Scanner:
            self.products['scanners'] += 1

    def give_equipment(self, equipment, shop):
        shop.get_equipment(equipment)
        if equipment.__class__ == Printer:
            self.products['printers'] -= 1
        elif equipment.__class__ == Computer:
            self.products['computers'] -= 1
        elif equipment.__class__ == Scanner:
            self.products['scanners'] -= 1


class OfficeEquipment(ABC):

    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def get_model(self):
        pass


class Printer(OfficeEquipment):
    printer_number = 0

    def __init__(self):
        Printer.printer_number += 1
        model = input(f"Enter the model of the {Printer.printer_number}th printer: ")
        cost = input(f"Enter the price of the {Printer.printer_number}th printer: ")
        while True:
            try:
                if not cost.isdigit():
                    raise MyOwnError("The price must be a number!")
            except MyOwnError as err:
                print(err)
                cost = input(f"Enter the price of the {Printer.printer_number}th printer: ")
            else:
                break

        self.location = None
        self.model = model
        self.cost = cost

    def __str__(self):
        return f'location: {self.location}, model: {self.model}, price: {self.cost}$'

    def get_cost(self):
        return f'{self.cost}$'

    def get_model(self):
        return self.model


class Computer(OfficeEquipment):
    computer_number = 0

    def __init__(self):
        Computer.computer_number += 1
        model = input(f"Enter the model of the {Computer.computer_number}th computer: ")
        cost = input(f"Enter the price of the {Computer.computer_number}th computer: ")
        while True:
            try:
                if not cost.isdigit():
                    raise MyOwnError("The price must be a number!")
            except MyOwnError as err:
                print(err)
                cost = input(f"Enter the price of the {Computer.computer_number}th printer: ")
            else:
                break

        self.location = None
        self.model = model
        self.cost = cost

    def __str__(self):
        return f'location: {self.location}, model: {self.model}, price: {self.cost}$'

    def get_cost(self):
        return f'{self.cost}$'

    def get_model(self):
        return self.model


class Scanner(OfficeEquipment):
    scanner_number = 0

    def __init__(self):
        Scanner.scanner_number += 1
        model = input(f"Enter the model of the {Scanner.scanner_number}th scanner: ")
        cost = input(f"Enter the price of the {Scanner.scanner_number}th scanner: ")
        while True:
            try:
                if not cost.isdigit():
                    raise MyOwnError("The price must be a number!")
            except MyOwnError as err:
                print(err)
                cost = input(f"Enter the price of the {Scanner.scanner_number}th printer: ")
            else:
                break
        self.location = None
        self.model = model
        self.cost = cost

    def __str__(self):
        return f'location: {self.location}, model: {self.model}, price: {self.cost}$'

    def get_cost(self):
        return f'{self.cost}$'

    def get_model(self):
        return self.model


printer_1 = Printer()
print(printer_1.get_model())
print(printer_1.get_cost())
office_1 = OfficeStore()
print(office_1.address)
print(office_1)
office_1.get_equipment(printer_1)
print(printer_1.location)
print(printer_1)
print(office_1.products)
office_2 = OfficeStore()
office_1.give_equipment(printer_1, office_2)
print(printer_1)
print(printer_1.location)
print(office_1.products)
print(office_2.products)
print(office_1)
print(office_2)
