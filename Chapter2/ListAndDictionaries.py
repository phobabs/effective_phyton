def generate_csv():
    yield ('Date', 'Make', 'Model', 'Year', 'Price')
    yield ('2020-11-01', 'Toyota', 'Corolla', 2016, 24000)
    yield ('2020-11-02', 'Ford', 'Fusion', 2018, 33000)
    yield ('2020-11-03', 'Chevrolet', 'Volt', 2014, 14000)

all_csv_rows = list(generate_csv())
header, *rows = all_csv_rows[0], all_csv_rows[1:]
#print(all_csv_rows)
#print('CSV Header:', header)
#print('CSV Row:', rows) 

# sort the list of tuples by the price
#rows.sort(key=lambda row: row[-1])
#print(rows)

it = list(generate_csv())
header, *rows = it
#print('csv header :' , header)
#print('csv rows :', len(rows))


# Define the Tool class
class Tool:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f'Tool(name={self.name}, weight={self.weight})'

# sort by complex criteria using the key parameter
tools = [
    Tool('level', 3.5),
    Tool('hammer', 1.25),
    Tool('screwdriver', 0.5),
    Tool('chisel', 0.25)
]

#print(('unsorted:', repr(tools)))
tools.sort(key=lambda x: x.weight)  # Sort tools by weight
#print('\n' + 'sorted by name:', tools)

places = ['home', 'work', 'New York', 'Paris']
places.sort()  # Sort places alphabetically
print('\n' + 'sorted by name:', places)
places.sort(key=lambda x: x.lower())  # Sort places alphabetically ignoring case
print('sorted by name ignoring case:', places)

# using multiple criteria to sort a list of tuples
power_tools = [
    ('drill', 4),
    ('circular saw', 5),        
    ('jackhammer', 40),
    ('sander', 4),
]       

power_tools.sort(key=lambda x: (x[1], x[0]))  # Sort by weight first, then by name
print('\n' + 'sorted by power:', power_tools)


    # For example, say that I’m writing a program to show the results
    # of a contest for the cutest baby animal. Here, 
    # I start with a dictionary containing the total vote count for each one:
votes = {
    'otter': 1281,
    'polar bear': 587,
    'fox': 863, 
    }
# I define a function to process this voting data 
# and save the rank of each animal name into a provided empty dictionary. 
# The rank is the position of the animal in the sorted list of names.
    
def populate_ranks(votes, ranks):
    names = list(votes.keys())
    names.sort(key=votes.get, reverse=True)
    for i, name in enumerate(names, 1):
        ranks[name] = i
        
# I also need a function that will tell me which animal won the contest

def get_winner(ranks):
    return next(iter(ranks))

ranks = {}
populate_ranks(votes, ranks)
print(ranks)
winner = get_winner(ranks)
print(winner)

# Item 16: Prefer get Over in and KeyError to Handle Missing Dictionary Keys
