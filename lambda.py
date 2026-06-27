s=lambda x: x*x
sq=[]
for i in range(1,21):
    sq.append(s(i))
print("Even Squares")
for i in sq:
    if i%2==0:
        print(i)