"""
Challenge #1:

Write a function that retrieves the last n elements from a list.

Examples:
- last([1, 2, 3, 4, 5], 1) ➞ [5]
- last([4, 3, 9, 9, 7, 6], 3) ➞ [9, 7, 6]
- last([1, 2, 3, 4, 5], 7) ➞ "invalid"
- last([1, 2, 3, 4, 5], 0) ➞ []

Notes:
- Return "invalid" if n exceeds the length of the list.
- Return an empty list if n == 0.
"""


def last(a, n):
    # Your code here
    if n > len(a):
        return "invalid"
    elif n < 1:
        return []

    # Print the last N element?
    return a[ -n : ]


my_list = [4, 3, 9, 9, 7, 6]

print (last(my_list, 5))

# accessing one individual element
print(my_list[4])

# access the last element in the list 
print(my_list[-1])


# Getting Subarrays
# get the first 3 element 
print(my_list[0:3])
print(my_list[1:5])
print(my_list[:3])
print(my_list[0:])

# create a list
print(my_list[:])

