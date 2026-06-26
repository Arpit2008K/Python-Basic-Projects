class Student:
    def __init__(self,name, roll_no, marks_list):
        self.name=name
        self.roll_no=roll_no
        self.marks_list=marks_list
    def add_mark(self,mark):
        if mark>100:
            print("Marks cannot be greater than 100")
        elif mark<0:
            print("Marks cannot be lesser than 0")
        else:
            self.marks_list.append(mark)

    def get_average(self):
        if self.marks_list==[]:
            print("There are no marks entered")
            return
        total=0
        for i in self.marks_list:
            total+=i
        return total /len(self.marks_list)
    def display_info(self):
        print("The details are")
        print("Name:",self.name)
        print("Roll number:",self.roll_no)
        print("Marks:",self.marks_list)

name=input("Enter your name:")
roll=input("Enter your roll number:")
s1=Student(name,roll,[])
n=int(input("Enter total number of subjects:"))
for i in range(n):
    m=float(input("Enter marks:"))
    s1.add_mark(m)
s1.display_info()
print("Average:",s1.get_average())