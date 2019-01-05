print("Hassan Ahmed Inamdar")
print("Roll No# 18B-080-CS,Sec-A")
print("Practice Problem 3.39")
def collision(x1,y1,r1,x2,y2,r2):
    import math
    center_dis = ((x2-x1)**2+(y2-y1)**2)
    if center_dis <= (r1+r2)**2:
        return True
    else:
        return False
x = collision(0,0,1.4,2,2,1.4)
print(x)
x2 = collision(0,0,3,0,5,3)
print(x2)
