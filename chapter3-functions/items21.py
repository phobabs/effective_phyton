
#Item 21: Know How Closures Interact with Variable Scope

# The behavior of Python's closures 
# can be surprising if the values of variables change.

# The problem is that the values of variables in the closure's scope
# are looked up when the inner function is called.If the values of the
# closed-over variables change, the inner function will use the latest value
# from the enclosing scope.                             


        
def sort_priority(values, group):
    def helper(x):  
        if x in group:
            return (0, x)
        return (1, x)
    values.sort(key=helper)
    

values = [8, 3, 1, 12, 5, 4, 7, 6]                       
group = {2, 3, 5, 7}
sort_priority(values, group)
print(values)
