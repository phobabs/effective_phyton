

matrix = [
          [1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]
          ]
flat = [x for row in matrix for x in row]
print(flat) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# same result ina traditional way
flat = []
for row in matrix:
    for x in row:
        flat.append(x)
        
print(flat) # [1, 2, 3, 4, 5, 6, 7, 8, 9]        
