print("Hassan Ahmed Inamdar")
print("Roll No# 18B-080-CS,Sec-A")
print("Practice Problem 3.13")

# Average of Two No.
def average(x,y):
    average.py = (x+y)/2
    return average.py
a = int(input("enter a no.:"))
b = int(input("enter a no.:"))
print("The Average of Two Entered No. is :" ,average(a,b))
help(average)

# List of Negative No.
def negative(number):
    neg_num = []
    for i in number:
        if i <0:
            print(i)
user_list =[]
for x in range (4):
    c = int(input("enter no." + str (x+1) + ":"))
    user_list.append(c)
negative(user_list)
help(negative)
