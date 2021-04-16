the_list_1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов' ]
print(the_list_1)

for indx in range(len(the_list_1)):
    for i in range(1, 10):
        if the_list_1[indx].startswith(str(i)) and len(the_list_1[indx]) == 1:
            the_list_1[indx] = '0' + the_list_1[indx]

        elif (the_list_1[indx].startswith('+') or the_list_1[indx].startswith('-')) and len(the_list_1[indx]) == 2:
            the_list_1[indx] = the_list_1[indx][0] + '0' + the_list_1[indx][1]

print(the_list_1)

indx_help = 0
for indx in range(len(the_list_1)):
    # indx_help += 1
    indx = indx + indx_help
    for i in range(0, 10):
        if the_list_1[indx].startswith('+') or the_list_1[indx].startswith('-') or the_list_1[indx].startswith(
                str(i)):
            the_list_1.insert(indx + 1, '"')
            the_list_1.insert(indx, '"')
            indx_help += 2

print(the_list_1)
print(" ".join(the_list_1))
i = 0
for el in the_list_1:
    indx = i
    if the_list_1[indx] == '"':
        the_list_1[indx] = "".join(the_list_1[indx:indx + 3])
        the_list_1.remove(the_list_1[indx + 1])
        the_list_1.remove(the_list_1[indx + 1])
    else:
        the_list_1[indx] = the_list_1[indx]
    i += 1

print(" ".join(the_list_1))
