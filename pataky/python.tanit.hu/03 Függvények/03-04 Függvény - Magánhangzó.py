def maganhangzo(char: chr) -> bool:
    if char.lower() in 'uioaöüóőúéáűí':
        return True
    return False


if __name__ == '__main__':
    letter = input('Adj meg egy betűt:')
    print('A megadott betű magánhangzó') if maganhangzo(letter) else print('A megadott betű Mássalhangzó')