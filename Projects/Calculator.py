
def add(n1,n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def mul(n1,n2):
    return n1 * n2

def div(n1,n2):
    return round(n1/n2,2)

operators= {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
}

def calculator():
    print("LOGO")
    print("Welome to the calculator app")

    first_num = float(input("Enter a number:"))

    for i in operators:
        print(i)

    should_continue = True

    while should_continue:
        operator = input("Select your operator: ")
        second_num = float(input("Enter another number:"))

        method = operators[operator]
        calculation = method(first_num,second_num)
        print(calculation)
        if input("Do you want to continue? Y/N").upper() == 'Y':
            first_num = calculation
        else:
            print("Restarting")
            should_continue = False
            calculator()

calculator()