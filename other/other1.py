a = 1
if a > 0:
    print("kokos")

a = 10
b = 2

slovnik = {"SPJA" : "Skripta"}
slovnik[460] = "katedra"
print(slovnik)

for i in slovnik:
    print("i:", i, "hodnota:", slovnik[i])


i = 0

while i < 5:
    print(i)
    i += 1

seznam = [1, 2, 5, "ahoj", 10, 100]

sum = 0

for prvek in seznam:
    if type(prvek) == int or type(prvek) == float:
        sum += prvek

print(sum)

def sqr(number, exponent = 2):
    return number**exponent

print(sqr(3, 5))

def args_fce(a, *b):
    print(a, b)

args_fce(1, 2)
args_fce(1, 2, 3, 4, 5)
args_fce(1, 2, 3, 4, "ahoj", 5)

def super_print(*p):
    s = " ".join(p)
    print("-" * len(s))
    print(s)
    print("-" * len(s))

super_print("jedna", "dve", "tri", "4")

def kw_fce(a, **kw):
    print(a, kw)

kw_fce("jedna", SPJA="Skripta", ALG="Algoritmy")

def filtruj_mesta(mesta, **kw):
    filtrovane = []
    if 'gt' in kw:
        limit = kw['gt']
        filtrovane = [key for key in mesta if mesta[key] > limit]
    return filtrovane

mesta = {"Ostrava": 336000, "Praha": 1249000,
        "Brno": 405000, "Olomouc": 101000,
        "Karvina": 63000, "Havirov": 82000}

print(filtruj_mesta(mesta, gt=100000))

def kokos(number, exponent = 2):
    return number**exponent

kks = kokos

print(kokos(3))
print(kks(3))

def sqr_lst(fun, lst):
    ret_lst = []
    for item in lst:
        ret_lst.append(fun(item))
    return ret_lst

print(sqr_lst(sqr, [1, 2, 3]))

sqr = lambda x: x**2
print(sqr(2))

pow = lambda number, exponent: number**exponent
print(pow(2, 3))

