def unikalnye(spisok):
    r=[]
    def obhod(s):
        for x in s:
            if isinstance(x, list):
                obhod(x)
            elif x not in r:
                r.append(x)
    obhod(spisok)
    return r

m=[1, 2, [3, 2], [4, [5, 3]], 6]
print("уникальные:", unikalnye(m))
