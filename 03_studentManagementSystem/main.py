import pickle


class Student:

    def __init__(self):
        self.spacing = "\t\t\t  "
        self.val = 40
        

    
    def display(self):
            self.reg = input("Enter student id: ")
            if self.reg.isdigit() != True:
                print("Inself.valid Entry! ID can only contain digits...")
                

            try:
                with open("student", "rb") as f:
                    dataLst = pickle.load(f)
            except FileNotFoundError:
                print("No existing data!")
            except Exception as e:
                print(e)
            else:
                i = 0
                for lst in dataLst:
                    i += 1
                    if self.reg in lst:
                        index = i - 1
                        
                        self.reg = f"ID: {dataLst[index][0]}"
                        self.name = f"Name: {dataLst[index][1]}"
                        self.class_ = f"Class: {dataLst[index][2]}"
                        self.stream = f"Stream: {dataLst[index][3]}"

                        print(f" {67*'='}")
                        print(f"||{65*' '}||")

                        print(f"||{self.spacing}{self.reg}{(self.val - len(self.reg))*' '} ||")
                        print(f"||{self.spacing}{self.name}{(self.val - len(self.name))*' '} ||")
                        print(f"||{self.spacing}{self.class_}{(self.val - len(self.class_))*' '} ||")
                        print(f"||{self.spacing}{self.stream}{(self.val - len(self.stream))*' '} ||")

                        print(f"||{65*' '}||")
                        print(f" {67*'='}")

                        break
                else:
                    print("No existing data found!")
                


    def getDetails(self):
            self.reg = input("Enter student id: ")
            if self.reg.isdigit() != True:
                print("Inavlid Entry! ID can only contain digits...")

            self.name = input("Enter student name: ")
            if self.name.isalpha() != True:
                print("Inavlid Entry! Name can only contain alphabets...")

            self.class_ = input("Enter student class: ")
            if self.class_.isdigit() != True:
                print("Inavlid Entry! Class can only contain digits...")

            self.stream = input("Enter stream: ")



    def addStudent(self):
        try:
            with open("student", "rb") as f:
                self.dataLst = pickle.load(f)
        except:
            self.dataLst = []
        
        self.getDetails()

        self.studentLst = [self.reg, self.name, self.class_, self.stream]
        self.dataLst.append(self.studentLst)

        with open("student", "wb") as f:
            pickle.dump(self.dataLst, f)


    def update(self):
        self.reg = input("Enter student id: ")
        if self.reg.isdigit() != True:
            print("Invalid Entry! Id can only contain digits...")
        
        with open("student", "rb") as f:
            self.dataLst = pickle.load(f)

        i = 0
        for lst in self.dataLst:
            i += 1
            if self.reg in lst:
                print("Data found!")
        
        print("Enter updated details:")
        self.getDetails()

        index = i - 1
        self.dataLst[index][0] = self.reg
        self.dataLst[index][1] = self.name
        self.dataLst[index][2] = self.class_
        self.dataLst[index][3] = self.stream

        with open("student", "wb") as f:
            pickle.dump(self.dataLst, f)

    def remove(self):
        self.reg = input("Enter student id: ")
        if self.reg.isdigit() != True:
            print("Invalid Entry! Id can only contain digits...")
        
        with open("student", "rb") as f:
            self.dataLst = pickle.load(f)

        i = 0
        for lst in self.dataLst:
            i += 1
            if self.reg in lst:
                print("Data found!")
        
        index = i - 1
        a = self.dataLst.pop(index)
        print(a)



obj = Student()


def start():
    
    welcome = '''\nSTUDENT MANAGEMENT SYSTEM
    1. Display Student Data
    2. Add New Student Data
    3. Updata Student Data
    4. Remove Student Data
    5. Exit\n'''
    print(welcome)

    try:
        choice = int(input("Enter choice: "))
        if choice not in (1, 2, 3, 4 ,5):
            raise ValueError
    except ValueError:
        print("Invalid Input! Enter a valid option...\n")


    if choice == 1:
        obj.display()
    elif choice == 2:
        obj.addStudent()
    elif choice == 3:
        obj.update()
    elif choice == 4:
        obj.remove()
    elif choice == 5:
        global run
        run = False


run = True
while run:
    start()