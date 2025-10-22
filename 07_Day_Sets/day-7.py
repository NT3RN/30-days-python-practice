# Exercise level 1
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(len(it_companies))
it_companies.add('Twitter')
print(it_companies)
it_companies.update(['BrainStation', 'Alibaba'])
print(it_companies)
it_companies.remove('IBM')
print(it_companies)

#Exercise level 2
print(A.union(B))
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(B.isdisjoint(A))
print(B.union(A))
print(A.symmetric_difference(B))
del it_companies, A, B

#Exercise level 3
ageset = set(age)
print(ageset)
print('Age: ', age)
print('Age set: ', ageset)
sentense = 'I am a teacher and I love to inspire and teach people'
print(len(sentense.split(' ')))