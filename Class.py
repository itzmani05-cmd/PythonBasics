class bike:
    name = ""
    gear = 0

bike1 = bike()
bike1.name = "Fz"
bike1.gear
print(bike1.name )

class Employee:
    sno = 0
    name = ""
    position = ""

employee1 = Employee()
employee2 = Employee()

employee1.sno = 1
employee1.name = "Manikandan"
employee1.position = "Employer"

employee2.sno = 2
employee2.name = "Jeevan"
employee2.position = "Manager"

print(f'Employer ID: {employee1.sno}\nEmployer name: {employee1.name}\nEmployer Position: {employee1.position}\n')
print(f'Employer ID: {employee2.sno}\nEmployer name: {employee2.name}\nEmployer Position: {employee2.position}')


class Room:
    length = 10.3
    breadth = 12.0
    def calculate_area(self):
        print(self.length*self.breadth)
    
study_room = Room()
study_room.length = 42.5
study_room.calculate_area()

