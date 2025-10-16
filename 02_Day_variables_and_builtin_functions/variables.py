#Day 2: 30 Days of python programming
firstname = 'Nafim'
lastname = 'Niloy'
fullname = 'Nafim Niloy'
country = 'Bangladesh'
city = 'Rajshahi'
age= 22
is_married = False
is_true = False
is_light_on = True
university, salary, haveJob = 'AIUB', 30000, True


#exercise level 2
print(type(fullname))
print(type(age))
print(type(is_true))
print(type(salary))
print(type(university))

print(len(firstname))
print(len(fullname))

num_one = 5
num_two = 4

total = num_one + num_two
print("Total: ",total)
diff = num_one - num_two
print("Difference: ",diff)
product = num_one * num_two
print("Product: ", product)
division = num_one / num_two
print("Divisiron: ",division)
remainder = num_one % num_two
print("Remainder: ", remainder)
floor_division = num_one // num_two
print("Floor division: ", floor_division)

# circle problem
r = 30
area_of_circle = 3.14*r**2
print(area_of_circle)
circum_of_circle = 2*3.14*r
print(circum_of_circle)
r = input('What is the radius of your cicle? ')
area_of_circle = 3.14*int(r)**2
print(area_of_circle)

#problem 13
usrFirstName = input('What is your firstname? ')
usrLastName = input ('What is your lastname? ')
usrCountry = input ('Input the country name: ')
usrAge = input ('Insert your age: ')
print('User name',usrLastName, usrLastName, 'Country:', usrCountry,'Age', usrAge)
