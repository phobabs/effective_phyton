# slicing

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print('Middle two:  ', a[3:5])
print('All but ends:', a[1:7])

#common Python trick for reversing a byte string is to slice the string with a stride of -1:
x = b'mongoose' 
y = x[::-1]
print(y) 
b'esoognom'
#This also works correctly for Unicode strings (see Item 3: “Know the Differences Between bytes and str”):
x = ''
y = x[::-1] 
print(y)


#Prefer Catch-All Unpacking Over Slicing

car_ages = [0, 9, 4, 8, 7, 20, 19, 1, 6, 15]
car_ages_descending = sorted(car_ages, reverse=True)
print(car_ages_descending)
oldest, second_oldest,*others = car_ages_descending
print(oldest, second_oldest, *others)


car_inventory = {
    'Downtown': ('Silver Shadow', 'Pinto', 'DMC'),
    'Airport': ('Skyline', 'Viper', 'Gremlin', 'Nova'),
}

# Unpacking the dictionary items into variables
((loc1, (best1, *rest1)),
 (loc2, (best2, *rest2))) = car_inventory.items()

print(loc1)

# loc1 will be 'Downtown', best1 will be 'Silver Shadow', and rest1 will be ['Pinto', 'DMC']
# loc2 will be 'Airport', best2 will be 'Skyline', and rest2 will be ['Viper', 'Gremlin', 'Nova']
print(f'Best at {loc1} is {best1}, {len(rest1)} others')
print(f'Best at {loc2} is {best2}, {len(rest2)} others')

    


#I define a function to process this voting data and
#save the rank of each animal name into a provided empty dictionary. In this case, the dictionary could be the data model that powers a UI element:
def populate_ranks(votes, ranks):
    names = list(votes.keys())
    names.sort(key=votes.get, reverse=True)
    for i, name in enumerate(names, 1):
        ranks[name] = i
 
 
 
 # LIST AND DCITIONARIES CHAPTER 2       
# slicing and unoacking
oldest = car_ages_descending[0]
second_oldest = car_ages_descending[1]
others = car_ages_descending[2:]
print(oldest, second_oldest, others)
# unpacking 
20, 19, [15, 9, 8, 7, 6, 4, 1, 0]

#  unpacking 
# starred expres- sion to achieve the same result as above
# without indexing or slicing:
oldest, second_oldest, *others = car_ages_descending
print(oldest, second_oldest, others)

20,19, [15, 9, 8, 7, 6, 4, 1, 0]

# A starred expression may appear in any position, 
# so you can get the benefits of catch-all unpacking anytime 
# you need to extract one slice:

oldest, *others, youngest = car_ages_descending
print(oldest, youngest, others)
20 ,0 ,[19, 15, 9, 8, 7, 6, 4, 1]

*others, second_youngest, youngest = car_ages_descending
print(youngest, second_youngest, others)
0 ,1, [20, 19, 15, 9, 8, 7, 6, 4]


car_inventory = {
    'Downtown': ('Silver Shadow', 'Pinto', 'DMC'),
    'Airport': ('Skyline', 'Viper', 'Gremlin', 'Nova'),
}
((loc1, (best1, *rest1)),
 (loc2, (best2, *rest2))) = car_inventory.items()

# another example where the starred expression 
# empty
short_list = [1, 2]
first, second, *rest = short_list
print(first, second, rest)



it = iter(range(1, 3))
first, second = it
print(f'{first} and {second}')


