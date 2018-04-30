ip = input("Enter IP Address:")
ctr = int()
x = ""
s_len=[]
seg_len=int()
for x in ip:
    if x == '.':
        print("Segment length:",seg_len)
        ctr = ctr+1
        seg_len =0
    else:
        seg_len = seg_len+ 1

if x!='.':
    print("Segment length:",seg_len)
    
count = ctr+1 
print("Segments:",count)

print("Length:",len(ip)-ctr)
