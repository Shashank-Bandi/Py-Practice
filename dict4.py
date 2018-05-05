s=input("Enter string to read:")
d = dict()
for x in s:
    d[x]=d.get(x,0)+1

for k,v in d.items():
    print("{} occurred {} times".format(k,v))
    
