#Exercise level 1
def add_two_num (num1, num2):
    total = num1 + num2
    return total

print(add_two_num(3,5))

def areaCircle(r):
    return 3.14 *r **2
print(areaCircle(4))

def addAll(*nums):
    total = 0
    for num in nums:
        total += num
    return total
print(addAll(5,8,23))
print(addAll(5,5))

def C2F(c):
    print((c*9/5)+32,'Degree Farenheit')
C2F(32)