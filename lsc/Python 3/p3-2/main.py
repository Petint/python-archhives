def print_even():
    nums = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}

    for k in nums.keys():
        if k % 2 == 0:
            print(k, nums[k])


def on_to_ten():
    one_to_ten = dict()
    for kay in range(1, 11):
        one_to_ten[kay] = kay ** 2
    print(one_to_ten)


def multiple():
    my_dict = {'data1': 1, 'data2': 2, 'data3': 3, 'data4': 4, 'data5': 5}
    result = 1
    for ky in my_dict.keys():
        result *= my_dict[ky]
    return result


def min_max():
    dingus = {"x": 535, "y": 66, "z": 4837}
    print(max(dingus.values()))
    print(min(dingus.values()))


def mixer():
    dct = {'1': ['a', 'b'], '2': ['c', 'd']}
    a, b = dct.values()
    for i in a:
        for y in b:
            print(i + y)


if __name__ == '__main__':
    import people
    print_even()
    on_to_ten()
    print(multiple())
    min_max()
    mixer()
    person = people.People(input("Add meg a nevét: "), int(input('Add meg a korát: ')),
                           input('Add meg a nemét: '), input('Add meg a munkáját: '))
    person.gdata()
    print(people.humans)
