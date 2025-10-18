#Day 4 task 
sentense1 = 'Thirty '+ 'Days '+'Of ' + 'Python'
print(sentense1)

sentense2 = 'Coding '+ 'For ' + 'All'
print(sentense2)

company = sentense2
print(company)

print(len(company))

print(company.upper(), company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company.strip('Coding'))
print(company.replace('Coding', 'Python'))
print(company.split())

sentense3 = "Facebook, Google, Microsoft, Apple, Amazon"
print(sentense3.split(','))

print(company.find('C'))
print(company.find('F'))
print(company.rfind('l'))

sentense4 = 'You cannot end a sentense with because because is a conjuction'
print(sentense4.find('because'))
print(sentense4.rfind('because'))

sentense5 = 'You cannot end a sentense with because because because is a conjuction'
print(sentense5.replace('because ',''))

print(company.startswith('Coding'))
print(company.endswith('coding'))

coding = ' Coding For All '
print(coding.strip())

challenge = '30DaysOfPython'
print(challenge.isidentifier())
challenge = 'thirty_days_of_python'
print(challenge.isidentifier())

pythonLibraries = ['Django', 'Flask', 'Bottle', 'Pyramid']
result = '# '.join(pythonLibraries)
print(result)

block = 'I am enjoying this challenge.\nI just wonder what is next'
print(block)

tabEscape ='Name\tAge\tCountry\tCity\nNafim\t23\tBangladesh\tDhaka'
print(tabEscape.expandtabs(10))

radius = 10
area = 3.14 * radius ** 2
print('The area of a circle with radius {} is {} meters square'.format(radius, area))

a = 8
b = 6

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))