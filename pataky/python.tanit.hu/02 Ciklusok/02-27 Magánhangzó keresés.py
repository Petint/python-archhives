"""
Kérjen be egy szöveget a felhasználótól, döntse el, hogy van-e benne magánhangzó, ha igen, akkor hol van az első!
Kis és nagybetűk esetén is jól működjön a program.
"""
print("Megnéélzük egy szövegben hogy van-e benne magánhangzó.")
vowels = 'aáeéiíoóöőuúüű'
dear_user = input("Adj meg egy szöveget: ").lower()
for index, letter in enumerate(dear_user):
    if letter in vowels:
        break
if index-1 == len(dear_user):
    print("Nincs benne magánhangzó.")
else:
    print('Van benne magánhangzó, az első ezen a helyen:', index+1)
