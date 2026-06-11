with open("Apurv.txt", "a") as myfile:
    myfile = myfile.write("\n hello world 1")

    with open("Apurv.txt", "r") as myfile:
        mydata = myfile.read()
print(mydata)