mai_nap = input("Add meg a mai dátumot pontal elválasztva.\n>")
# Eltárolja a mai napot
mikr_sz = input("Add meg a születésed napját pontal elválasztva.\n>")
# Eltárolja a születés dátumot
years, months, days = 0, 0, 0
# Létrehoz egy változót az éveknek, kónapoknak, napoknak.
lenght_of_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# eltárolja a hónapok hosszát

# Felbondja a dátuimokat
# 0 = Év
# 1 = Hónap
# 2 = Nap
for x in mai_nap:
    today = mai_nap.split(".")
for x in mikr_sz:
    born = mikr_sz.split(".")
# Számokká álakítja a sövegeket
for i in range(len(born)):
    born[i] = int(born[i])
for i in range(len(today)):
    today[i] = int(today[i])
# Kiszámolja az éveket
years = today[0] - born[0]
# Kiszámolja a hónapokat

# Kiszámolja a napokat
while not (born[1] == today[1] and born[0] == today[0] and born[2] == today[2]):
    # Szökőév elenörzés
    if born[2] == 2 and (
            (born[0] % 4 == 0 and born[0] % 100 != 0) or born[0] % 400 == 0):
        # Szökőévben
        if born[2] > lenght_of_months[born[1] - 1] + 1:
            born[2] += 1
        else:
            born[2] = 1
            born[1] += 1
    else:  # ha nem szökőév van
        if born[2] < lenght_of_months[born[1] - 1]:
            born[2] += 1  # Még nincs vége a hónapnak
        else:
            # Vége van a hónapnak
            if born[1] >= 12:  # Újév hónap reset
                born[0] += 1
                born[1] = 1
                born[2] = 1
            else:
                born[1] += 1
                born[2] = 1
    days += 1
# Kiadja az adatokat.
print(f"Te {years} éves vagy.\n Avagy {months} hónapós,\n Tehát {days} napos.")
