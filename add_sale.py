import sys


with open('bakery.csv', 'a', encoding='utf-8') as f:
    sale = sys.argv[1] + '\n'
    f.write(sale)
