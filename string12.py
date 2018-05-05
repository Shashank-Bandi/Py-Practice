print("------------Reversing Word in sentence-----------")
s1 = "Shashank Bandi is a good boy"
print(s1)

sep = s1.split()
print(sep)

new_list=[]
finallist=[]
i= (len(sep)-1)

while (i>=0):
    new_list = sep[i]
    finallist.append(new_list)
    i=i-1

print(finallist)

print("--------------------Reversing Entire String----------")

print(s1[::-1])
