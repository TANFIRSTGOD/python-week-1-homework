def lcm(x,y):
    x_multiplyer = 1
    y_multiplyer = 1
    x_multiples = []
    y_multiples = []
    while True:
        x_multiples.append(x * x_multiplyer)
        x_multiplyer += 1
        y_multiples.append(y * y_multiplyer)
        y_multiplyer += 1
        for i in x_multiples:
            for v in y_multiples:
                if i == v:
                    return(v)

print(lcm(24,36))