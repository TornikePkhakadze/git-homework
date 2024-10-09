def remove_dupl(string):
    lst=[]

    for char in string:
        if char not in lst:
            lst.append(char)
    
    st = "".join(lst)
    if s == st:
        return True
    else:
        return False
            
s = "lppo"


print(remove_dupl(s))