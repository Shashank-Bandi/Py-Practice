sent = input("Enter a sentence:")
i=0
tot = len(sent)
for char in sent:
    print(char,"is at",i,'+VE index',i-tot,'-VE index'  )
    i=i+1


