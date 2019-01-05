print("Hassan Ahmed Inamdar")
print("Roll No# 18B-080-CS,Sec-A")
print("Practice Problem 3.37")
def point(x1,y1,x2,y2):
    import math
    d = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
    if x2==0:
        print("The slope is infinity"+' '+"and Distance is", d)
    else:
        s = ((y2-y1) / (x2-x1))
        print("The Slope is",s,"And Distance is",d)
co_ordinate = point(4,3,0,1)
co_ordinate = point(6,7,8,9)
