import time

start_time = time.time()

def gcf(x,y):
    if x > y:
        x,y = y,x
    
    for i in range(x, 0, -1):
        if x % i == 0 and y % i == 0:
            return i

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
                    return v

print(gcf(137690, 298))
print(lcm(137690, 298))

stop_time = time.time()

print(stop_time - start_time)