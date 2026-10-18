def sdelat_ploskim(spisok):
    i=0
    while i<len(spisok):
        if isinstance(spisok[i], list):
            vn=spisok[i]
            del spisok[i]
            sdelat_ploskim(vn)
            for j in range(len(vn)):
                spisok.insert(i+j, vn[j])
            i+=len(vn)
        else:
            i+=1

dannye=[1, 2, [3, 4], 5, [6, [7, 8]]]
print("было:", dannye)
sdelat_ploskim(dannye)
print("стало:", dannye)
