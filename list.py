try:
    Student = []
    name = input("Enter student's name :")
    Student.append (name)
    print (Student)
    while type(name) is str:
        name = input("Enter student's name :")
        Student.append (name)
        print (Student)
except:
    print('there is an error')