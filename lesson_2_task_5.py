price = [12.3, 56.1, 87.6, 65.4, 87.06, 99.1, 78.1, 46.7, 63.3, 55.14, 87.6, 87]
i = 0
price1=price[:]
for el in price:
    rub = round(el // 1)
    kop = round((el % 1) * 100)
    kop = str(kop)
    if len(kop) == 1:
        kop = '0' + str(kop)
    print(rub, "руб ", kop, "коп")
    text_list = rub, "руб ", kop, "коп"
    text_list= str(text_list)
    price1[i] = text_list
    i += 1
print(price1)
print(",".join(price1))
print(sorted(price))
print(price)
prices_lessing = sorted(price,reverse=True)
print(prices_lessing)
for i in range(6):
    print(i,'.',prices_lessing[i])