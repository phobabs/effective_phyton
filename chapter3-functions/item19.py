# Item 19: Never Unpack More Than Three Variables When Functions Return Multiple Values
def get_stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    return minimum, maximum

numbers = [100, 245, 30, 4, 5]
minimum, maximum = get_stats(numbers)
# print(f'Min: {minimum}, Max: {maximum}')

lengths = [63, 73, 72, 60, 67, 66, 71, 61, 72, 70]
def get_avg_ratio(numbers):
    average = sum(numbers) / len(numbers)
    scaled = [x / average for x in numbers]
    scaled.sort(reverse=True)
    return scaled

longest, *middle, shortest = get_avg_ratio(lengths)
# print(f'Longest:  {longest:>4.0%}')
# print(f'Shortest: {shortest:>4.0%}')
# print(f'middle: {middle[-1]:>4.0%}')

# Item 20: Prefer Raising Exceptions to Returning None
def careful_divide(a: float, b: float) -> float:
    """Divides a by b.
    Raises:
        ValueError: When the inputs cannot be divided.
    """
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputs') from e

x, y = 5, 2
try:
    result = careful_divide(x, y)
    print(result)
except ValueError as e:
    print(e)



