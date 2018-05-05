l1 = eval(input("Enter  list 1:"))
l2 = eval(input("Enter list 2:"))
s1 = set(l1)
s2 = set(l2)

s3 = s1.intersection(s2)
final = list(s3)
if len(final)>0:
    print("True")
else:
    print("No Common elements")
