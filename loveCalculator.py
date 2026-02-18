def calculate_love_score(name1, name2):
    names = (name1 + name2).upper()  # make case insensitive
    Total = 0
    Total1 = 0
    T = R = U = E = 0

    for i in names:
        if i == "T":
            T += 1
        if i == "R":
            R += 1
        if i == "U":
            U += 1
        if i == "E":
            E += 1

        Total = T + R + U + E

    L = O = V = E2 = 0

    for i in names:
        if i == "L":
            L += 1
        if i == "O":
            O += 1
        if i == "V":
            V += 1
        if i == "E":
            E2 += 1

        Total1 = L + O + V + E2

    connect = int(str(Total) + str(Total1))
    print(connect)


calculate_love_score("Tire", "Tile")