def type_logger(callback):
    def wrapper(argument):
        a = callback(argument)
        print(argument, ': ', type(argument))
        return a

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
print(a)
