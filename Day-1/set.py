student_id = {112,332,4,4}
print(student_id)

empty_set = set()
empty_dic = {}

number = {2,4,6,6,2,8}
print(number)

number.add(23)
print(number)

companies = {'L','K','L'}
tech_companies = {'L',"i"}
companies.update(tech_companies)
print(companies)

companies.discard('L')
print(companies)

# first set
A = {1, 3, 5}

# second set
B = {0, 2, 4}

# perform union operation using |
print('Union using |:', A | B)

# perform union operation using union()
print('Union using union():', A.union(B)) 


# first set
A = {1, 3, 5}

# second set
B = {1, 2, 3}

# perform intersection operation using &
print('Intersection using &:', A & B)

# perform intersection operation using intersection()
print('Intersection using intersection():', A.intersection(B)) 