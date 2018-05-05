number = int(input("Enter the number:"))

i=1
print("Factors are: ")
while(i<=number):
    if(number%i==0):
        print(i)
    i=i+1
