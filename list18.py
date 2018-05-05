l1 = eval(input("Enter list 1:"))
l2 = eval(input("Enter list 2:"))
#l1 = [1,2,3,4]
#l2 = [2,5,6,7]
c=int()
for x in l1:
    if x in l2:
        c = c+1

if c>0:
    print("True")
else:
    print("False")
