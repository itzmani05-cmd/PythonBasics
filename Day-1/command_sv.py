import csv
with open("employee.csv",'w',newline = '') as file:
    w = csv.writer(file)
    w.writerow(['SNO','Name','Qualification'])
    no = int(input("Enter the no of Employee: "))
    for employee in range(no):
        sno = int(input("Enter Employee no: "))
        ename = input("Enter Employee name: ")
        eQual = input("Enter Qualification of the employee: ")
        w.writerow([sno, ename, eQual])

#if reading the file means
#with open('employee.txt','r')
#we use reader() for reading the file