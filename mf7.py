#BMI in function
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
