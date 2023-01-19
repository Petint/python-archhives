"""
Teszteljük a felhasználó python tudását. A mellékelt utf-8 kódolású text fájlból véletlenszerűen olvassuk be az egyik sort, ügyelve arra, hogy a fájlban van fejléc sor is, azt nem választhatjuk!
A fájl soraiban pontosvesszővel elválasztva vannak egymás után:
művelet;1. opció;2. opció;3. opció;a helyes megoldás száma
Írjuk ki a kozolra a mintának megfelelően a műveletet, majd kérdezzünk rá, hogy a felhasználó szerint melyik válasz a helyes a három közül, és írjuk is ki a három opciót.
Olvassuk be a felhasználó válaszát, azaz a tippelt helyes válasz számát. Ha nem 1, 2 vagy 3 választ ad, akkor írjuk ki, hogy nincs ilyen választási lehetőség.
Ha megadta az 1, 2 vagy 3-t mint választ, akkor írjuk ki, hogy helyes vagy helytelen a válasz. Helytelen válasz esetén írjuk ki azt is, hogy mi lett vona a helyes.
"""


def get_questions():
    with open('python-teszt.txt', 'rt', encoding='UTF-8') as question_file:
        _ = question_file.readline()
        questions = [question for question in question_file]
        questions = [question.replace('\n', '') for question in questions]
        return [question.split(';') for question in questions]


def main():
    questions = get_questions()
    print(questions)


if __name__ == '__main__':
    main()
