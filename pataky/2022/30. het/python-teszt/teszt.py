def file_import(path: str):
    """Data import from specified file."""
    _feladatok_file = open(path, 'rt', encoding='utf-8')
    _feladatok_raw = _feladatok_file.read().splitlines()
    _feladatok_file.close()
    _feladatok = [f.split(';') for f in _feladatok_raw]
    del _feladatok_file, _feladatok_raw, _feladatok[0]
    return _feladatok


def ask(question: 'list[str]'):
    answer = question[-1]
    print(f"""
Az alabbi muveletnek mi az eredmenye?
{question[0]}
1) {question[1]}
2) {question[2]}
3) {question[3]}
    """)
    dear_user = input('Melyik a helyes valasz (1, 2, 3): ')
    if dear_user not in ['1', '2', '3']:
        print("Nincs ilyen lehetoseg!")
        _, answer = ask(question)
    return dear_user == answer, answer


feladatok = file_import('feladatok.txt')
print("Python muveletek - TESZT")
for feladat in feladatok:
    answer_bool, answer_str = ask(feladat)
    print('Helyes valasz') if answer_bool else print(f'Helytelen valasz. A helyes valasz: {answer_str}')
