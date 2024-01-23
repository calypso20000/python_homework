# Given the salaries of three employees working at a department, 
# find the amount of money by which the salary of the highest-paid employee differs from the salary of the lowest-paid employee. 
# The input consists of three positive integers - the salaries of the employees. 
# Output a single number, the difference between the top and the bottom salaries

employee1=int(input("Eemployee 1 salary: "))
employee2=int(input("Eemployee 2 salary: "))
employee3=int(input("Eemployee 3 salary: "))
top=0
if employee3<employee1>employee2 and employee3<employee2:
    top=employee1-employee3
elif employee3<employee1>employee2 and employee2<employee3:
    top=employee1-employee2
elif employee3<employee2>employee1 and employee3<employee1:
    top=employee2-employee3
elif employee3<employee2>employee1 and employee1<employee3:
    top=employee2-employee1
elif employee2<employee3>employee1 and employee2<employee1:
    top=employee3-employee2
elif employee2<employee3>employee1 and employee1<employee2:
    top=employee3-employee1

print(top)