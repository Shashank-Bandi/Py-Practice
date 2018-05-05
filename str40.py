s=input("Enter a string:")
char=input("Enter the characters to be stripped:")

s1 = "".join(x for x in s if x not in char)
print(s1)
