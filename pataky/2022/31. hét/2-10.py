from random import randint
secret = randint(1, 5)

tipp = 0
while tipp is not secret:
    try:
        du = input('Tippelj 1-5 kozott: ')
        if du == '':
            exit('Ures szoveget atdal meg.')
        tipp = int(du)
    except ValueError:
        print('Nem szamot adtal meg!')
    if tipp is not secret:
        print('nem talalt')

print('Eltalaltad a szamot.\nViszlat!')
