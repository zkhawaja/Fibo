

def Fibo(x):
    if x==0 or x==1:
        return x
    else:
        return Fibo(x-1) + Fibo(x-2)
