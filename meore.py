def racqvia(string):
    dick = {}
    for i in string:
        if i not in dick:
            dick[i] = 1
        else:
            dick[i] += 1
    return dick
print(racqvia("matebote"))
