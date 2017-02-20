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
