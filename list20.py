l1 = eval(input("Enter list of values:"))
final=[]
for x in l1:
    if x%2!=0:
        final.append(x)

print(final)
