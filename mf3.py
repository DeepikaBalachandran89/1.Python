#functions of single input in multiple proceedures
age=int(input("enter the number:"))
def AgeCategory():
        if(age<19):
            print("children")
            vari="children"
        elif(age<35):
            print("adult")
            vari="adult"
        elif(age<59):
            print("citizen")
            vari="citizen"
        else:
            print("senior citizen")
        return vari