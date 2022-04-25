def getscore(_num:int):
    """Visszad egy bejövő értéket
        és egy DU-által beadott számot tuple-ként."""
    try:
        _du = int(input("Adj meg egy számot (1-100): "))
    except:
        print("Nem számot adtál meg!")
        _du = 1
    finally:
        if _du > 100:
          print("Túl nagy számot adtál meg!")
          return int(_num), 100
        elif _du < 1:
            print("Túl kis számot adtál meg!")
            return int(_num), 1
        else:
            return int(_num), _du


def ellenor(_pnt:int):
    """Pontokka jegyekké alakít"""
    _hatr = [1, 40, 55, 70, 85]
    _jegy = [1, 2, 3, 4, 5]
    for i in range(len(_hatr)-1,0,-1):
        if _pnt >= _hatr[i]:
            return _jegy[i]
    return 1


def mma(_lst:tuple):
    """Min  Max Atlag"""

    min = max = _lst[0]
    sum = 0
    for j in _lst:
        sum += j
        if j < min:
            min = j
        elif j > max:
            max = j
    atlag = sum / len(_lst)
    print(f"legkisebb: {min}, legnagyobb: {max}, átlag: {atlag}")


scoreNum = [getscore(i) for i in range(1, 6)]
scoreNum = tuple(scoreNum)
gradeLst = [ellenor(i[1]) for i in scoreNum]
gradeLst = tuple(gradeLst)
mma(gradeLst)
"""for x in scoreNum:
    print("pont:",x[1])
    print("jegy:",ellenor(x[1]))"""
# print(ellenor(85))
