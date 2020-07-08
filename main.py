from datetime import datetime


def code(a, b, c, n):
    if n == 0:
        c = cle(a, b, c, n)
        c = sub(c, n)
    else:
        c = sub(c, n)
        c = cle(a, b, c, n)
    return c


def sub(c, n):
    alphabet = [chr(i) for i in range(97, 97 + 26)]
    date = datetime.now()
    y = date.year
    m = date.month
    d = date.day
    fact_26 = 403291461126605635584000000
    dec = pow(d + m, y + d, fact_26)
    Sub = []
    res = alphabet[:]

    for i in range(26, 1, -1):
        r = dec % i
        dec //= i
        Sub.append(res[r])
        del res[r]
    Sub.append(res[0])
    t = ""
    for i in range(len(c)):
        if c[i] in alphabet:
            if n == 0:
                t += Sub[alphabet.index(c[i])]
            else:
                t += alphabet[Sub.index(c[i])]
        else:
            t += c[i]
    return t


def cle(a, b, message, n):
    alphabet, c = [chr(i) for i in range(97, 97 + 26)], ""
    for i in message:
        if i in alphabet:
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
                b = (b % 10) * 2 + x
            else:
                b = (b % 10) ** 2 + x
        else:
            c += i
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
