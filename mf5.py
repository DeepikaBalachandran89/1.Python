#with NO AgeCategory   no return
def AgeCategoryNO():
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
age=int(input("enter the number:"))
deepika=AgeCategoryNO()