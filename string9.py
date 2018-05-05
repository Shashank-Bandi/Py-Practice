s1 = "Shashank Bandi"
print(s1, sep=',')
print(s1.strip())
print(s1.split())
s2 = "18-04-2018"
print(s2.split('-'))
l=s2.split('-')
for x in l:
    print(x)
for x in range(10):
    print("\n")
s="10,20,30,40,50,60"
l = s.split(",",3)
for x in l:
    print(x)
l = s.rsplit(",",3)
for x in l:
    print(x)
    
