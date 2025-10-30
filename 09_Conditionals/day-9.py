#Day 9 Exercises 
#Level 1
age = input('Enter your age: ')
age = int(age)
if age >= 18:
    print('You are old enough to learn how to drive')
else:
    r_age = 18 - age
    print('you need {} more years before you can drive'.format(r_age))

myAge = 25
myAge = int(myAge)
yAge = input('Enter your age: ')
yAge = int(yAge)
if yAge > myAge:
    if yAge - myAge == 1:
        print('You are 1 year older than me')
    else:
        age = yAge - myAge
        print('You are {} years older than me'.format(age))
elif myAge > yAge:
    if myAge - yAge ==1:
        print('I am one year older than you')
    else:
        age = myAge - yAge
        print('I am {} years older than you'.format(age))
else:
    print('We are the same age')

#Exercise level 2
grade = input('Input grade: ')
grade = int(grade)
if grade>=80 and grade <=100:
    print('A')
elif grade>=70 and grade <=79:
    print('B')
elif grade>=60 and grade <=69:
    print('C')
elif grade>=50 and grade <=59:
    print('D')
elif grade>=0 and grade <=49:
    print('F')
else:
    print('Enter valid grade')

userFruit = input('Enter fruit name: ')
fruits = ['banana', 'orange', 'mango', 'lemon']
if userFruit in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(userFruit)
    print(fruits)

#Exercise level 3
#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
person={
    'first_name': 'Nafim',
    'last_name': 'Niloy',
    'age': 25,
    'country': 'Bangladesh',
    'is_marred': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
if "skills" in person:
    print(person['skills'])
if 'skills' in person:
    x = len(person['skills'])
    x=int(x/2)
    print(person['skills'][x])
#  * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
if 'JavaScript' in person['skills'] and 'React' in person['skills']:
    if 'Node' in person['skills'] and 'MongoDB' in person['skills']:
        print('He is a fulllstack developer')
    else:
        print('He is a frontend developer')
elif 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
    if 'React' in person['skills']:
        print('He is a fullstack developer')
    else:
        print('He is a backend developer')
else:
    print('Unknown title')