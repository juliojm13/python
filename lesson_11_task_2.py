class MyOwnError(Exception):
    def __init__(self, text):
        self.text = text


while True:
    try:
        a = int(input("write the first number, please: "))
        b = int(input("write the second number, please: "))
        if b == 0:
            raise MyOwnError("the second number can not be zero, you can not divide by zero! ")
    except ValueError:
        print("You must write a number! ")
    except MyOwnError as err:
        print(err)
    else:
        result = a / b
        print(f'the result of the division is {result} ')
        break
