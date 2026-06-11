mydic = {'a':"apple",50:"Sachin","p":"python",99:99.90}
for i in mydic:
    print(f"key is {i} value is {mydic[i]}")
    mydic  = {}
    key = input("Enter Key: ")
    value = input("Enter Value: ")

    mydic[key] = value
    for i in mydic:
        print(f"key is {i} value is {mydic[i]}")
