#task 1
class string:
    input_string = ""
    def getString():
        string.input_string = input("enter a string: ")
    def printString():
        print(string.input_string.upper())
string.getString()
string.printString()

#task 2
class Shape:
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length ** 2
    
#task 3
class Rectangle(Shape):
    def __init__(self, length, width):
        self.width = width
        self.length = length
    def area(self):
        return self.length * self.width
    
#task 4
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print("Point coordinates:", self.x, self.y)
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
    
#task 5
class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            print("Invalid deposit amount. Please deposit a positive amount.")
            return False
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                return True
            else:
                print("Insufficient funds. Withdrawal amount exceeds the available balance.")
                return False
        else:
            print("Invalid withdrawal amount. Please withdraw a positive amount.")
            return False
        
#task 6
def is_prime(num):
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

