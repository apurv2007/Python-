mylist = {}
count = int(input("How many Records? "))

for i in range(0,count):
    mykey = input("Enter Key: ")
    mylist[mykey] = input("Enter Value: ")
    print(mykey)
    print(mylist)