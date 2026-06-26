def student_database():
    student={}
    while True:
        try:
            print()
            print("Enter 1 to add")
            print("Enter 2 to search by roll number")
            print("Enter 3 to display all students")
            print("Enter 4 to exit")
            ch=int(input("Enter your choice:"))
            print()

            if ch==1:
                roll=int(input("Enter your roll number:"))
                name=input("Enter your name:")
                age=int(input("Enter your age:"))
                city=input("Enter your city name:")
                student[roll]={
                    "Name":name,
                    "Age":age,
                    "City":city
                }
            elif ch==2:
                roll=int(input("Enter your roll number:"))
                if roll in student:
                    print(student.get(roll))
                else:
                    print("Roll number not found")
            elif ch==3:
                print(student)
            elif ch==4:
                print("Exiting.....")
                break
            else:
                print("Enter a valid choice!")
        except ValueError:
            print("Enter numeric value")
student_database()