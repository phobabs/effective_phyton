a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_squares = [x**2 for x in a if x % 2 == 0]
print(even_squares)

alt = map(lambda x: x**2, filter(lambda x: x % 2 == 0, a))
assert even_squares == list(alt)    
print(even_squares) # [4, 16, 36, 64, 100]

c =list(filter(lambda x: x % 2 == 0, a) )# <filter object at 0x7f8b1c1b3d90> 
print(c)
map(lambda x: x**2, filter(lambda x: x % 2 == 0, a)) # <map object at 0x7f8b1c1b3d90>
list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, a))) # [4, 16, 36, 64, 100]  

# dictionary and set comprehensions
even_squares_dict = {x: x**2 for x in a if x % 2 == 0}
threes_cubed_set = {x**3 for x in a if x % 3 == 0} 