name=input()
age=int(input())
weight=int(input())
height=int(input())
hourly_salary=int(input())
worked_hours=int(input())
current_year=2026


birth_year=current_year - age
bmi = weight/ (height * height)
total_salary = hourly_salary * worked_hours
 
print(name)
print(age)
print(birth_year)
print(bmi)
print(total_salary)

