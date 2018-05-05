d = eval(input("Enter Dictionary:"))
l = d.values()
sum = 0
for x in l:
    sum = sum+ x
k = d.keys()
con = ""
for x in k:
    con = con + x
print("Sum of values:",sum)
print("Keys:",con)

