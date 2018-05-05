x = int(input("Enter the range of squares:"))
n = int(input("Enter the no of digits, you wish to see:"))
s = [x*x for x in range(1,x)]
print(s)
final=[]
l=len(s)
final = s[:n]+s[l-n:l]   #s[l:l-7:-1]
print(final)
