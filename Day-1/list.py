
student = ['Jack',32,'Computer Science']
print(student)

student = ['Jack',32,'Computer Science',[2,4]]
print(student)
print(student[2])
print(student[-1])

my_list = ['m','a','n','i']
print("my-list =",my_list)
print("my-list =",my_list[1:3])
print("my-list =",my_list[1:])
print("my-list =",my_list[:3])
print("my-list =",my_list[:-3])


my_list.append('k')
print(my_list)

my_list.insert(5,'a')
print(my_list)

number = [1,4,5,5]
my_list.extend(number)
print(my_list)

my_list[2] = "python"
print(my_list)

my_list.remove(1)
print(my_list)

del my_list[1:3]
print(my_list)

a = len(my_list)
print(a)