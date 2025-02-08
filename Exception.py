#exception = 1/0
#print(exception)

#print(dir(locals()['__builtins__']))

try:
    print(3/0)
except:
    print("Error")

try:
    list = [2,34,5,1]
    print(list[5])
except ZeroDivisionError:
    print("Denominator cannot be 0")
except IndexError:
    print("Index out of Bound")

try:
    no = 5
    assert no % 2 == 0
    print("Even number")
except:
    print("Not an even number")


try:
    num = 10/0
    print(num)
except:
    print("Error")
finally:
    print("This is finally block.")

##Custom exception
class InvalidAge(Exception):
    "age is greater than 18"
    pass

number = 18
try:
    input = 15
    if(input < number):
        raise InvalidAge
    else:
        print("Eligible to Vote")
except:
    print("Exception occured")
