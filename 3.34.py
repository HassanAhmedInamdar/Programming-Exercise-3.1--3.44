print("Hassan Ahmed Inamdar")
print("Roll No# 18B-080-CS,Sec-A")
print("Practice Problem 3.34")
def pay(hourly,hours):
    print("hourly wage: ",hourly,"hr")
    print("hourly pay: ","10$")
    if hours>=40:
        sal = 40*hourly
        Over_time = sal+ hourly*(hours - 40) *1.5
        return Over_time
    else:
        Not_Over_time = hours*hourly
        return Not_Over_time
salary = pay(10,35)
print(salary)
salary2 = pay(10,45)
print(salary2)
