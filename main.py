
def code(a, b, message, n):
    alphabet, c = [chr(i) for i in range(97, 97 + 26)], ""
    for i in message:
        nb = alphabet.index(i)
        if n == 0:
            nb += a
        else:
            nb -= a
        c += alphabet[nb % 26]
        x = a
        b %= 26
        a = b
        if b < 10:
            b += x
        elif b < 20:
            b = int(str(b)[-1]) * 2 + x
        else:
            b = int(str(b)[-1]) ** 2 + x
    return c


def main():
    while True:
        print('Saisir :\n 1 pour crypter,\n 2 pour decoder \n 3 pour quitter')
        n = input()
        if n.isdigit():
            if n == "1" or n == "2":
                print("Veuillez-entrer la premiere clé")
                a = input()
                print("Veuillez-entrer la deuxième clé")
                b = input()
                print("Veuillez-entrer le message")
                c = input()
                if a.isdigit() and b.isdigit():
                    c = code(int(a), int(b), c.lower(), int(n) - 1)
                    print(c)
            elif n == "3":
                break


main()
