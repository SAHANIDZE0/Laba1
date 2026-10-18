import datetime
def log_calls(fname):
    def obvertka(f):
        def vnutr(*args, **kwargs):
            with open(fname, "a", encoding="utf-8") as file:
                vremya=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(vremya+" "+f.__name__+" "+str(args)+" "+str(kwargs)+"\n")
            return f(*args, **kwargs)
        return vnutr
    return obvertka

@log_calls("log.txt")
def plus(a, b):
    return a+b

plus(3, 4)
plus(1, 2)
print("записано в log.txt")
