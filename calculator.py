"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


active = True

while active:
    equation = input("Type an equation to calculate: ")

    elements_in_equation = equation.split(' ')
    calc_type = elements_in_equation.pop(0)
    int_elements = []

    for element in elements_in_equation:
        element = int(element)
        int_elements.append(element)
    
    if calc_type == "add":
        calc = add(int_elements[0], int_elements[1])  

    elif calc_type == "subtract":
        calc = subtract(int_elements[0], int_elements[1])

    elif calc_type == "multiply":
        calc = multiply(int_elements[0], int_elements[1])

    elif calc_type == "divide":
        calc = divide(int_elements[0], int_elements[1])

    elif calc_type == "square":
        calc = square(int_elements[0])

    elif calc_type == "cube":
        calc = cube(int_elements[0])

    elif calc_type == "power":
        calc = power(int_elements[0], int_elements[1])

    elif calc_type == "mod":
       calc = mod(int_elements[0], int_elements[1])

    elif calc_type == "q":
        active = False
        quit()

    else:
        input("Invalid command\n")
        calc = None
    
    if calc:
        print(calc)
