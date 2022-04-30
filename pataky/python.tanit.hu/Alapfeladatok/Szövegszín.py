"""
01-28 Szövegszín
Írd ki az alábbi szöveget úgy, hogy a színeket jelentő szavak az adott színnel legyenek kiírva.
A szövegbekérésnél pedig a felhasználó által begépelt szöveg sárga (yellow) legyen.
Minden más szöveg az alapértelmezett színben maradjon.
"""
from colorama import Fore

# Tájékoztatjuk a felhasználót, hogy hogyan működik a program
print('\nEbben a programban a kiírások színezési lehetőségeit mutatjuk be.\n')

print(f'Ezek különböző színek: {Fore.RED}red{Fore.RESET}, {Fore.GREEN}green{Fore.RESET}, {Fore.BLUE}blue{Fore.RESET},'
      f' {Fore.MAGENTA}magenta{Fore.RESET}...')
x = input(f'Gépelj be valami szöveget ({Fore.YELLOW}sárga{Fore.RESET} lesz): {Fore.YELLOW}')

print(f'{Fore.RESET}\nEz itt ismét alapértelmezett színű szöveg. Viszlát!\n')