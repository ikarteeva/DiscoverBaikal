f = open('input.txt', 'r')

string = f.readline()

enter = list(f.readline().replace(' ', ''))
exit = list(f.readline().replace(' ', ''))

f1 = open('output.txt', 'w')

for element1 in exit:
    j = 0
    for element in enter:
         if element1 == element:
            j = j + 1
    if j == 0:
        f1.write('NO\n')
    else:
        f1.write('YES\n')

f1.close()
f.close()
