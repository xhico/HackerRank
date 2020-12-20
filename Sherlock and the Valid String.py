from collections import Counter


# Complete the isValid function below.
def isValid(s):
    # Go over string and count how many times string occured
    char_dict = Counter(s)

    # initiate largest and smallest count with last char
    min_count = char_dict[s[-1]]
    max_count = char_dict[s[-1]]

    count_dict = {}
    for char, value in char_dict.items():
        if value in count_dict:
            count_dict[value] += 1
        else:
            count_dict[value] = 1
        
        # also update max and min count
        if value < min_count:
            min_count = value
        if value > max_count:
            max_count = value

    # final test
    if len(count_dict) == 1:
        return 'YES'
    elif len(count_dict) == 2:
        if count_dict[max_count] == 1 and max_count - min_count == 1:
            return 'YES'
        elif count_dict[min_count] == 1 and min_count == 1:
            return 'YES'
    return 'NO'


print(isValid("aabbcd"))
print(isValid("aabbccddeefghi"))
print(isValid("abcdefghhgfedecba"))
print(isValid("abbccc"))
"""
NO
NO
YES
NO
"""
