import sys

with open('bakery.csv', 'r', encoding='utf-8') as f:
    if len(sys.argv) == 1:
        content = f.read()
        print(content)
    elif len(sys.argv) == 2:

        start = int(sys.argv[1])
        content = f.readlines()
        for indx in range(start -1, len(content)):
            print(content[indx])

    elif len(sys.argv) == 3:

        start = int(sys.argv[1])
        finish = int(sys.argv[2])
        content = f.readlines()
        for indx in range(start -1, finish):
            print(content[indx])