print("Hello, World")
print('Hello, World')

#Single Line Comments

#command for below line-> to display the value 25
print(25)

#declate a variable
name = "John"
#print the above line -> John
print(name)  #John

#Multi Line Comments

#first line
#second line
#third line
print("HII");

#multiline string as comments
'''multiline
comments'''
print("Welcome")


num1 = 10
num2 = 15
sum = num1 + num2
print("Sum of two above declared number is,", sum)

#assign a value to a variable
language = "Python"
print(language)

#then i am changing the value of a variable...
language = "Java"
print(language)

#assigning multiple values to multiple variables
a, b, c = 5,3.2,"Hello"
print(a)
print(b) 
print(c) #Hello

a = b = "Python"
print(a)
print(b)

#here, Python is a literals
#name is a variable
name = "Python"
print(name)

num = 5
Num = 55
print(num)
print(Num)

##Numberic Literals
#numberic literals are immutable(unchangeable)

#Integer literals
#eg :- 5,11,-11,1,12,0

#FLoating-point literals
#eg :- 2.5,6.76,0.0,-1.45

#complex literals
#here numerals are in the form of a+bj, where a is real and b is imaginary
#eg :- 6+9j

##String literals
#'manikandan'
#'Manikandan'

##Boolean literals
#True and False
#eg :- 
ispass = True
print(ispass)

##Character literals
#eg :- 'g' and also number is also a character literals like '4'
character_literals = 'c'
character_literals2 = '44'
print(character_literals)
print(character_literals2)

##Special literals 
#eg :- None
value = None
print(value)

##collection literals

#list
fruits = ["apple","mango","orange"]
print(fruits)

#tuple
numbers = (1,2,3)
print(numbers)

#dictionary
alphabets = {'a':'apple', 'b':'ball'}
print(alphabets)

#type conversion

##implicit - automatically converts
##explicit - user converts it

#int to float
interger_no = 1
print(type(interger_no))
float_no = 1.1
output_ = interger_no + float_no
print(output_)
print(type(output_))

#str to int
num_string = '12'
print(type(num_string))
num_int = 12
num_string = int(num_string)
print(type(num_string))
new = num_string + num_int
print(new)

print("hii",end= ' ')
print('hello, welcome')

print('new year',2023,'See you soon!',sep= '. ')

x = 5
y = 6
print('The value of x is {} and {}'.format(x,y))

