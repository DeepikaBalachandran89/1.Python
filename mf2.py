#function-oops(MUltiple Conditions in set of proceedures)
lists=[10,40,50,60]
def AgeCategory():
    for age in lists:
        if(age<19):
            print("children")
        elif(age<35):
            print("adult")
        elif(age<59):
            print("citizen")
        else:
            print("senior citizen")