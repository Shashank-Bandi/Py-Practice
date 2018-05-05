l=eval(input("Enter list of values:"))
min =int(input("Enter minimum range:"))
max =int(input("Enter maximum range:"))
ctr=int()
for x in l:
    if min<x<max:
        ctr = ctr+1

print("Count:",ctr)
