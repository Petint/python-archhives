import os


def get_new_title(title):
    _new_title = title[0] + title[1]
    _new_title += ' ' + title[-1]
    _new_title += ' - '
    for ttl in title[3:-5]:
        _new_title += ' ' + ttl
    return _new_title


def main():
    for _, _, titles in os.walk("./Sonic Boom", topdown=False):
        for title in titles:
            title = title.split()
            new_title = get_new_title(title)
            print(title, new_title, sep=' --> ')
    # os.rename()


if __name__ == '__main__':
    main()
