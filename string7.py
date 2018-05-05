name = ""
list = ['Shashank','Sarath','Tarun','Alekhya','Sanjana']
while name not in list:
    name = input("Enter a name:")
    if name.strip() in list:
        print(name,"is in the list, Thank you!!")
    else:
        print(name,"is not in the list, Please enter again")
    
