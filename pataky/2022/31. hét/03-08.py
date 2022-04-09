"""Black Tom's circle calculator by Petint"""
from math import pi


def kerulet(r: float) -> float:
    return 2 * r * pi


def felulet(r: float, k: float) -> float:
    return r * k


print('Egy kor keruletet es feluletet fogjuk meghatarozni.')
sugar = float(input('Add meg a kor sugarat: '))
krt = kerulet(sugar)
flt = felulet(sugar, krt)
print('A kor kerulete: %fcm\nA kor felulete: %fcm2' % (round(krt, 2), round(flt, 2)))
