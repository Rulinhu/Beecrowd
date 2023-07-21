while True:
    try:
        string = input()
        counter = 0
        new_string = ''
        for i, c in enumerate(string):
            if string[i] != " ":
                if counter % 2 == 0:
                    new_string += c.upper()
                else:
                    new_string += c.lower()
                counter += 1
            else:
                new_string += " "

        print(new_string)

    except EOFError:
        break