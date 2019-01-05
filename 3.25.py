print("Hassan Ahmed Inamdar")
print("Roll No# 18B-080-CS,Sec-A")
print("Practice Problem 3.25")
user_list = []
for x in range (3):
    a = input("Student Name :")
    user_list.append(a)

for x in range (3):
    if user_list [x] [:1] in ('a','A','b','B','c','C','d','D','e','E','f','F','g','G','h','H','i','I','j','J','k','K','l','L','m','M','n','N','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w','W','x','X','y','Y','z','Z'):
        print(user_list[x])
