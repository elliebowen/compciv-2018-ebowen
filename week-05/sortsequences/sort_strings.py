from datastubs import STRING_LIST

'''
STRING_LIST = [
    '12',
    '100000',
    'Zero',
    'Dax',
    'danny',
    '199',
]
'''

def reverse_alpha():
    return sorted(STRING_LIST, reverse=True)


def alpha_case_insensitive():
    def foocap(a):
        for x in a:
            a.upper(x)
        return a
    return sorted(STRING_LIST, key = foocap, reverse = False)


def by_longest_length():
    def foolen(a):
        return len(a)
    return sorted(STRING_LIST, key = foolen, reverse = True)


def filter_and_sort_number_strings():
    """
    Filter the original list for strings that
    contain numbers. Then sort that list of number
    strings but as strings (i.e. alphaebtical order)
    Hint: string objects have a method named .isnumeric()
    https://www.geeksforgeeks.org/python-string-isnumeric-application/
    """
    # fill it out
    def foonums(a):
        strnums = []
        for x in a:
            if a.isnumeric():
                strnums.append(str(a(x)))
                return strnums
    return sorted(STRING_LIST, key = foonums)

def filter_and_sort_number_strings_as_numbers():
    """
    Filter the list for strings that contain numbers
    and then sort that list of strings in *numerical* order
    Hint: string objects have a method named .isnumeric()
    https://www.geeksforgeeks.org/python-string-isnumeric-application/
    Hint: Use the int() or float() method to convert a numeric string
       into an actual number
    """
    # fill it out
     def foonums(a):
        nums = []
        for x in a:
            if a.isnumeric():
                nums.append(int(a(x)))
                return nums
    return sorted(STRING_LIST, key = foonums)