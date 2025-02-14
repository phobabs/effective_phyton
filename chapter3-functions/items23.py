c = 0
list_x = [1,3,4,5]
for i in list_x:
    #print(c,i)
    c = c + 1
    
    
def remainder(number, divisor):
    return number % divisor
assert remainder(20, 7) == 6   

#print(remainder(20, 7))

#print(remainder(20, divisor=7)) # 6
#print(remainder(number=20, 7)) # SyntaxError: positional argument follows keyword argument

#item 23: provide optional behavior with keyword arguments

my_kwrgs = {'number': 20, 'divisor': 7}

# passing a dictionary contents to call a function like remainder,
# you can do this by using the ** operator

assert remainder(**my_kwrgs) == 6
#print(remainder(**my_kwrgs)) # 6

# The ** operator allows you to provide keyword arguments that aren't present in the dictionary my_kwrgs    
my_kwrgs = {'number': 20}   
#assert remainder(**my_kwrgs) == 0
#print(remainder(**my_kwrgs)) # 0

#you can also use the ** operator multiple times 
#if you know that the dictionaries don’t contain overlapping keys:
my_kwargs = {
    'number': 20,
}
other_kwargs = {
    'divisor': 7,
}
assert remainder(**my_kwargs, **other_kwargs) == 6

#use the **kwargs catch-all parameter to collect those 
#arguments into a dict that you can then process

def print_parameters(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} = {value}')
print_parameters(alpha=1.5, beta=9, gamma=4)    
#alpha = 1.5        
#beta = 9
#gamma = 4



