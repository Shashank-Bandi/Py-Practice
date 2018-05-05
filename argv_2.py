#Read group of Values ae command line arguements and print them.
from sys import argv
print("All the values:",argv)
print("Excluding the file name",argv[1:])
print("Printing Individual values:")
for x in argv:
    print(x)
