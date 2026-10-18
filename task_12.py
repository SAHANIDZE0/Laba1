text=input("текст: ")
words=text.replace(",", "").replace(".", "").replace("!", "").replace("?", "").split()
chast={}
for w in words:
    w=w.lower()
    chast[w]=chast.get(w, 0)+1
samoe=""
kolvo=0
for w in chast:
    if chast[w]>kolvo:
        samoe=w
        kolvo=chast[w]
kor=words[0]
dl=words[0]
for w in words:
    if len(w)<len(kor):
        kor=w
    if len(w)>len(dl):
        dl=w
print("слов всего:", len(words))
print("самое частое:", samoe, "-", kolvo)
print("короткое:", kor)
print("длинное:", dl)
print("частоты:", chast)
new=[w for w in words if len(w)>=3]
print("после фильтра слов всего:", len(new))
chast2={}
for w in new:
    w=w.lower()
    chast2[w]=chast2.get(w, 0)+1
print("частоты после фильтра:", chast2)
