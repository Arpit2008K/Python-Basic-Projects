def manage_marks():
    try:
        total=0
        #Created an empty list
        m=[]
        m1=float(input("Enter your marks:"))
        m2=float(input("Enter your marks:"))
        m3=float(input("Enter your marks:"))
        m4=float(input("Enter your marks:"))
        m5=float(input("Enter your marks:"))

        #Stored marks in a list
        m.append(m1)
        m.append(m2)
        m.append(m3)
        m.append(m4)
        m.append(m5)

        #Calculated total of marks
        for i in range(len(m)):
            total+=m[i]
    #Handled Non-numeric input
    except ValueError:
        print("Enter a numeric Value")
    #Printing average
    print("Average marks:",total/len(m))

    #Printing Highest marks
    print("Highest marks:",max(m))

    #Printing Lowest marks
    print("Lowest marks:",min(m))

    ##Printing marks in descending order
    m.sort(reverse=True)
    print("Marks in descending order:",m)

#Calling the function
manage_marks()