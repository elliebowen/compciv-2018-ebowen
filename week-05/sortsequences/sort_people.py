from datastubs import PEOPLE_LIST

def longest_name():
    def foolen(p):
        return len(p['name'])
    return sorted(PEOPLE_LIST, key=foolen, reverse=True)

def youngest():
    def fooage(a):
        return a['age']
    return sorted(PEOPLE_LIST, key = fooage, reverse = False)

def oldest():
    def fooage(a):
        return a['age']
    return sorted(PEOPLE_LIST, key = fooage, reverse = True)

def name_reverse_alpha():
    def fooalp(a):
        return a['name']
    return sorted(PEOPLE_LIST, key = fooalp, reverse = True)

def country_then_age():
    def fooca(a):
        country = a['country']
        age = a['age']
        return (country, age)
    sorted(PEOPLE_LIST, key = fooca, reverse = False)