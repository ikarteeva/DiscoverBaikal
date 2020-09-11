f = open('input.txt', 'r') 
first = list(f.readline().split())
n = int(first[0])
m = int(first[1])

ans = [[0]*n for _ in range(n)]

for it in range(m):
    l = f.readline().split()
    r, c = map(int, l)
    ans[r-1][c-1] = ans[c-1][r-1] = 1
 
f1 = open('output.txt', 'w') 

for element in ans:
     for element1 in element:
       f1.write(str(element1))
     f1.write("\n")

f.close()
f1.close()
