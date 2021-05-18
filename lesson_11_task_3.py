class MyOwnError(Exception):
    def __init__(self, text):
        self.text = text


result = []
while True:
    try:
        new_number = input("enter a new number or 'stop' to finish: ")
        if new_number == 'stop':
            break
        elif not new_number.isdigit():
            raise MyOwnError('you can enter just numbers!')

    except MyOwnError as err:
        print(err)
    else:
        new_number = int(new_number)
        result.append(new_number)

print(result)
