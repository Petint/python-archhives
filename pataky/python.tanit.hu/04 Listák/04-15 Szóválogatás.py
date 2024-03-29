"""
Kérjünk be a felhasználótól három betűt és a keresett szavak hosszát.
A programban már megadott hosszú magyar szavak közül válogassuk ki azokat, amelyekben szerepel a három betű és adott hosszúságúak.
Ellenőrizzük, hogy a hossz legalább 9 és legfeljebb 21 legyen. Ha nem az, akkor kérjük be újra.
Ellenőrizzük a betűk számát is, és ha netán nem hármat adott meg a felhasználó, kérjük be újra.
Ha nem található a feltételnek megfelelő szó, akkor azt írjuk ki, különben listázzuk ki a talált szavakat a mintának megfelelően.
"""

# Hosszú magyar szavak listája:
szavak = ['adminisztráció', 'aggodalmaskodik', 'akadékoskodik', 'akaratnyilvánítás', 'akasztófáravaló',
          'akklimatizálódik', 'aktualizálódik', 'alkoholmérgezés', 'alkotóképesség', 'állatszelídítő', 'állításköteles',
          'antialkoholista', 'áttekinthetetlen', 'automatikus', 'autóvezető', 'bebizonyosodik', 'becsületbíróság',
          'belebocsátkozik', 'belebonyolódik', 'belecsimpaszkodik', 'belehabarodik', 'beleilleszkedik',
          'belekotnyeleskedik', 'belerozsdásodik', 'beletemetkezik', 'belevörösödik', 'bizalomgerjesztő',
          'bizonyíthatatlan', 'boszorkányégetés', 'búcsúelőadás', 'búcsúlátogatás', 'centralizáció', 'ceruzahegyező',
          'cigarettaszünet', 'csalatkozhatatlan', 'csapatösszevonás', 'csecsemőgondozó', 'cselekvőképesség',
          'cselekvőképtelenség', 'cseresznyepálinka', 'csillapíthatatlan', 'diadalkoszorú', 'diadalmaskodik',
          'dolgavégezetlenül', 'egészségvédelem', 'egybeilleszkedik', 'elállatiasít', 'elállatiasodik',
          'elanyátlanodik', 'elbátortalanít', 'elbátortalanodik', 'elcsökevényesedik', 'elégedetlenkedik',
          'elégtételadás', 'elengedhetetlen', 'elértéktelenedik', 'életfilozófia', 'életfogytiglani',
          'élethossziglani', 'életlehetőség', 'életmegnyilvánulás', 'elévülhetetlen', 'elforgácsolódik',
          'elgondolkodtató', 'elhomályosodik', 'elidegenedik', 'elkanászosodik', 'elkedvetlenedik',
          'ellenforradalmár', 'ellenforradalmi', 'ellenforradalom', 'elmagyarosodik', 'elmaradhatatlan',
          'elmegyógyintézet', 'előadóművész', 'előreláthatólag', 'elsivatagosodik', 'elszemtelenedik',
          'elszigetelődik', 'elszíntelenedik', 'elterebélyesedik', 'eltörölhetetlen', 'elválaszthatatlan',
          'elvárosiasodik', 'elvilágiasodik', 'elviselhetetlen', 'elvitathatatlan', 'emancipáció', 'emberábrázolás',
          'emberemlékezet', 'emlékkiállítás', 'emocionális', 'enciklopédia', 'enciklopédikus', 'engedetlenkedik',
          'engesztelhetetlen', 'építőművészet', 'erőszakoskodik', 'értelemárnyalat', 'érzéstelenítés',
          'érzéstelenítő', 'exhibicionizmus', 'fájdalomcsillapító', 'fantazmagória', 'fejlődésképtelen',
          'felbecsülhetetlen', 'felegyenesedik', 'felelevenítés', 'felhőátvonulás', 'felülmúlhatatlan',
          'felvilágosítás', 'felvilágosodott', 'figyelembevétel', 'fizetésképtelen', 'generáljavítás',
          'gondolatolvasó', 'gondolatpárhuzam', 'gyakornokoskodik', 'gyarmatbirodalom', 'gyermekhalandóság',
          'gyermekirodalom', 'gyógypedagógia', 'gyógyszerészhallgató', 'háborúellenes', 'haditengerészet',
          'hadkötelezettség', 'hadseregtábornok', 'halálveszedelem', 'hallucináció', 'hasznavehetetlen',
          'haszontalankodik', 'határozatképes', 'helyreigazítás', 'hiábavalóság', 'homeopátia', 'hozzáférhetetlen',
          'hozzávetőleges', 'humanitárius', 'idegcsillapító', 'idegenlégió', 'idegenvezető', 'idegkimerülés',
          'idegkimerültség', 'idegösszeroppanás', 'ideggyógyintézet', 'ideológia', 'ideológiai', 'ideszemtelenkedik',
          'idevonatkozó', 'időmilliomos', 'időpocsékolás', 'igazságkeresés', 'igazságszeretet', 'igazságtalanság',
          'imperialista', 'imperializmus', 'inaszakadtáig', 'individuális', 'indulatoskodik', 'irracionális',
          'ismeretterjesztő', 'istenigazában', 'istenigazából', 'ítélethirdetés', 'javakorabeli', 'javítóintézet',
          'jelentésváltozás', 'jövedelemtöbblet', 'kálváriajárás', 'kamarazenekar', 'kapituláció', 'katonaszökevény',
          'kellemetlenkedik', 'keresztényüldözés', 'keresztülerőszakol', 'keresztülvihetetlen', 'késedelmeskedik',
          'kétségbevonhatatlan', 'kezességvállalás', 'kiapadhatatlan', 'kibékíthetetlen', 'kiegyenlítődik',
          'kiegyensúlyozott', 'kiengesztelődik', 'kifürkészhetetlen', 'kiismerhetetlen', 'kilométeróra',
          'kimagyarázkodik', 'kiszolgáltatottság', 'kiterebélyesedik', 'kitörölhetetlen', 'kivilágosodik',
          'koreográfia', 'kormeghatározás', 'köpönyegforgató', 'körmeszakadtáig', 'körömszakadtáig',
          'körülményeskedik', 'köszönetnyilvánítás', 'kötelességmulasztás', 'kötelességtudó', 'kötélidegzetű',
          'következésképpen', 'következetesség', 'következetlenség', 'közbeékelődik', 'közteherviselés',
          'kultúrforradalom', 'kutatóintézet', 'külpolitikai', 'laboratórium', 'lámpagyújtogató', 'lealacsonyodik',
          'leegyszerűsödik', 'lehetetlenülés', 'lekicsinyelhető', 'lélegzetelállító', 'lélegzetvisszafojtva',
          'lelkiismeretesség', 'lelkiismeretlen', 'lépcsőkanyarulat', 'letagadhatatlan', 'létbizonytalanság',
          'levélkézbesítő', 'magatehetetlen', 'manipuláció', 'másodpercmutató', 'materialista', 'megacélosodik',
          'megalománia', 'megbecstelenítő', 'megbecsülhetetlen', 'megbizonyosodik', 'megbocsáthatatlan',
          'megemberesedik', 'megfellebbezhetetlen', 'megfiatalodik', 'megfizethetetlen', 'meggondolatlanság',
          'meghatározhatatlan', 'megingathatatlan', 'megközelíthetetlen', 'megközelíthető', 'megkülönböztetett',
          'megmagyarázhatatlan', 'megmakrancosodik', 'megsokszorozódik', 'megtámadhatatlan', 'megtermékenyítés',
          'megvesztegethetetlen', 'megvilágosodik', 'megvirágosodik', 'munkahipotézis', 'munkalehetőség',
          'munkanélküliség', 'művészettörténet', 'nacionalista', 'nacionalizmus', 'nagyfejedelemség',
          'nekifohászkodik', 'nekirugaszkodik', 'nekiveselkedik', 'nélkülözhetetlen', 'népfelszabadító',
          'neveletlenkedik', 'nevelőintézet', 'nikotinmérgezés', 'normalizálódik', 'nyakszirtmerevedés',
          'nyughatatlankodik', 'obszervatórium', 'odasettenkedik', 'okvetetlenkedés', 'okvetetlenkedik',
          'olvasóközönség', 'olvasztókemence', 'operaénekes', 'operettfigura', 'oroszlánszelídítő', 'öntözőcsatorna',
          'öntudatosodik', 'örökbefogadás', 'örökkévalóság', 'összecsavarodik', 'összecsomósodik',
          'összecsoportosul', 'összeelegyedik', 'összefacsarodik', 'összeférhetetlen', 'összeférhetetlenség',
          'összegubancolódik', 'összegyülekezik', 'összehasonlítás', 'összeházasodik', 'összeismerkedik',
          'összekapaszkodik', 'összekovácsolódik', 'összekunkorodik', 'összeszedelődzködik', 'pánamerikai',
          'páneurópai', 'páralecsapódás', 'paralelogramma', 'petróleumfőző', 'petróleumlámpa', 'pillanatfelvétel',
          'predesztináció', 'primadonnáskodik', 'professzionista', 'professzionizmus', 'racionalizál',
          'rakoncátlankodik', 'regeneráció', 'regenerálódik', 'reprezentáció', 'reprezentációs',
          'reprodukálhatatlan', 'részvétlátogatás', 'részvétnyilvánítás', 'riadókészültség', 'spiritualizmus',
          'stabilizáció', 'szabadgondolkodó', 'szabadságszerető', 'szabálytalankodik', 'szembehelyezkedik',
          'szentimentalizmus', 'szenzációhajhászás', 'szerecsenmosdatás', 'szeretetadomány', 'szeretetlakoma',
          'szeretetreméltóság', 'szeretetvendégség', 'szétforgácsolódik', 'szőrszálhasogatás', 'szövegösszefüggés',
          'tájékozatlanság', 'takarékoskodik', 'tankötelezettség', 'tántoríthatatlan', 'tautológia',
          'tehetetlenségi', 'tehetségkutató', 'teketóriázik', 'tekintetbevétel', 'teleológia', 'temperamentumos',
          'térgeometria', 'természetbölcselet', 'természetimádás', 'természetimádó', 'termonukleáris',
          'tetszésnyilvánítás', 'titokzatoskodik', 'torokköszörülés', 'tömeghisztéria', 'tömegmegmozdulás',
          'tömegszerencsétlenség', 'tömegszuggesztió', 'történelemformáló', 'történettudomány', 'tragédiaköltő',
          'tragikomédia', 'tudomásulvétel', 'türelmetlenkedik', 'udvariaskodik', 'uszálypolitika', 'utánozhatatlan',
          'útbaigazítás', 'vadászrepülőgép', 'valamirevaló', 'végeláthatatlan', 'végeszakadatlan', 'vegetáriánus',
          'végkielégítés', 'végkövetkeztetés', 'véleménynyilvánítás', 'vigasztalhatatlan', 'világbirodalom',
          'világirodalom', 'világszenzáció', 'világviszonylatban', 'visszaemlékezés', 'visszavonhatatlan',
          'vitaelőadás', 'zabolázhatatlan', 'zászlólobogtatás', 'zeneirodalom', 'zenepedagógus', 'zongorabillentyű',
          'zongorahangverseny', 'zongoratanítás']

# Itt folytassuk a program írását


def check_length(word: str, desired_length: int):
    return len(word) == desired_length


def does_contain(search_word, letters_to_find):
    letter_count = 0
    for letter in letters_to_find:
        if letter in search_word:
            letter_count += 1
    return letter_count == 3


def main():
    print('Magyar szavak között keresünk adott hosszúsagút, amelyben szerepel három megadott betű.\n')
    letters = input('Adj meg három betűt:')
    length = int(input('\nAdd meg a keresett szavak hosszát (9-21):'))
    candidates = (word for word in szavak if check_length(word, length))
    candidates = (word for word in candidates if does_contain(word, letters))
    print('Ezekre a szavakra gondolhattál:')
    [print(word) for word in candidates]


if __name__ == '__main__':
    main()
