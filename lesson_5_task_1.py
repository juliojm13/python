def odd_numbs (n):
    for num in range(1,n+1):
        if num%2:
            yield num

odd_to_15 = odd_numbs(15)
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))

