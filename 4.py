def get_number(number):
    number_list = []
    
    for i in number:
        number_list.append(i)
    
    assert number_list[0] == "+"
    assert len(number_list) == 13
    assert type(number) == str

    if number_list[1] == "6" and number_list[2] == "6":
        print("Thailand")
    elif number_list[1] ==  "3" and number_list[2] == "4":
        print("Spain")
    else:
        print("Other country")

get_number(input(""))