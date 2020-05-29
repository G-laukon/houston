def nested_sum(x):
    total = 0
    for y in x:
        total = total + sum(y)
    return total
