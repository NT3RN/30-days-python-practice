# Day 3 exercises 
age =23
print(type(age), age)
height=5.8
print(type(height))

b=input('Enter base: ')
h=input('Enter height: ')
area = .5*int(b)*int(h)
print(area)

a = input ('Enter side a: ')
b = input ('Enter side b: ')
c= input ('Enter side c: ')

perimeter = int(a)+int(b)+int(c)
print(perimeter)

length = input('Enter length: ')
width = input('Enter width: ')
premiter = 2*(float(length)+float(width))
area = float(length)*float(width)
print('Area: ', area, 'Premiter: ', premiter)

print(len('python'))
print(len('dragon'))

help('keywords')

print('jargon' in 'I hope this course is not full of jargon')

print(not 'on' in 'dragon' and 'on' in 'python')

l = len('python')
l=float(l)
print(type(l))
l=str(l)
print(type(l))

print(7//3 == int(2.7))
i='9.8'
i=float(i)
i=int(i)
print(type(i))
print('10' == 10)
print(i==10)
print(i)

hours = input('Enter hours : ')
hours = int(hours)
rate = input('Enter per hour rate: ')
rate = int(rate)
weeklyEarning = rate * hours
print('Your weekly earning is', weeklyEarning, 'BDT')

for i in range (1,6):
    j = i*i
    k =j*i
    print(i, 1 , j, k)