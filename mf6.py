#logic oddeven
def oddeven():
    num=int(input("Enter the number:"))
    if((num%2)==0):
        print("Even Number")
        con="Even Number"
    else:
        print("Odd Number")
        con="Odd Number"
    return con