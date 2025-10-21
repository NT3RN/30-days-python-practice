#Exercise: Level 1
empty_tuple = ()
brothers = ('Nafim', 'Niloy', 'John')
sisters = ('Putul', 'Puja', 'Mala')
siblings = brothers + sisters
print(siblings)
print('Total siblings: ', len(siblings))
family_members = list(siblings)
family_members[0] = 'Dad'
family_members[1] = 'Mom'
print(family_members)
family_members = tuple(family_members)
print(family_members)

#Exercise Level 2
del family_members
fruits = ('apple', 'banana', 'mango')
vegi = ('tomato', 'cabage', 'cucumber')
product = ('bread', 'milk', 'noodles')
food_stuff_tp = fruits + vegi + product
print(food_stuff_tp)
sliced_food = food_stuff_tp[0:5] + food_stuff_tp[6:]
print(sliced_food)
del food_stuff_tp
#print(food_stuff_tp) tuple doesnt exists after delete

exists = 'banana' in sliced_food
print(exists)