def sliyanie(a, b):
    for k in b:
        if k in a:
            if isinstance(a[k], dict) and isinstance(b[k], dict):
                sliyanie(a[k], b[k])
            elif isinstance(a[k], list) and isinstance(b[k], list):
                for x in b[k]:
                    if x not in a[k]:
                        a[k].append(x)
            elif isinstance(a[k], set) and isinstance(b[k], set):
                a[k]=a[k]|b[k]
            else:
                a[k]=b[k]
        else:
            a[k]=b[k]
    return a

d1={"a": 1, "b": {"c": 1, "d": 2}}
d2={"e": 3, "b": {"c": 5, "f": 6}}
sliyanie(d1, d2)
print(d1)
