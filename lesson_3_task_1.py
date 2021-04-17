numbers = { 'один': 'one', 'два': 'two', 'три': 'three', 'четыре': 'four', 'пять': 'five', 'шесть': 'six', 'семь': 'seven', 'восемь': 'eigth',
           'девять': 'nine', 'десять': 'ten'}

def translate_1 (number):
    if number not in numbers:
        print(None)
    else:
        print(numbers[number])

translate_1('три')
translate_1('пять')
translate_1('два')
translate_1('семь')
translate_1('сто')