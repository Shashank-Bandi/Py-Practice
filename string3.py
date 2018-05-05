string = str(input("Enter a string:"))
n = int(input("Enter the number of times you want to print:"))

if (len(string)==2):
    print(string)
else:
    sub=string[:2]
    print(n*sub)
    
