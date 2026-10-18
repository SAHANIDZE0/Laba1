def type_check(*tipy):
    def dekor(f):
        def obvertka(*args, **kwargs):
            for i in range(len(args)):
                if not isinstance(args[i], tipy[i]):
                    raise TypeError("неверный тип аргумента "+str(i+1))
            return f(*args, **kwargs)
        return obvertka
    return dekor

@type_check(int, int)
def slozhi(a, b):
    return a+b

print(slozhi(2, 3))
print(slozhi(2.5, 3))
