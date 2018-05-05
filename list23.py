import itermore
import inspect
l=eval(input("Enter list of values:"))
size = len(l)
i=0
g=[]
while i<size:
    g.append(1)
    i=i+1
    
final = itermore.gpermutations(l,g)

for  x in final:
    print(x)

lines = inspect.getsource(itermore.gpermutations(l,g))
print(lines)
