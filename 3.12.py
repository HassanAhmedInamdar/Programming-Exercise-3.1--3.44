print("Hassan Ahmed Inamdar")
print("Roll No# 18B-080-CS,Sec-A")
print("Practice Problem 3.12")
def negative(number):
    neg_num= []
    for i in number:
        if i <0:
            neg_num.append(i)
    return neg_num
x = negative([1,3,-9,-10,-6,-8])
print(*x, sep="\n")
