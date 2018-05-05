l=eval(input("Enter a list of values:"))
d=dict()
for x in l:
    d[x]=d.get(x,0)+1
print(d)
count=int()
for k,v in d.items():
    if v%2!=0:
        count = k

print(count)
