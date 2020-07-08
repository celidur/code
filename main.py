from datetime import datetime
import random


def code(a, b, c, n, y, m, d):
    if n == 0:
        c = cle(a, b, c, n)
        c = sub(c, n, y, m, d)
    else:
        c = sub(c, n, y, m, d)
        c = cle(a, b, c, n)
    return c


def sub(c, n, y, m, d):
    alphabet = [chr(i) for i in range(97, 97 + 26)]
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
        r = 1
        print('Saisir :\n 1 pour crypter,\n 2 pour decoder \n 3 pour quitter')
        n = input()
        if n.isdigit():
            if n == "1" or n == "2":
                if n == "2":
                    print("Ce message a-t-il été envoyé aujourd'hui ? (O/N)")
                    r = input()
                if n == "1" or r.lower() == 'o':
                    date = datetime.now()
                    y = date.year
                    m = date.month
                    d = date.day
                else:
                    print("Veuillez entrer l'année d'écriture du message")
                    y = int(input())
                    print("Veuillez entrer le mois d'écriture du message")
                    m = int(input())
                    print("Veuillez entrer le jour d'écriture du message")
                    d = int(input())
                random.seed(pow(y + m, m + d))
                a = random.randint(0, 25)
                random.seed(pow(y + d, (m + d) * y, y ** y))
                b = random.randint(0, 25)
                d = 0
                while a % 10 == 0 and b % 10 == 0:
                    d += 1
                    random.seed(pow(y + m, m + d) + d)
                    a = random.randint(0, 25)
                    random.seed(pow(y + d, (m + d) * y, y ** y) + d)
                    b = random.randint(0, 25)
                print("Veuillez-entrer le message")
                c = input()

                if str(a).isdigit() and str(b).isdigit():
                    c = code(int(a), int(b), c.lower(), int(n) - 1, y, m, d)
                    print('\n' + c + '\n')
            elif n == "3":
                break


main()
