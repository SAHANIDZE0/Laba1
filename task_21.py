import time
def timing(f):
    def obvertka(*args, **kwargs):
        t1=time.time()
        r=f(*args, **kwargs)
        t2=time.time()
        print("время:", round((t2-t1)*1000, 3), "мс")
        return r
    return obvertka

@timing
def schet(n):
    s=0
    for i in range(n):
        s+=i
    return s

schet(500000)
