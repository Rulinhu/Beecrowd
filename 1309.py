import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
while True:
    try:
        moeda = float(float(input()) + (float(input()) / 100))

        print(locale.currency(moeda, grouping=True))
    except EOFError:
        break