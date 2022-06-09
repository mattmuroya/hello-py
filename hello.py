import math
print("Hello, world!")


# strings

first, last = "matt", "muroya"
full = f"{first} {last}"
first_name_length = len(first)

course = "Python Programming"

print(course[0])  # "P"
print(course[-1])  # "g"
print(course[0:3])  # "Pro" (slice)

print(type(course))  # str
print(course.upper())
print(course.lower())
print(course.title())  # title case

print(course.strip())  # trim whitespace

print(course.find("Pro"))  # returns index 9, -1 for not found
print(course.replace("P", "B"))  # "Bython Programming"
print("Programming" in course)  # True

# numbers

x = 10  # decimal
x = 0b10  # binary (2 in decimal)
print(bin(x))  # 0b10 prints binary format

x = 10 + 3
x = 10 - 3
x = 10 * 3
x = 10 / 3  # returns float
x = 10 // 3  # returns int
x = 10 ** 3  # pow
x = 10 % 3  # mod

x = x + 1
x += 1  # no incrementor++/decrementor--

x = 0x12c  # hexadecimal
print(hex(x))  # 0x12c


PI = 3.14
print(round(PI))  # 3
print(abs(PI))  # absolute val
print(math.floor(PI))  # import math

# logical operators: and, or, not
# if/else blocks

age = int(input("age?"))
if age >= 18:
    print("adult")
elif age >= 13:
    print('teen')
elif age >= 9:
    pass  # does nothing; skips to next evaluation
else:
    print('child')

# chaining operators

if 18 <= age < 65:
    print("eligible")

# ternary operators

print("eligible" if age >= 18 else "not eligible")

# for loops

for x in "Python":
    print(x)

for x in ["a", "b", "c"]:
    print(x)

for x in range(5):  # note: range returns a range obj, not a list
    print(x)

for x in range(2, 5):  # range obj takes less memory than a list
    print(x)

for x in range(0, 10, 2):  # start index, stop index, step
    print(x)

names = ["John", "Mary"]
for name in names:
    if name.startswith("J"):
        print("Found")
        break
else:  # if for loop iterates through all elem without break, execute else
    print("Not found")

# while loops

guess = 0
answer = 5

while answer != guess:
    guess = int(input("Guess: "))
# else:  # optional; executes if the while loop completes without a break statement
#     pass

# functions
# pep8 puts double line breaks between function declarations


def increment(number, by=1):  # by=1 is default value, making second argument optional
    return (number, number + by)  # can return multiple values


def decrement(number: int, by: int = 1) -> tuple:  # can type funcs and args
    return (number, number - by)


# returns multiple values as a tuple; like an immutable list
print(increment(2, 3))


print(increment(2, by=3))  # can use named parameters called "keyword argument"

# args


# def multiply(*list):  # returns tuple. works like ...args in JavaScript
#     total = 1
#     for num in list:
#         total *= num
#     return total


# print(multiply(2, 3, 4, 5))


def save_user(**user):  # accepts keyword arguments and builds a dictionary, analogous to a JS object
    print(user)


# called with two keyword arguments, returns {'id': 1, 'name': 'admin'}
save_user(id=1, name="admin")

# scope

message = "a"


def greet():
    if True:
        # python enforces new variable declaration; does not modify global message var "a"
        # global message  # if you use global keyword, it tells python to modify the global version of the variable
        # try to avoid global variables in general as a best practice
        message = "b"  # function local scope; python does not have block-level scope
    print(message)


print(message)
greet()


# debugging
# create launch.json in debugging panel
# F9 to set breakpoint
# F5 to launch debug

def multiply(*numbers):
    total = 1
    for num in numbers:
        total *= num
    return total


print("start")
print(multiply(1, 2, 3))
print("finish")

# fizzbuzz
# if input is divisible by 3 return "Fizz"
# if input is divisible by 5 return "Buzz"
# if input is divisible by 3 and 5 return "FizzBuzz"


def fizz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        print("FizzBuzz")
    elif input % 3 == 0:
        print("Fizz")
    elif input % 5 == 0:
        print("Buzz")
    else:
        print(input)
    return


fizz_buzz(3)
fizz_buzz(5)
fizz_buzz(7)
fizz_buzz(15)
