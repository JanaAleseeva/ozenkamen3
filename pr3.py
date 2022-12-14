with open("sckola.txt") as f:
    kol = 0
    sum = 0
    for l in f:
        kol += 1
        l1 = len(l)
        for i in range(l1):
            if l[i].isdigit():
                num = int(l[i])
                sum += num
                if num < 3:
                    print("Ученик, чья оценка меньше 3-х:", l)
                break
    sred = sum / kol
    print("Средний бал по классу:", sred)