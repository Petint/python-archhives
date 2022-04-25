mai_nap = input("Add meg a mai dátumot pontal elválasztva.\n>")
#Eltárolja a mai napot
mikr_sz = input("Add meg a születésed napját pontal elválasztva.\n>")
#Eltárolja a születés dátumot
years, months, days = 0, 0, 0
#Létrehoz egy változót az éveknek, kónapoknak, napoknak.
lenght_of_months = [31,28,31,30,31,30,31,31,30,31,30,31]
#eltárolja a hónapok hosszát

#Felbondja a dátuimokat
# 0 = Év
# 1 = Hónap
# 2 = Nap
for x in mai_nap:
    today = mai_nap.split(".")
for x in mikr_sz:
    megszületett = mikr_sz.split(".")
#Számokká álakítja a sövegeket
for i in range(len(megszületett)):
    megszületett[i] = int(megszületett[i])
for i in range(len(today)):
    today[i] = int(today[i])
#Kiszámolja az éveket
years = today[0] - megszületett[0]
#Kiszámolja a hónapokat

#Kiszámolja a napokat
while (not (megszületett[1] == today[1] and megszületett[0] == today[0] and megszületett[2] == today[2])):
    #Szökőév elenörzés
    if megszületett[2] == 2 and ((megszületett[0] % 4 == 0 and megszületett[0] % 100 != 0) or megszületett[0] % 400 == 0):
        #Szökőévben
        if megszületett[2] > lenght_of_months[megszületett[1]-1] + 1:
            megszületett[2] += 1
        else:
            megszületett[2] = 1
            megszületett[1] += 1
    else:   #ha nem szökőév van
        if megszületett[2] < lenght_of_months[megszületett[1]-1]:
            megszületett[2] += 1 #Még nincs vége a hónapnak
        else:
            #Vége van a hónapnak
            if megszületett[1] >= 12:   #Újév hónap reset
                megszületett[0] += 1
                megszületett[1] = 1
                megszületett[2] = 1
            else: 
                megszületett[1] += 1
                megszületett[2] = 1
    days += 1
#Kiadja az adatokat.
print(f"Te {years} éves vagy.\n Avagy {months} hónapós,\n Tehát {days} napos.")
