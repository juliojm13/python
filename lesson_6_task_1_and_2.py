import time

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    result = []
    for row in f:
        mini_result = (
            row.split('- -')[0], row.split('"')[1].split('/')[0], row.split('"')[1].split('T')[1].split("H")[0])
        result.append(mini_result)
    # print(*result , sep= '\n')
    spammer = result[1][0]
    max_suma = 0
    start = time.perf_counter()
    for i in range(len(result)):
        summa = 0
        for j in range(len(result)):
            if result[i][0] == result[j][0]:
                summa += 1
        if summa >= max_suma:
            max_suma = summa
            spammer = result[i][0]
    finish = time.perf_counter()

    print(spammer, max_suma, "time= ", finish - start)
