import random
num1 = 4
num2 = 7
c = num1 - num2
print(c)

#and
#or
#not

##identity operators
#x is True
#x is not True

##memorship opertors
#in
#not in
number = 10

if 10 > 0:
    print(f'{number} is a positive number.')
print("Outside")

x = 1
total = 0

if x != 0:
    total += x
    print(total)
print("This is always executed")

number = -5
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
print("outside")


number = 5
if number >= 0:
    if number == 0:
        print("0")
    else:
        print("Number is positive")
else:
    print("Negative")


n = 10
if n >= 10:
    print(10)
    pass
    print(10)
print('hello')


print(random.randrange(10,20))
print(random.random())
