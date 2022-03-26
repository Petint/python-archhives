def file_import(path: str):
    """Data import from specified file."""
    _feladatok_file = open(path, 'rt', encoding='utf-8')
    _feladatok_raw = _feladatok_file.read().splitlines()
    _feladatok_file.close()
    _feladatok = [f.split(';') for f in _feladatok_raw]
    del _feladatok_file, _feladatok_raw, _feladatok[0]
    return _feladatok


feladatok = file_import('feladatok.txt')
for feladat in feladatok:
    print(feladat)
