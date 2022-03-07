def duget(l: int) -> 'list[int]':
    nums = []
    while len(nums) < 5:
        try:
            n = int(input("Addj meg egy egész számot: "))
        except ValueError:
            print("Nem (megfelelő) számot adtál meg.")
        else:
            nums.append(n)
    return nums


def pdat(dat: 'list[int]'):
    for y in dat:
        print(y, end='-')
    print('')


def rev(_input: 'list[int]') -> 'list[int]':
    _output = []
    for l in range(len(_input)-1, -1, -1):
        _output.append(_input[l])
    return _output
    

def getmin(_input: 'list[int]'):
    mp = 0  
    min = _input[0]
    for i in range(len(_input)):
        if _input[i] < min:
            min, mp = _input[i], i
    print(f"A legkisebb elem: {min}\nA helye: {mp+1}")


def getmax(_input: 'list[int]'):
    mp = 0  
    max = _input[0]
    for i in range(len(_input)):
        if _input[i] > max:
            max, mp = _input[i], i
    print(f"A legnagyobb elem: {max}\nA helye: {mp+1}")


def getavrg(_inout: 'list[int]'):
    avrg = sum(_inout) // len(_inout)
    print(avrg)
    # Unlocked new ability: list.index()
    try:
        avrp = _inout.index(avrg)
    except ValueError:
        avrg = min(_inout, key=lambda x:abs(x-avrg))
        avrp = _inout.index(avrg)
    print(f'A lista átlagához legközelebbi érték: {avrg}\nA helye: {avrp + 1}')
    


data = duget(5)
pdat(data)
pdat(rev(data))
getmin(data)
getmax(data)
getavrg(data)
