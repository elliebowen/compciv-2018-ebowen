from datastubs import NUMBER_LIST


def reverse_numerical_order():
    return sorted(NUMBER_LIST, reverse=True)


def numerical_order():
    return sorted(NUMBER_LIST)

def as_absolute_value():
   anums = [abs(x) for x in NUMBER_LIST] 
   return sorted(anums) 


def as_inverse_number():
    inums = [(1/x) for x in NUMBER_LIST]
    return sorted(inums)
    