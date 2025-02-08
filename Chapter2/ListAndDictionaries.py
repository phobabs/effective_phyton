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
tools.sort(key=lambda x: x.weight)
#print('\n' + 'sorted by name:', tools)

places = ['home', 'work', 'New York', 'Paris']
places.sort()
print('\n' + 'sorted by name:', places)
places.sort(key=lambda x: x.lower())
print('sorted by name ignoring case:', places)

# using multiple criteria to sort a list of tuples
power_tools = [
    ('drill', 4),
    ('circular saw', 5),        
    ('jackhammer', 40),
    ('sander', 4),
]       

power_tools.sort(key=lambda x: (x[1], x[0]))
print('\n' + 'sorted by power:', power_tools)