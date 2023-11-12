#1
'''
from functools import reduce
import operator

def multiply_all(numbers):
    if not numbers:
        return None
    else:
        return reduce(operator.mul, numbers)
def main():
    try:
        input_numbers = input()
        numbers = [float(num) for num in input_numbers.split()]
        result = multiply_all(numbers)
        if result is not None:
            print(f"The product of all numbers in the list is: {result}")
        else:
            print("The list is empty.")
    except ValueError:
        print("Invalid input. Please enter valid numbers separated by spaces.")
if __name__ == "__main__":
    main()
'''
#2
'''
def count_case_letters(input_string):
    upper_count = sum(1 for char in input_string if char.isupper())
    lower_count = sum(1 for char in input_string if char.islower())
    return upper_count, lower_count
def main():
    input_string = input()
    upper_count, lower_count = count_case_letters(input_string)

    print(f"\nuppercase letters: {upper_count}")
    print(f"lowercase letters: {lower_count}")
if __name__ == "__main__":
    main()
'''
#3
'''
def is_palindrome(input_string):
    i, j = 0, len(input_string) - 1
    while i < j:
        while i < j and not input_string[i].isalnum():
            i += 1
        while i < j and not input_string[j].isalnum():
            j -= 1
        if input_string[i].lower() != input_string[j].lower():
            return False
        i += 1
        j -= 1

    return True
def main():
    input_string = input()
    if is_palindrome(input_string):
        print(f"is a palindrome.")
    else:
        print(f"is not a palindrome.")
if __name__ == "__main__":
    main()
'''
#4
'''
import math
import time
def delayed_square_root(number, milliseconds):
    time.sleep(milliseconds / 1000)
    return math.sqrt(number)
def main():
        number = float(input())
        milliseconds = int(input())
        if milliseconds < 0:
            raise ValueError("Delay should be a non-negative value.")
        result = delayed_square_root(number, milliseconds)
        print(f"Square root of {number} after {milliseconds} milliseconds is {result}")
if __name__ == "__main__":
    main()
'''
#5
'''
def all_true(tuple_elements):
    return all(tuple_elements)
def main():
    tuple_elements = eval(input())
    if isinstance(tuple_elements, tuple):
        print(f"all elements are True: {all_true(tuple_elements)}")
    else:
        print("input is not a tuple.")
if __name__ == "__main__":
    main()
'''