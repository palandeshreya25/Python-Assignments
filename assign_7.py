
def data(file):
    f = open(file,"a+")
    print("File opened successfully")
    try:
        roll_no=input("Enter your rollno :")
        name=input("Enter your name :")
        dept=input("Enter your department :")
        f.writelines(roll_no)
        f.writelines(name)
        f.writelines(dept)
        print("Data written successfully ")
    except FileNotFoundError:
        print("FileNotFound Error Exception Handled Here")
    finally:
        print("No exception")
    f.seek(0)               
    file1=f.readlines()
    print("Data present in File")
    print(file1)           
    print("Data readed successfully")

    f.close()
    print("File closed successfully")
data("shreya.txt")