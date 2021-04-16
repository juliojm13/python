cube_not_even_numbers = []
for number in range(1, 1001):
    if not number % 2 == 0:
        cube_not_even_numbers.append(number ** 3)
print(cube_not_even_numbers)
numbers_for_summ = []
for number in cube_not_even_numbers:
    summ_number = 0
    copy_number = number
    while copy_number:
        summ_number += copy_number % 10
        copy_number = copy_number // 10
    if summ_number % 7 == 0:
        numbers_for_summ.append(number)
print(numbers_for_summ)
summ = 0
for number in numbers_for_summ:
    summ += number
print(summ)
numbers_for_summ_2 = []
for number in cube_not_even_numbers:
    summ_number=0
    copy_number = number + 17
    while copy_number:
        summ_number += copy_number % 10
        copy_number = copy_number // 10
    if summ_number % 7 == 0:
        numbers_for_summ_2.append( number + 17 )
print(numbers_for_summ)
summ = 0
for number in numbers_for_summ_2:
    summ += number
print(summ)
