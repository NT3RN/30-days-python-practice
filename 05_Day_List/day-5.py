#day 5
#Exercise level 1
arr = []
names =['Nafim' , 'Raj' , 'Rahat', 'Arnob', 'Jamal']
print(len(names))
print(names)
print('Frist index: {}, middle index: {}, last index:{}'.format(names[0], names[2], names[4]))
mixed_data_type = ['Nafim', '23', "5'8\"", 'Single', 'Bangladesh']
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'Oracle']
print(mixed_data_type)
print(it_companies)
print(len(it_companies))
it_companies[2] = 'IBM'
print(it_companies)
it_companies.append('Microsoft')
print(it_companies)
it_companies.insert(0, 'Amazon')
print(it_companies)
it_companies[0]=it_companies[0].upper()
print(it_companies)
result = '#; '.join(it_companies)
print(result)
does_exists = 'Google' in it_companies
print(does_exists)
it_companies.sort()
print(it_companies)
it_companies.sort(reverse=True)
print(it_companies)
first3comp = it_companies[::3]
print(first3comp)
last3comp=it_companies[-3::]
print(last3comp)
index = int(len(it_companies)/2)
print('index:', index)
print(len(it_companies))
it_companies.pop(index)
print(it_companies)
it_companies.pop()
print(it_companies)
it_companies.clear()
print(it_companies)
del it_companies
#print(it_companies) gives errors as it is not defined
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'Mongo']
full_stack = front_end + back_end
print(full_stack)
fs_copy = full_stack.copy()
print(fs_copy)
index = fs_copy.index('Redux')
print(index)
fs_copy.insert(index+1, 'Python')
fs_copy.insert(index+2, 'SQL')
print(fs_copy)

#exercise level 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort(reverse=True)
print(ages)
ages.sort()
print(ages)
max_age = max(ages)
min_age = min(ages)
avg = sum(ages)/len(ages)
print('Min age: ', min_age)
print('Max age: ', max_age)
print('average :', avg)
print('Range of ages: ', max_age - min_age)
index = len(ages)/2 -1
index = int(index)
print(index)
print('Median : ', (ages[index]+ages[index + 1])/2)
print(abs(min_age - avg))
print(abs(max_age - avg))