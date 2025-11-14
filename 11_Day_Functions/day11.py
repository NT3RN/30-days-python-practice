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

def checkSeason(month):
    season = {
        'January': 'Winter',
        'February':'Winter',
        'March': 'Spring',
        'April': 'Spring',
        'May': 'Spring',
        'June': 'Summer',
        'July': 'Summer',
        'August': 'Summer',
        'September': 'Fall',
        'October': 'Fall',
        'November': 'Fall',
        'December': 'Winter'
    }
    if month in season:
        print('Season is:', season[month])
    else:
        print('Type valid month name')
checkSeason('August')

def solve_quadratic_eqn(a, b, c):
    dis = (b**2 - 4*a*c)**.5
    x1 = (-b + dis)/ (2*a)
    x2 = (-b - dis)/ (2*a)
    return x1, x2

def print_list(list):
    for l in list:
        print(l)

def reverse_list(list):
    r_list = []
    for l in range(len(list)):  
        r_list.append(list.pop())
    return r_list

l = [12,3,4,5]
print(reverse_list(l))

#Level 3
def is_prime(num):
    if num <=1: return False
    else:
        for n in range (2,num):
            if num%n == 0: return False
            else: return True

print(is_prime(6))

def is_unique(items):
    return len(items)==len(set(items))

items = [222,453,53,3,3,'a']
print(is_unique(items))

def is_same(types):
    type1 = set()
    for t in types:
        type1.add(type(t))
    if len(type1) == 1:
        return True
    else:
        return False

print(is_same(items))

