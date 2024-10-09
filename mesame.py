def shetrialeba(string):
    lst = []
    s = -1

    for i in string:
        lst.append(string[s])
        s -= 1
    return lst

print(shetrialeba("ojauhsdckjasdhbfjkka"))