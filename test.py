import time

n=456378902858290907415273676326459758501863587455889046415299414290812776158851091008643992243505529957417209835882169153356466939122622249355759661863573516345589069208441886191855002128064647429111920432377907516007825359999

n2 = int(n**0.5)
temp = time.time()
for i in range(((n - 2 * n2 + 1) // 4) * 4, 0, -4):
    if i % 10000 == 0:
        print(i)
        print(time.time() - temp)
        temp = time.time()
    if pow(2, i, n) == 1:
        print(i)