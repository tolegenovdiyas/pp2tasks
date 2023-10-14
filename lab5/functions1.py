#1
'''
ounces=float(input())
def ounces_to_grams(g):
    g=ounces/28.3495231 
    print(g)

ounces_to_grams(ounces)
'''
#2
'''
f=int(input())
def conversion(c):
    c=(5 / 9) * (f - 32)
    print(c)

conversion(f)    
'''
#3
'''
numheads=int(input())
numlegs=int(input())
def solve(numheads, numlegs):
     for c in range(numheads + 1):
        r = numheads - c
        if(2 * c + 4 * r) == numlegs: print(c, r)
solve(numheads, numlegs)
'''
#4
'''
input_numbers = input()
def isprime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    prime_numbers = filter(isprime, numbers)
    return list(prime_numbers)

numbers = list(map(int, input_numbers.split()))
prime_numbers = filter_prime(numbers)
print(prime_numbers)
'''
#5
'''
string = input()
from itertools import permutations
def print_permutations(input_string):
    permuted_strings = permutations(input_string)
    for permuted_string in permuted_strings:
        print(''.join(permuted_string))
print_permutations(string)
'''
#6
'''
string = input()
def reverse(string):
    r_sentence = string.split()
    reversed_sentence = ' '.join(reversed(r_sentence))
    print(reversed_sentence)
reverse(string)    
'''
#7
'''
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

nums= input()
numbers = [int(num) for num in nums.split()]
result = has_33(numbers)
if result:
    print("True")
else:
    print("False")
'''    
#8
'''
def spy_game(nums):
    code = [0, 0, 7]
    index = 0
    for num in nums:
        if num == code[index]:
            index += 1
            if index == 3:
                return True

    return False
nums = input()
numbers = [int(num) for num in nums.split()]
result = spy_game(numbers)
if result:
    print("True")
else:
    print("False")
'''
#9
'''
import math
def volume(r):
    v=(4/3) * math.pi * (r**3)
    print(v)

radius=int(input())
volume(radius)
'''
#10
'''
def unique(list):
    unique_list = []
    for item in list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list
list = input()
newlist = list.split()
result = unique(newlist)
print(result)
'''
#11
'''
def is_palindrome(word):
    reversed = ''.join(word.split()).lower()
    return reversed == reversed[::-1]
word = input()
result = is_palindrome(word)
if result:
    print("palindrome")
else:
    print("not a palindrome")
'''
#12
'''
def histogram(numbers):
    for num in numbers:
        line = ''
        for _ in range(num):
            line += '*'
        print(line)
list = input()
zvezda_list = [int(x) for x in list.split()]
histogram(zvezda_list)
'''
#13
'''
import random

def guess_the_number():
    name = input("Hello! What is your name?\n")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    secret_number = random.randint(1, 20)
    attempts = 0

    while True:
        guess = input("Take a guess.\n")
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {attempts} {'guess' if attempts == 1 else 'guesses'}!")
            break
guess_the_number()
'''
#14 task in separate file