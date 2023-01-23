"""
Feladat leírás:
Mindegyik alábbi feladathoz készítsünk saját függvényt.
A 2. feladattól kezdve a függvények bemenő paramétere a lista, visszatérési értékük pedig a kiíratandó teljes szöveges válasz a kérdésre.
1. Olvassunk be öt egész számot egy listába. Feltételezhetjük, hogy a felhasználó valóban csak egész számokat ad meg.
2. Írjuk ki a lista elemeit egy sorban, kötőjellel elválasztva, abban a sorrendben, ahogy azt a felhasználó megadta.
3. Írjuk ki a lista elemeit fordított sorrendben, egy sorban, kötőjellel elválasztva.
4. Írjuk ki, hányadik elem a legkisebb és mennyi az.
5. Írjuk ki, hányadik elem a legnagyobb és mennyi az.
6. Írjuk ki melyik elem áll a legközelebb a teljes lista átlagához és hogy az hányadik elem.
"""


def user_get(length: int) -> list:
    numbers = []
    while len(numbers) < 5:
        try:
            n = int(input("Adj meg egy egész számot: "))
        except ValueError:
            print("Nem (megfelelő) számot adtál meg.")
        else:
            numbers.append(n)
    return numbers


def data_print(data_list: list):
    for _data in data_list:
        print(_data, end='-')
    print('')


def reverse(input_data: list) -> list:
    _output = []
    for i, _ in enumerate(input_data):
        _output.append(input_data[i * -1])
    return _output


def getmin(input_data: list):
    max_point = 0
    smallest = input_data[0]
    for i in range(len(input_data)):
        if input_data[i] < smallest:
            smallest, max_point = input_data[i], i
    print(f"A legkisebb elem: {smallest}\nA helye: {max_point + 1}")


def getmax(input_data: list):
    max_point = 0
    _max = input_data[0]
    for i in range(len(input_data)):
        if input_data[i] > _max:
            _max, max_point = input_data[i], i
    print(f"A legnagyobb elem: {_max}\nA helye: {max_point + 1}")


def get_average(_inout: list):
    average = sum(_inout) // len(_inout)
    print(average)
    # Unlocked new ability: list.index()
    try:
        average_position = _inout.index(average)
    except ValueError:
        average = min(_inout, key=lambda x: abs(x - average))
        average_position = _inout.index(average)
    print(f'A lista átlagához legközelebbi érték: {average}\nA helye: {average_position + 1}')


data = user_get(5)
data_print(data)
data_print(reverse(data))
getmin(data)
getmax(data)
get_average(data)
