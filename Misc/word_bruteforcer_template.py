alphalow = 'abcdefghijklmnopqrstuvwxyz'
alphahigh = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '0123456789'
alpha = alphalow + alphahigh
alnum = alpha + num

candidate = alphalow
max_length = 5
prefix = ''


def main():
    run(prefix)


def run(base):

    if len(base) >= max_length:
        return

    for c in candidate:
        word = base + c
        chk(word)
        run(word)


def chk(word):
    # print(word)
    # implement here
    pass


if __name__ == '__main__':
    main()