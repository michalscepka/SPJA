#dynamicke typovani
a = 5
print(a)
#5
a = 5.4
type(a)
#<class 'float'>
a = 'ahoj'
print(a)
type(a)
#<class 'str'>

print(3+2)
#5
print(3/4)
#0.75
print(3//4) #int deleni
#0
print(3**4) #pow(3, 4)
#81
print(3%4)  #modulus
#3

print("abc"+"dbsdaf")
#'abcdbsdaf'
print("abc"+"dbc"*2)
#'abcdbcdbc'
print("abc"+"dbc"*4)
#'abcdbcdbcdbcdbc'

print(False + True)
#1
print(False and True)
#False
print(False or True)
#True
print(3>5)
#False

#seznam/list
lst = [1,2,3,4]
print(lst)
#[1, 2, 3, 4]
lst = [1,2,3,4,["a", "b"]]
print(lst)
#[1, 2, 3, 4, ['a', 'b']]
#help(lst)

print(lst[1])
#2
#print(lst[10])
#IndexError: list index out of range
#print(lst[])
#SyntaxError: invalid syntax
lst[::-1]   #obracene vypsane
#[['a', 'b'], 4, 3, 2, 1]
print(lst[-1])
#['a', 'b']
print(lst[:2])  #od 0. do 1. indexu
#[1, 2]
print(lst[:-2])
#[1, 2, 3]
print(lst[2:])
#[3, 4, ['a', 'b']]
print(lst[-2:])
#[4, ['a', 'b']]
print(lst[1:3])
#[2, 3]
lst[2]="1234"
print(lst)
#[1, 2, '1234', 4, ['a', 'b']]
len(lst)
#5
print(lst+lst)
#[1, 2, '1234', 4, ['a', 'b'], 1, 2, '1234', 4, ['a', 'b']]

#---n-tice---
vec=(1,2,3)
#vec[0] = 10
#TypeError: 'tuple' object does not support item assignment
len(vec)
#3
print(vec[:2])
#(1, 2)
print(vec[2]==3)
#True
vec=(1,2,3, 5.5, (1,), "ahoj", [1, 2, 3])
vec[-1][1]=22
print(vec)
#(1, 2, 3, 5.5, (1,), 'ahoj', [1, 22, 3])
#help(vec)

#---dictionary---
dct = {}
print(dct)
#{}
dct = {"one":1, "two":2}
print(dct)
#{'one': 1, 'two': 2}
print(dct["one"])
#1
dct["one"]="jedna"
print(dct)
#{'one': 'jedna', 'two': 2}
dct["three"]= "tri"
print(dct)
#{'one': 'jedna', 'two': 2, 'three': 'tri'}
print(dct.keys())
#dict_keys(['one', 'two', 'three'])
list(dct.keys())
#['one', 'two', 'three']
print("one" in dct)
#True

'''
def main():
    print("Hello world!")
    print("Hello another world!")

if __name__ == "__main__":
    main()
'''

#print("Hello world!")
#print("Hello another world!")

def add(a, b = 0):
    if a < 0:
        a = 0
    elif a < 5:
        a = a + 1
    else:
        a = a -1
    return a + b

def sum_of_items(lst):
    s = 0
    for x in lst:
        s += x
    '''non python pristup
    for i in range(len(lst)):
        s += lst[i]'''
    return s

def translate(eng_word, dct={"one": "jedna", "two": "dve"}):
    if eng_word not in dct:
        return None
    return dct[eng_word]

def myfce():
    pass

def main():
    print(add(10,))
    print(sum_of_items([1,2,3,4,5]))
    print(translate("twofff"))

if __name__ == "__main__":
    main()
