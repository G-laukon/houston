def birthday_paradox(samples):
    birthday_co = 0
    import random
    for i in range (samples):
        team = []
        for i in range(23):
            team.append(random.randint(1,365))
        if has_duplicates(team) == True:
            birthday_co += 1       
    return birthday_co/samples
    

def has_duplicates(t):   
    for x in t:
        t_copy = t + []
        t_copy.remove(x)
        for y in t_copy :
            if x == y:
                return True
