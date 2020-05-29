def cumsum(x):
    total = 0
    for i in range(len(x)):
        total = x[i] + total
        x[i] = total
    return(total,x)
