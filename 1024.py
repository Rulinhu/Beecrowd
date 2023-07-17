p = int(input())

for i in range(p):
    text = input()
    text2 = ''
    text3 = ''

    for j in text:
        if (65 <= ord(j) <= 90 or 97 <= ord(j) <= 122):
                text2 += chr(ord(j) + 3)
        else:
            text2 += j

    text2 = text2[::-1]

    for j in text2[int(len(text2) / 2):]:
        text3 += chr(ord(j) - 1)

    print(text2[0:len(text2) // 2] + text3)