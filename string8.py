main = input("Enter Main String:")
sub = input("Enter sub string:")

if sub in main:
    print("Sub string is present")

    print("Count of sub string in string is", main.count(sub,0,len(main)))
    
