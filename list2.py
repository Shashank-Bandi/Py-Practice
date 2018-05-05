l = [10,20,30,40,50]
target = int(input("Enter a value to search:"))

try:
    print(target,"Available at index",l.index(target))
except ValueError:
    print(target,"not available")
