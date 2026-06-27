import math
try:
    sentence=input("Enter a sentence:")
    words=sentence.split()
    words=set(words)
    print("Sorted Words:")
    print(sorted(words))
    print("Square of total number of unique words:",math.pow(len(words),2))
except:
    print("Unexpected Error Occurred")