#1
'''
def square_generator(n):
    for i in range(1, n + 1):
        yield i**2
n = int(input())
squares = square_generator(n)
for square in squares:
    print(square, end=' ')
'''
#2
'''
def even_numbers_generator(n):
    for num in range(0, n + 1, 2):
        yield str(num)
n = int(input())
even_numbers = even_numbers_generator(n)
print(','.join(even_numbers))
'''
#3
'''
def divisible_by_3_and_4(n):
    for num in range(0, n + 1):
        if num % 3 == 0 and num % 4 == 0:
            yield num
n = int(input())
divisible_numbers = divisible_by_3_and_4(n)
for num in divisible_numbers:
    print(num)
'''
#4
'''
def squares(a, b):
    for num in range(a, b + 1):
        yield num**2

a = int(input())
b = int(input())
square_generator = squares(a, b)
for square in square_generator:
    print(square)
'''
#5
'''
def numbers_to_zero(n):
    for i in range(n, -1, -1):
        yield i
n = int(input())
number_generator = numbers_to_zero(n)
for number in number_generator:
    print(number)
'''
