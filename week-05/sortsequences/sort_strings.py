from datastubs import STRING_LIST

def reverse_alpha():
    return sorted(STRING_LIST, reverse=True)


def alpha_case_insensitive():
    def foocap(a):
        for x in a:
            return a.upper()
    return sorted(STRING_LIST, key = foocap)



def by_longest_length():
    def foolen(a): 
        return len(a)
    return sorted(STRING_LIST, key = foolen, reverse=True)



def filter_and_sort_number_strings():
    snums = [] 
    for x in STRING_LIST:
        if x.isnumeric():
            snums.append(x)    
    return sorted(snums)



def filter_and_sort_number_strings_as_numbers():
    snums = [] 
    for x in STRING_LIST:
        if x.isnumeric():
            snums.append(x) 
    def foo(x):
        return int(x)  
    return sorted(snums, key = foo)