def pyramid():
    bricks = int(input("enter the number of bricks: "))
    height = 0

    while bricks > 0:
        if bricks >= height + 1:
            bricks -= height + 1
            height += 1
        else:
            break

    res = f"The height of the pyramid {height}, and we have {bricks} bricks left."
    print(res)


def chi9gu5():
    """De Morgan identity"""
    p = True
    q = False
    print(not(p and q) == (not p or not q))
    print(not (p or q) == (not p and not q))


"""
BinOps:
and
or
is
not
==
!=
<<
<<=
>>
>>=
=, +=, -=, *=, /=
&
|
"""


def income_calc():
    age_income = dict(Mari=[31, 21800], Joseph=[56, 450000], Masha=[22, 745740], Vadim=[32, 636894], Marci=[16, 0],
                      Bill=[36, 19525])
    youngest = 1000000000
    youngest_name = ''
    maz_inmok = -1
    mozt_inkommen = ''

    key_list = list(age_income.keys())
    vaule_list = list(age_income.values())

    for i in vaule_list:
        if i[0] < youngest:
            youngest = i[0]
            youngest_name = key_list[vaule_list.index(i)]
        if i[1] > maz_inmok:
            maz_inmok = i[1]
            mozt_inkommen = key_list[vaule_list.index(i)]
    print(youngest_name, 'Is rhe zungest')
    print(mozt_inkommen)
    ages = [vaule_list[i][0] for i in range(vaule_list.__len__())]
    print(sum(ages) / len(ages))


if __name__ == '__main__':
    pyramid()
    chi9gu5()
    income_calc()
