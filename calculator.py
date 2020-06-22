def calculate():
    
    num1 = input("Please select a number: ")
    oper = input("please select an operand +, -, *, /: ")
    num2 = input("please select a second number: ")
    if oper == "+":
      add = num1 + num2
      print(add)
    elif oper == "-":
        diff = num1 - num2
        print(diff)
    elif oper == "*":
         mult = num1 * num2
         print(mult)
    elif oper == "/":
            if num2 == 0:
                 Print("Cannot Divide by 0")
            else:
                 div = num1 / num2
                 print(div)
    else:
         print("you did not enter an operand. \n please try again")
         
