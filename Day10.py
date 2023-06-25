# Calculator

def add(firstNumber, secNumber):
    return firstNumber + secNumber


def sub(firstNumber, secNumber):
    return firstNumber - secNumber


def mul(firstNumber, secNumber):
    return firstNumber * secNumber


def div(firstNumber, secNumber):
    return firstNumber / secNumber


def calculator():
    firstNum = float(input("Enter first number:"))

    operations = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div,
    }

    for operators in operations:
        print(operators)

    keep_calculating = True
    while keep_calculating:
        operator = input("Which operation do you want to perform?")
        secNum = float(input("Enter second number:"))

        # result after calculation
        result = operations[operator]
        result = result(firstNum, secNum)
        print(f"{firstNum} {operator} {secNum} = {result}")

        keep_calculating = input(f"Do you want to continue calculating with {result} y or n:").lower()
        if keep_calculating == "y" or keep_calculating == "yes":
            firstNum = result
        elif keep_calculating == "n" or keep_calculating == "no":
            keep_calculating = input(f"Do you want to start new calculation y or n:").lower()
            if keep_calculating == "y" or keep_calculating == "yes":
                # recursive call
                calculator()
            elif keep_calculating == "n" or keep_calculating == "no":
                keep_calculating = False
        else:
            keep_calculating = False
            print("\t\t\t***********")


# calling calculation
calculator()
