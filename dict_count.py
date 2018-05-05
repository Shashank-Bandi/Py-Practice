s1 = input("Enter a string to read:")
d = dict()

for x in s1:
    d[x] = d.get(x,0)+1

print(d)
