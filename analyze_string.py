def index(string):
    count=0
    if string=="":
        print("The string is empty!")
    else:
        print("Lenght of the entered string:",len(str))
        print("Reverse string:",str[-1::-1])

        for i in str:
            a=i.upper()
            if a=="A" or a=="E" or a=="I" or a=="O" or a=="U":
                count+=1
        print("Total number of vowels in the string:",count)
        for i in range(len(str)):
            print("Each Character:",str[i],"it's positive index:",i,"it's negative index:",i-len(str))

str=input("Enter a string:")
index(str)