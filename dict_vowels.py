s1 = input("Enter a string:")
v = {'a','e','i','o','u'}
d=dict()
for x in s1:
    if x in v:
        d[x] = d.get(x,0)+1

print("Vowels and count")
print(d)
