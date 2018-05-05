list = eval(input("Enter list of words:"))

word_len=[]
##l = int()
for x in list:
    l = len(x)
    word_len.append(l)

word_len.sort(reverse=True)

print(word_len[0])
