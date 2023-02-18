import os


def get_new_title(title):
    title = title.split()
    _new_title = 'Sonic Boom '
    _new_title += 'episode ' + title[-2]
    _new_title += ' -'
    for ttl in title[3:-4]:
        _new_title += ' ' + ttl
    return _new_title


def main():
    for _, _, titles in os.walk("./Sonic Boom", topdown=False):
        for title in titles:
            new_title = get_new_title(title)
            print(title, new_title, sep=' --> ')
            os.rename(os.path.join('./Sonic Boom', title), os.path.join('./Sonic Boom', new_title+'.mp4'))


if __name__ == '__main__':
    main()
