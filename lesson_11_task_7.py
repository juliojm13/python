class ComplexNumbers:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f'{self.number}'

    def __add__(self, other):
        result = self.number + other.number
        return ComplexNumbers(result)

    def __mul__(self, other):
        result = self.number * other.number
        return ComplexNumbers(result)


number_1 = ComplexNumbers(5+4j)
number_2 = ComplexNumbers(5-2j)
print(number_1 + number_2)
print(number_2 * number_1)