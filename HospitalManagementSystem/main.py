import pickle


def getDetails():
    global id_, name, age, sex
    id_ = input("\nEnter patient's id: ")
    name = input("Enter patient's name: ")
    age = input("Enter patient's age:")
    sex = input("Enter patient's gender: ")


def display():
    found = False
    try:
        with open("data", "rb") as f:
            dataLst = pickle.load(f)
    except:
        print("\nDatabase is empty!!\n")

    else:
        id_ = input("\nEnter patient id: ")
        for lst in dataLst:
            if lst[0] == id_:
                found = True
                print(f"Available details for patient '{id_}':")
                print(f"Name : {lst[1]}")
                print(f"Age : {lst[2]}")
                print(f"Gender : {lst[3]}")

        if not found:
            print("\nPatient not found!!\n")


def add():
    try:
        with open("data", "rb") as f:
            dataLst = pickle.load(f)
    except:
        dataLst = []

    getDetails()
    lst = [id_, name, age, sex]
    dataLst.append(lst)

    with open("data", "wb") as f:
        pickle.dump(dataLst, f)


def update():
    found = False
    try:
        with open("data", "rb") as f:
            dataLst = pickle.load(f)
    except:
        print("\nDatabase is empty!!\n")
    else:
        idTemp = input("\nEnter patient id: ")
        for index, lst in enumerate(dataLst[:]):
            if lst[0] == idTemp:
                found = True
                print("Existing data found...")

                print("Enter updated details: ")
                getDetails()
                dataLst.pop(index)
                dataLst.insert(index, [id_, name, age, sex])

                with open("data", "wb") as f:
                    pickle.dump(dataLst, f)
                print("\nUpdate complete...\n")
        
        if not found:
            print("\nPatient not found!!\n")


def remove():
    found = False
    try:
        with open("data", "rb") as f:
            dataLst = pickle.load(f)
    except:
        print("\nDatabase is empty!!\n")
    else:
        id_ = input("\nEnter patient id: ")
        
        for index, lst in enumerate(dataLst[:]):
            if lst[0] == id_:
                found = True
                choice = input(f"Are you sure you want to delete {id_}'s data (Y/N): ")
                if choice.lower() == "y":
                    dataLst.pop(index)

                    with open("data", "wb") as f:
                        pickle.dump(dataLst, f)
                    print("\nPatient data deleted!!\n")
                else:
                    print("Cancelled...\n")
            if not found:
                print("\nPatient not found!!\n")


welcome = '''\nHOSPITAL MANAGEMENT SYSTEM\n
1. Display Patient Details
2. Add Patient Details
3. Update Patient Details
4. Remove Patient Details
5. Exit\n'''



def main():
    run = True

    while run:
        print(welcome)
        try:
            choice = int(input("Enter choice: "))
            if choice not in (1, 2, 3, 4, 5):
                raise ValueError
        except ValueError:
            main()
        
        if choice == 1:
            display()
        elif choice == 2:
            add()
        elif choice == 3:
            update()
        elif choice == 4:
            remove()
        else:
            run = False

main()