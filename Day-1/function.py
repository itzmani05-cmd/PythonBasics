def greet():
    print("Hello world")

greet()

def add(num1,num2):
    sum = num1+num2;
    print(sum)
add(2,3)

def add(num1,num2):
    sum = num1+num2;
    return sum
c = add(2,3)
print(c)

a = 10 #global variable
def val():
    b = 20 #variable scope
    print(b)
val()


# outside function 
def outer():
    message = 'local'

    # nested function  
    def inner():
        
        # declare nonlocal variable
        nonlocal message

        message = 'nonlocal'
        print("inner:", message)

    inner()
    print("outer:", message)

outer()

def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))
        #1*2*3 = 6


num = 3
print("The factorial of", num, "is", factorial(num))