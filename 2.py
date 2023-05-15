def do_something(x):
    answer = 0
    array = [x, x ** 0, x // x , x % (x - 4), [x]]
    for i in range(x):
        answer += array[i]
    return answer

x = int(input())

print(do_something(x))

try:
    do_something(x) # บรรทัดน􀁦ีหา้ มแก้
except ZeroDivisionError:
    print('Input value is less than length of the list')
else:
    print(do_something(x))