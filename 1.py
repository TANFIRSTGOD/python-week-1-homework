def do_something(x):
    answer = 0
    array = [x, x ** 0, x // x , x % (x - 4), [x]]
    for i in range(x):
        answer += array[i]
    return answer

x = int(input())

try:
    do_something(x) # บรรทัดน􀁦ีหา้ มแก้
except ZeroDivisionError:
    # เกิดข􀁦ึนเม􀁣ือ x = 0
    print('Input value is more than length of the list')