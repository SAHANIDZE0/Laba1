s=input("строка: ")
s2=s.lower().replace(" ", "")
if s2==s2[::-1]:
    print("палиндром")
else:
    print("не палиндром")
