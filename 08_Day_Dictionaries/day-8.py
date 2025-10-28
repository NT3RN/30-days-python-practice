#Exercise Day 8
dog = {}

dog['name']='Bush'
dog['color']= 'Black'
dog['legs'] = 4
dog['age'] = 5
dog['breed'] = 'Unknown'
print(dog)

student = {
    'first_name': 'Nafim',
    'last_name': 'Niloy',
    'gender': 'Male',
    'age': 25,
    'skills' : ['NodeJS','React', 'Python', 'JS'],
    'address':{
        'city': 'Dhaka',
        'country':'Bangladesh'
    }
}
print(student)
print(student['address'])
print('City: ',student['address']['city'])
print('Access skills list at 0 index: ',student['skills'][0])
print(type(student['skills']))
print('Length of student dictionaries: ',len(student))
print(student.keys())
print(student.items())
student['skills'].append('HTML')
print(student['skills'])
del student['gender']
print(student)
del dog