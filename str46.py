s=input("Enter a string:")
l=['a','e','i','o','u']
d=dict()

for x in s:
    if x in l:
        d[x]=d.get(x,0)+1

print("Vowels:",d)
   
