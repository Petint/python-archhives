"""
Olvassunk be egy szöveget és írjuk ki, hogy van-e benne kis "a"-betű.
"""
print('A bekért szövegből megállapítjuk, hogy van-e benne kis \'a\' betű.')
text = input('adj meg egy szöveget: ')
if text.count('a'):
    print('A szövegben van kis "a" betű.')
else:
    print('A szövegben nincs kis "a" betű.')
