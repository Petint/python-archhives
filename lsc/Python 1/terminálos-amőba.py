import winsound
palyatar = [" ","1","2","3","1","-","-","-","2","-","-","-","3","-","-","-"]
van_nyertes = False
player_1_fordulo = True

def row_check(r):
    start = r * 4 + 1
    return palyatar[start] == palyatar[start+1] and palyatar[start+1] == palyatar[start+2] and palyatar[start] !="-"

def column_c(c):
    start = 4 + c
    return palyatar[start] == palyatar[start+4] and palyatar[start+4] == palyatar[start+8] and palyatar[start] !="-"

def atlo_c(a):
    start = 4 + a
    step = 5
    return palyatar[start] == palyatar[start+step] and palyatar[start+step] == palyatar[start+2*step] and palyatar[start] !="-"

def printtable():
    for i in range(0, 16, 4):
        print("|".join(palyatar[i:i+4]))

while not van_nyertes:
    printtable()
    if player_1_fordulo:
        print("Játékps 1")
    else:
        print("Játékps 2")

    ujhely = False
    while not ujhely:
        sor , oszlop = 0 , 0
        while ((sor < 1 or sor > 3) or (oszlop < 1 or oszlop > 3 )):
            sor , oszlop =  int(input("Hányadik sor?\n> ")) ,int(input("Hányadik oszlop?\n> "))
        ujhely = palyatar[4* sor + oszlop] == "-"
        if player_1_fordulo:
            palyatar[4* sor + oszlop] = "O"
        else:
            palyatar[4* sor + oszlop] = "X"
        if row_check(1) or row_check(2) or row_check(3) or column_c(1) or column_c(2) or column_c(3) or atlo_c(1) or atlo_c(3):
            printtable()
            winsound.PlaySound("SystemAsterisk",winsound.SND_ASYNC)
            if player_1_fordulo:
               print("Játekosp 1 nyert")
               van_nyertes = True
            else:
               print("Játekosp 2 nyert")
               van_nyertes = True      
    player_1_fordulo = not player_1_fordulo
    
