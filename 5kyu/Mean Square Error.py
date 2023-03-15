# Complete the function that

# accepts two integer arrays of equal length
# compares the value each member in one array to the corresponding member in the other
# squares the absolute value difference between those two values
# and returns the average of those squared absolute value difference between each member pair.
def solution(array_a, array_b):
    square_value = 0
    length_of_array = len(array_a)
    for i in range(length_of_array):
        difference = array_a[i] - array_b[i]
        square_value += difference**2
    return square_value/length_of_array
