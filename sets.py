import random
import math

s1=set()

for i in range(10):
    n=float(input("Enter a number:"))
    s1.add(n)
t=tuple(s1)
print("Three random integers")
for i in range(3):
    print(random.choice(t))
total=0
for i in t:
    total+=i
print("Square root is:",math.sqrt(total))