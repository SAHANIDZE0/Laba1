def keshirovanie(f):
    keš={}
    def obvertka(*args):
        if args in keš:
            return keš[args]
        r=f(*args)
        keš[args]=r
        return r
    return obvertka

@keshirovanie
def kwadrat(x):
    print("считаю квадрат", x)
    return x*x

print(kwadrat(4))
print(kwadrat(4))
print(kwadrat(5))
print(kwadrat(5))
