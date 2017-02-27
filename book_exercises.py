def f(x):
    return x * 2

def d(x,y,z):
    return (x+y)*z

def no_parameter():
    return 2 + 2

# length function
len("yoo")

def young_old():
    age = input("Enter your age:")
    int_age = int(age)
    if int_age < 21:
        print("You are young!")
    else:
        print("WOW, you are old!")

def even_odd():
    n = input("type a number:")
    n = int(n)
    if n % 2 == 0:
        print(n, " is even")
    else:
        print(n, " is odd")

def f():
    x = 1
    y = 2
    z = 3
    print(x)
    print(y)
    print(z)


try:
    a = input("type a number: ")
    b = input("type another: ")
    a = int(a)
    b = int(b)
    print(a/b)
except(ZeroDivisionError,ValueError):
    print("Invalid Input.")


def squared_function(n):
    print(n*2)

def string_print(str):
    print(str)

'''
4. Write a program with two functions. The first function should take an
integer as a parameter and return the result of the integer divided by 2.
The second function should take an integer as a parameter and return the
result of the integer multiplied by 4. Call the first function, save the
result as a variable, and pass it as a parameter to the second function.
'''

def takes_int():
    a = input("I need a number:")
    int_return = int(a)
    return int_return/2
def times_four(n):
    return n * 4

