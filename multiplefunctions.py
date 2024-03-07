class multiplefunctions():
    def oddeven():
        num=int(input("Enter the number:"))
        if((num%2)==0):
            print("Even Number")
            con="Even Number"
        else:
            print("Odd Number")
            con="Odd Number"
        return con
    def BMI():
        BMI=int(input("Enter the BMI:"))
        if(BMI<18.5):
            print("UnderWeight")
            body="UnderWeight"
        elif(BMI<24.9):
            print("Normal")
            body="Normal"
        elif(BMI<29.9):
            print("Overweight")
            body="Overweight"
        else:
            print("Vey OverWeight")
            body="Very OverWeight"
        return body