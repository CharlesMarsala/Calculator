"""This program is a calculator and its purpose is to help solve simple math
problems."""
__author__ = "Charles Marsala"

import math
import time


def addition(num1, num2):
    """
This function gets 2 values and adds them
    :param num1: First number
    :param num2: Second number to be added
    :return: the value of the addition
    """
    return num1 + num2


def subtraction(num1, num2):
    """
This function gets 2 values and subtracts them
    :param num1: First number
    :param num2: Second number that is going to be subtracted
    :return: the value of the subtraction
    """
    return num1 - num2


def division(num1, num2):
    """
This function gets a numerator and a denominator and divides them
    :param num1: Numerator
    :param num2: Denominator
    :return: The value of the division
    """
    return num1 / num2


def multiplication(num1, num2):
    """
This function gets 2 numbers and multiply then
    :param num1: First number
    :param num2: Second number that is going to be multiplied by the first
    :return: The value of the multiplication
    """
    return num1 * num2


def absolute_division(num1, num2):
    """
This function gets a numerator and a denominator and divides them
    :param num1: Numerator
    :param num2: Denominator
    :return: The whole value of the division
    """
    return num1 // num2


def remainder(num1, num2):
    """
This function gets a numerator and a denominator and divides them
    :param num1: Numerator
    :param num2: Denominator
    :return: The remainder of the division
    """
    return num1 % num2


def exponent(num1, num2):
    """
This function gets 2 numbers and elevate the first number to the power of the
 second
    :param num1: First number
    :param num2: The exponent
    :return:The value of the Exponentiation
    """
    return num1 ** num2


def square_root(num1):
    """
This function calculates the square root of a given number
    :param num1: A positive number
    :return: The value of the square root
    """
    return math.sqrt(num1)


def is_perfect(number_test):
    """
This function tests to see if the given number is a perfect square
    :param number_test: The number to be tested
    :return: Returns if the number is a perfect square or not
    """
    sqrt = math.isqrt(number_test)

    if sqrt * sqrt == number_test:
        print(number_test, " is a perfect square!", "\n")

    else:
        print(number_test, " is not a perfect square", "\n")

    return 0


def main():
    """
This is the main function and it runs the entire program.
       """
    # Here im presenting the calculator
    validation = True
    while validation:
        name = input("What is your name?: ")
        if name.isalpha():
            print("Hello " + name, end="! Welcome to Charles' Calculator! \n"
                                       "This program is a"
                                       " calculator and its purpose is to "
                                       "help solve"
                                       " simple math problems.\n",
                  sep="")
            validation = False
        else:
            print("Invalid name")

    # Now we start the calculator

    time.sleep(1)  # This puts a delay for the next output for 3 seconds
    loop = 0
    while loop == 0:  # This keeps the program running until the user inputs
        # '0'
        time.sleep(1)
        try:
            pick_function = str(input("\nPlease enter the digit that "
                                      "corresponds to the function "
                                      "you "
                                      "want to use \n(1) - Addition \n(2) -"
                                      " Subtraction \n(3) - "
                                      "Division \n(4) - Multiplication\n(5) - "
                                      "Absolute Division \n("
                                      "6) - Remainder \n(7) - Power \n(8) - "
                                      "Square Root \n(9) - Is "
                                      "Perfect square test\n(?) - OR AND BUT"
                                      " Explanation\n(!) - "
                                      "Average calculator\n"))

            if pick_function == '1':

                inside_loop = 0
                while inside_loop == 0:
                    try:
                        num1 = float(input("Enter the first number: "))
                        num2 = float(input("Enter the second number: "))
                        print(num1, " + ", num2, " = ", addition(num1, num2),
                              "\n")
                        inside_loop += 1
                        time.sleep(2)
                        valid_response = True
                        while valid_response:
                            proceed = input(
                                "To continue using the program type (y / yes)"
                                "\nTo stop the "
                                "program type (n / no)\n")
                            try:
                                if proceed == 'yes' or proceed == 'y':
                                    valid_response = False
                                elif proceed == 'no' or proceed == 'n':
                                    valid_response = False
                                    loop += 1
                                else:
                                    print("Invalid Response, try again.")

                            except ValueError:
                                print("Invalid selection, try again.")

                    except ValueError:
                        print("Invalid input. \nPlease enter a number")

            if pick_function == '2':

                inside_loop = 0
                while inside_loop == 0:
                    try:
                        num1 = float(input("Enter the first number: "))
                        num2 = float(input("Enter the second number: "))
                        print(num1, " - ", num2, " = ",
                              subtraction(num1, num2), "\n")
                        inside_loop += 1
                        time.sleep(2)
                        valid_response = True
                        while valid_response:
                            proceed = input(
                                "To continue using the program type (y / yes)"
                                "\nTo stop the "
                                "program type (n / no)\n")
                            try:
                                if proceed == 'yes' or proceed == 'y':
                                    valid_response = False
                                elif proceed == 'no' or proceed == 'n':
                                    valid_response = False
                                    loop += 1
                                else:
                                    print("Invalid Response, try again.")

                            except ValueError:
                                print("Invalid selection, try again.")

                    except ValueError:
                        print("Invalid input. \nPlease enter a number")

            if pick_function == '3':

                inside_loop = 0
                while inside_loop == 0:
                    try:
                        num1 = float(input("Enter the numerator: "))
                        num2 = float(input("Enter the denominator: "))
                        print(num1, " / ", num2, " = {:.3f}"
                              .format(division(num1, num2)), "\n")
                        inside_loop += 1
                        time.sleep(2)
                        valid_response = True
                        while valid_response:
                            proceed = input(
                                "To continue using the program type (y / yes)"
                                "\nTo stop the "
                                "program type (n / no)\n")
                            try:
                                if proceed == 'yes' or proceed == 'y':
                                    valid_response = False
                                elif proceed == 'no' or proceed == 'n':
                                    valid_response = False
                                    loop += 1
                                else:
                                    print("Invalid Response, try again.")

                            except ValueError:
                                print("Invalid selection, try again.")

                    except ValueError:
                        print("Invalid input. \nPlease enter a number")

            if pick_function == '4':

                inside_loop = 0
                while inside_loop == 0:
                    try:
                        num1 = float(input("Enter the first number: "))
                        num2 = float(input("Enter the second number: "))
                        print(num1, " * ", num2, " = ",
                              multiplication(num1, num2), "\n")
                        inside_loop += 1
                        time.sleep(2)
                        valid_response = True
                        while valid_response:
                            proceed = input(
                                "To continue using the program type (y / yes)"
                                "\nTo stop the "
                                "program type (n / no)\n")
                            try:
                                if proceed == 'yes' or proceed == 'y':
                                    valid_response = False
                                elif proceed == 'no' or proceed == 'n':
                                    valid_response = False
                                    loop += 1
                                else:
                                    print("Invalid Response, try again.")

                            except ValueError:
                                print("Invalid selection, try again.")

                    except ValueError:
                        print("Invalid input. \nPlease enter a number")

            if pick_function == '5':

                inside_loop = 0
                while inside_loop == 0:
                    try:
                        num1 = float(input("Enter the numerator: "))
                        num2 = float(input("Enter the denominator: "))
                        print(num1, " / ", num2, " = ",
                              absolute_division(num1, num2), "\n")
                        inside_loop += 1
                        time.sleep(2)
                        valid_response = True
                        while valid_response:
                            proceed = input(
                                "To continue using the program type (y / yes)"
                                "\nTo stop the "
                                "program type (n / no)\n")
                            try:
                                if proceed == 'yes' or proceed == 'y':
                                    valid_response = False
                                elif proceed == 'no' or proceed == 'n':
                                    valid_response = False
                                    loop += 1
                                else:
                                    print("Invalid Response, try again.")

                            except ValueError:
                                print("Invalid selection, try again.")

                    except ValueError:
                        print("Invalid input. \nPlease enter a number")

            if pick_function == '6':

                inside_loop = 0
                while inside_loop == 0:
                    try:
                        num1 = float(input("Enter the first number: "))
                        num2 = float(input("Enter the second number: "))
                        print(num1, " / ", num2, " = ", remainder(num1, num2),
                              "\n")
                        inside_loop += 1
                        time.sleep(2)
                        valid_response = True
                        while valid_response:
                            proceed = input(
                                "To continue using the program type (y / yes)"
                                "\nTo stop the "
                                "program type (n / no)\n")
                            try:
                                if proceed == 'yes' or proceed == 'y':
                                    valid_response = False
                                elif proceed == 'no' or proceed == 'n':
                                    valid_response = False
                                    loop += 1
                                else:
                                    print("Invalid Response, try again.")

                            except ValueError:
                                print("Invalid selection, try again.")

                    except ValueError:
                        print("Invalid input. \nPlease enter a number")

            if pick_function == '7':

                inside_loop = 0
                while inside_loop == 0:
                    try:
                        num1 = float(input("Enter the first number: "))
                        num2 = float(input("Enter the exponent: "))
                        print(num1, "^", num2, " = ", exponent(num1, num2),
                              "\n")
                        inside_loop += 1
                        time.sleep(2)
                        valid_response = True
                        while valid_response:
                            proceed = input(
                                "To continue using the program type (y / yes)"
                                "\nTo stop the "
                                "program type (n / no)\n")
                            try:
                                if proceed == 'yes' or proceed == 'y':
                                    valid_response = False
                                elif proceed == 'no' or proceed == 'n':
                                    valid_response = False
                                    loop += 1
                                else:
                                    print("Invalid Response, try again.")

                            except ValueError:
                                print("Invalid selection, try again.")

                    except ValueError:
                        print("Invalid input. \nPlease enter a number")

            if pick_function == '8':

                inside_loop = 0
                while inside_loop == 0:
                    try:
                        num1 = float(input("Enter a positive number: "))
                        print("The square root of ", num1, " is = {:.4f}".
                              format(square_root(num1)), "\n")
                        inside_loop += 1
                        time.sleep(2)
                        valid_response = True
                        while valid_response:
                            proceed = input(
                                "To continue using the program type (y / yes)"
                                "\nTo stop the "
                                "program type (n / no)\n")
                            try:
                                if proceed == 'yes' or proceed == 'y':
                                    valid_response = False
                                elif proceed == 'no' or proceed == 'n':
                                    valid_response = False
                                    loop += 1
                                else:
                                    print("Invalid Response, try again.")

                            except ValueError:
                                print("Invalid selection, try again.")

                    except ValueError:
                        print("Invalid input. \nPlease enter a number")

            if pick_function == '9':

                inside_loop = 0
                while inside_loop == 0:
                    try:
                        number_test = int(input("Enter the number to see if"
                                                " it is"
                                                " a perfect square: "))
                        is_perfect(number_test)
                        inside_loop += 1
                        time.sleep(2)
                        valid_response = True
                        while valid_response:
                            proceed = input(
                                "To continue using the program type (y / yes)"
                                "\nTo stop the "
                                "program type (n / no)\n")
                            try:
                                if proceed == 'yes' or proceed == 'y':
                                    valid_response = False
                                elif proceed == 'no' or proceed == 'n':
                                    valid_response = False
                                    loop += 1
                                else:
                                    print("Invalid Response, try again.")

                            except ValueError:
                                print("Invalid selection, try again.")

                    except ValueError:
                        print("Invalid input. \nPlease enter a number")

            if pick_function == '!':

                inside_loop = 0
                while inside_loop == 0:
                    try:
                        quantity = int(input("Please enter the number of "
                                             "digits you want to "
                                             "calculate the average for: "))
                        list_avg = []
                        print("Enter the integer(s): ")

                        for j in range(quantity):
                            number = int(input())
                            list_avg.append(number)
                        print((sum(list_avg)) / len(list_avg))
                        inside_loop += 1
                        time.sleep(2)
                        valid_response = True
                        while valid_response:
                            proceed = input(
                                "To continue using the program type (y / yes)"
                                "\nTo stop the "
                                "program type (n / no)\n")
                            try:
                                if proceed == 'yes' or proceed == 'y':
                                    valid_response = False
                                elif proceed == 'no' or proceed == 'n':
                                    valid_response = False
                                    loop += 1
                                else:
                                    print("Invalid Response, try again.")

                            except ValueError:
                                print("Invalid selection, try again.")

                    except ValueError:
                        print("Invalid input. \nPlease enter a number")

            if pick_function == '?':
                x = 10
                y = 7
                # Now i'll explain 'OR'
                print("We are going to assign X = 10 and Y = 7 to exemplify"
                      " the "
                      "use of 'OR, AND, NOT' ")
                print("You will use 'OR' when you want to compare some given "
                      "data and if at least one of the information is True "
                      "the statement is True as "
                      "well, and it will only be False if both are False "
                      "\nCheck the example below.\n")
                print("If X == Y or X > Y print 'True' otherwise print "
                      "'False'")
                if x == y or x > y:
                    print(True)
                else:
                    print(False, "\n")
                time.sleep(4)
                print()
                print()
                # Now I'll explain 'AND'
                print("You will use 'AND' when you want to compare some given "
                      "data and if both information are True the statement is "
                      "True as "
                      "well, and it is False if at least 1 of the information"
                      " is False \nCheck the example below.\n")
                print("If X == Y and X >= Y print 'True' otherwise print "
                      "'False'")
                if x == y and x >= y:
                    print(True)
                else:
                    print(False, "\n")
                time.sleep(4)
                print()
                print()
                # Now I'll explain 'NOT'
                print("You will use 'NOT' when you want to compare some "
                      "given data"
                      " and if the information is False the statement is "
                      "True  "
                      "and it is False if the information is True "
                      "\nCheck the example below.\n")
                print("If not X == Y ")
                if not x == y:
                    print(True)
                else:
                    print(False, "\n")
                time.sleep(2)

                valid_response = True
                while valid_response:
                    proceed = input("To continue using the program type "
                                    "(y / yes)\nTo stop the "
                                    "program type (n / no)\n")
                    try:
                        if proceed == 'yes' or proceed == 'y':
                            valid_response = False
                        elif proceed == 'no' or proceed == 'n':
                            valid_response = False
                            loop += 1
                        else:
                            print("Invalid Response, try again.")

                    except ValueError:
                        print("Invalid selection, try again.")

        except ValueError:
            print("Invalid input. \nPlease enter a number")

    print("-" * 100)
    print("Thank you for using my calculator!")
    print("-" * 100)


if __name__ == "__main__":
    main()
