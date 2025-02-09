# slicing

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print('Middle two:  ', a[3:5])  # Slicing to get elements from index 3 to 4
print('All but ends:', a[1:7])  # Slicing to get elements from index 1 to 6

# common Python trick for reversing a byte string is to slice the string with a stride of -1:
x = b'mongoose' 
y = x[::-1]  # Reversing the byte string
print(y) 
b'esoognom'
# This also works correctly for Unicode strings (see Item 3: “Know the Differences Between bytes and str”):
x = ''
y = x[::-1] 
print(y)

# Slicing with a stride
x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(x[2::2])  # Slicing to get every second element starting from index 2
print(x[2:2:-2]) # Slicing to get every second element starting from index 2 in reverse order
# Prefer Catch-All Unpacking Over Slicing

# Item 13: Prefer Catch-All Unpacking Over Slicing
car_ages = [0, 9, 4, 8, 7, 20, 19, 1, 6, 15]
car_ages_descending = sorted(car_ages, reverse=True)
print(car_ages_descending)
oldest, second_oldest, *others = car_ages_descending
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
#print(first, second, rest)



it = iter(range(1, 3))
first, second = it
print(f'{first} and {second}')

# unpacking iterator

def generate_csv():
    yield ('Date', 'Make', 'Model', 'Year', 'Price')
    yield ('2020-11-01', 'Toyota', 'Corolla', 2016, 24000)
    yield ('2020-11-02', 'Ford', 'Fusion', 2018, 33000)
    yield ('2020-11-03', 'Chevrolet', 'Volt', 2014, 14000)

all_csv_rows = list(generate_csv())
header, *rows = all_csv_rows[0], all_csv_rows[1:]
print(all_csv_rows)
#print('CSV Header:', header)
#print('CSV Row:', rows)

# Item 14: Sort by Complex Criteria Using the key Parameter
class Animal:
    def __init__(self, name, weight):
        self.name = name  # Assign the name parameter to the instance variable
        self.weight = weight  # Assign the weight parameter to the instance variable

    def __str__(self):
        return f'{self.name} weighs {self.weight} kg'  # Return a string representation of the object

# Example usage
elephant = Animal('Elephant', 1200)
print(elephant)  # Output: Elephant weighs 1200 kg


drill = (4, 'drill')
sander = (4, 'sander')
assert drill[0] == sander[0]  # Same weight
assert drill[1] < sander[1]   # Alphabetically less
assert drill < sander         # Thus, drill comes first

power_tools = [
    (4, 'drill'),   # 4 kg          
    (5, 'circular saw'),  # 5 kg
    (40, 'jackhammer'),  # 40 kg
    (4, 'sander'),  # 4 kg
]

power_tools.sort(key=lambda x: (x[1], x[0]))  # Sort by name first, then by weight
print(power_tools)  # Output: [(5, 'circular saw'), (4, 'drill'), (40, 'jackhammer'), (4, 'sander')]
# The power tools are sorted by name first and then by weight
# The lambda function is used to specify the sorting criteria 

power_tools.sort(key=lambda x: (-x[0], x[1]))  # Sort by weight in descending order, then by name
print(power_tools)  # Output: [(40, 'jackhammer'), (5, 'circular saw'), (4, 'drill'), (4, 'sander')]
# The power tools are sorted by weight in descending order and then by name in ascending order      

# Item 15: Be Cautious When Relying on dict Insertion Ordering

baby_names = {
    'cat': 'kitten',
    'dog': 'puppy',
}

print(baby_names)  # Output: {'cat': 'kitten', 'dog': 'puppy'}
# The order of the dictionary items is preserved but for python 3.5 the order changes (it will be sorted by keys) 
votes = {
    'otter': 1281,              
    'polar bear': 587,
    'fox': 863,
}                   

print(votes)  # Output: {'otter': 1281, 'polar bear': 587, 'fox': 863}  # The order of the dictionary items is preserved

# The populate_ranks function processes the voting data and saves the rank of each animal name into a provided empty dictionary 

def populate_ranks(votes, ranks):
    names = list(votes.keys())
    names.sort(key=votes.get, reverse=True)
    for i, name in enumerate(names, 1):
        ranks[name] = i
        return ranks

ranks = {}
populate_ranks(votes, ranks)
print(ranks)  # Output: {'otter': 1}    # The otter is the only animal in the ranks dictionary

# Item 16: Prefer get Over in and KeyError to Handle Missing Dictionary Keys
counters = {             # A dictionary of animal names and their counts        
    'otter': 1,
    'polar bear': 2,
    'fox': 3,
}

# The increment function increments the count of a given animal name in the counters
def increment(counters, name):
    try:
        counters[name] += 1
    except KeyError:
        counters[name] = 1