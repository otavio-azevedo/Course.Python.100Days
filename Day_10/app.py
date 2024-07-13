import os
from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


print(logo)

new_calculation = True
while(new_calculation):
    first_number = float(input("What's the first number?: "))

    operations_info = ""

    for key in operations:
        operations_info += f"{key}, "

    operations_info = operations_info.rstrip(", ")

    operation = input(f"What's the operation? ({operations_info}): ")

    second_number = float(input("What's the second number?: "))

    operation_result = operations[operation](first_number, second_number)
    print(f"{first_number} {operation} {second_number} = {operation_result}")

    new_calculation_str = input("Do you want to do a new calculation?: (y/n)")
    new_calculation = True if new_calculation_str == "y" else False
    os.system("cls")
