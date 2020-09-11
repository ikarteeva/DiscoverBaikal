f = open('input.txt', 'r') 

n = int(f.readline())

f1 = open('output.txt', 'w') 

if n > 0:
 first = list(f.readline().split())

 result = [int(item) for item in first] 

 i = 2

 while i < n:
   result[i] = result[i] + min(result[i-1], result[i-2])
   i = i + 1

 if i > 2:
  f1.write(str(result[i-1]))
 elif i > 1:
  f1.write(str(min(result[i-1], result[i-2])))
 else:
  f1.write(str(result[0])) 


f.close()
f1.close()
