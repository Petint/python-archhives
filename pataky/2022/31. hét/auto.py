uzfogy = 0.06  # benzinfigyasztás/1Km
uzar = 500  # benzinár
# User megkérdezése:
try:
    aszam = int(input("Hány autó?\n> "))  # Autók száma
    atav = float(input("Mekkora távolság?\n> "))  # Távolság
except:
    print("Kérlek csak számot adj meg!")
else:
    # Kiszámolás:
    benzpc = atav * uzfogy  # Üzemanyagfogyaszás/autó kiszámítása
    benz = benzpc * aszam  # Beszorzás az autók számával
    ar = benz * uzar  # beszorzás az üzemanyagárral
    print(f"A(z) {aszam} autó {atav}Km alatt {benz}, azaz {ar}Ft. értékű benzint fogyasztott.")  # Kiirás forintban,
    # program leáll.
