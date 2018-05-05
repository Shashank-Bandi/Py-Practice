s = input("Enter a string:")
d = dict()
for x in s:
    d[x] = d.get(x,0)+1

print(d)
