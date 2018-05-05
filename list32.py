l=eval(input("Enter list of values:"))
d=dict()
for x in l:
    d[x]=d.get(x,0)+1

for k,v in d.items():
    print("{} has occurred {} times".format(k,v))
