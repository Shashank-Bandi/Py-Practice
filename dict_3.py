n = int(input("Enter no of students you want to enter:"))
i=1
d = dict()
while(i<=n):
    name = input("Enter name of student:")
    marks = eval(input("Enter marks of student:"))
    d[name] = marks
    i = i+1
print("Following are the details entered")
print(d)
x = input("Enter name of the student:")
print("Marks of the student are:",d.get(x))

while True:
    name = input("Enter name of student:")
    marks = d.get(name ,-1)
    print("Marks:",d.get(name))
    if marks=='-1':
        print(d.setdefault(name,"Marks have not been entered"))
        print(d)
    choice = input("Do u want to continue?Yes|No:")
    if choice == "No":
        break
    else:
        continue
