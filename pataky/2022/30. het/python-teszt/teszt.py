# file import
path = 'feladatok.txt'
feladatok_file = open(path, 'rt', encoding='utf-8')
feladatok_raw = feladatok_file.read().splitlines()
feladatok_file.close()
feladatok = [f.split(';') for f in feladatok_raw]
del feladatok_file, feladatok_raw, feladatok[0]

for feladat in feladatok:
    print(feladat)
