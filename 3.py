def get_number(num):
    num_list = []
    for i in num:
        num_list.append(i)
    if num_list[0] != '+':
        raise LookupError('ไม่มี country code')
    elif len(num_list) != 13 and num_list[0] != '+':
        raise IndexError('ความยาวไม่ตรงกับท􀁣ีกำหนด')
    elif type(num) != str:
        raise TypeError('บอร์ท􀁣ีใส่เข้ามาไม่ใส่ String')
    elif num_list[0] == '+' and len(num_list) != 13:
        raise ValueError('ไม่ตรงรูปแบบท􀁣ีกำหนด')

    if num_list[1] == "6" and num_list[2] == "6":
        print("Thailand")
    elif num_list[1] == "3" and num_list[2] == "4":
        print("Spain")
    else:
        print("Other country")

get_number(input())