import math

f = open('input.txt', 'r') 

first = list(f.readline().split()) 
second = list(f.readline().split())
third = list(f.readline().split())


x1 = int(first[0])
x2 = int(second[0])
x3 = int(third[0])

y1 = int(first[1])
y2 = int(second[1])
y3 = int(third[1])

a = math.sqrt(((x2-x1) ** 2) + ((y2-y1) ** 2))
b = math.sqrt(((x3-x2) ** 2) + ((y3-y2) ** 2))
c = math.sqrt(((x3-x1) ** 2) + ((y3-y1) ** 2))

f1 = open('output.txt', 'w') 

alpha = int((((math.acos((b * b + c * c - a * a) / (2 * b * c)) * 180)) / math.pi))
betta = int((((math.acos((a * a + c * c - b * b) / (2 * a * c)) * 180)) / math.pi))
gamma = int((((math.acos((a * a + b * b - c * c) / (2 * a * b)) * 180)) / math.pi))

if ((alpha == 90) or  (betta == 90)  or (gamma == 90)):
    f1.write("RIGHT")
elif ((alpha > 90) or (betta > 90) or (gamma > 90)):
    f1.write("OBTUSE")
elif:
    f1.write("ACUTE")

f.close()
f1.close()
