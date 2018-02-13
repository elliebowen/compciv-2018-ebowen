from datastubs import NUMBER_LIST


def reverse_numerical_order():
    return sorted(NUMBER_LIST, reverse=True)


def numerical_order():
    return sorted(NUMBER_LIST)

def as_absolute_value():
    def fooabs(a):
        return abs(x)
    return sorted(NUMBER_LIST, key = fooabs) 

def as_inverse_number():
    def fooinv(a)
    inums = [(1/x) for x in NUMBER_LIST]
    return sorted(inums)
    