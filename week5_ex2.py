inOrder = True

number_1 = int(input("Enter a first number: "))
number_2 = int(input("Enter second number: "))
number_3 = int(input("Enter third number: "))

def inOrder():
    if number_3 >= number_2 >= number_1:
        return True
    else:
        return False
    
if inOrder():
    print("In order")
else:
    print("Not in order")