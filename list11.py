l=eval(input("Enter list of values:"))
c=int()

for x in l:
    #print(x)
    char=str(x)
    size=len(char)
    
    if(char[:1]==char[size:size-2:-1]):
        c=c+1

print(c)
