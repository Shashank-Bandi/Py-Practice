lst=eval(input("Enter a list of values:"))
l=len(lst)
i=0
final=[]
j=i+1
temp=int()
while(i<l):
    temp = lst[i]
    lst[i]= lst[j]
    lst[j]=temp
    final.append(i)
    final.append(j)
    i=i+2

print(final)
