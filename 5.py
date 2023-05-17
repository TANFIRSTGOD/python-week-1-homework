def enum(items):
    assert type(items) == list
    return_value = []
    position = 1
    for i in items:
        return_value.append((position, i))
        position += 1

    print(return_value)

enum(['a', 2, None])
