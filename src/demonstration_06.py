"""
Challenge #6:

Return the number (count) of vowels in the given string.

We will consider `a, e, i, o, u as vowels for this challenge (but not y).

The input string will only consist of lower case letters and/or spaces.
"""
def get_count(input_str):
    # Your code here
    # loop over each character in the string
    amount = 0 
    for char in input_str.lower_str:
        if char in 'aeiou':
            amout += 1

    return amount

sample_str = 'auidah kEoLmno' # 6 vowels

print(get_count(sample_str))