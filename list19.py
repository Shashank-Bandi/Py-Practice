l1 = eval(input("Enter list:"))
n = eval(input("Enter the indexes:"))
for x in n:
    del l1[x]

print("Reformed list:",l1)
