import math


def handle(f, x):
    return f(x)


def f(x):
    return x


def Logarit(x):
    return math.log2(x)


def nLogarit(x):
    return x * math.log2(x)


def Square(x):
    return x * x


def Cubic(x):
    return pow(x, 3)


def Exp(x):
    return pow(2, x)


n = [1, 2, 4, 8, 16, 32, 64, 128]

f1 = []
f2 = []
f3 = []
f4 = []
f5 = []
f6 = []

for i in n:
    f1.append(handle(f, i))
for i in n:
    f2.append(handle(Logarit, i))
for i in n:
    f3.append(handle(nLogarit, i))
for i in n:
    f4.append(handle(Square, i))
for i in n:
    f5.append(handle(Cubic, i))
for i in n:
    f6.append(handle(Exp, i))
