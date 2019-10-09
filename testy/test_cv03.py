import numbers

#1
def fu(a, b, x):
    return ((a*x) + b)

def fu_map(a, b, f, *x):
    li = [f(a, b, item) for item in x if isinstance(item, numbers.Number)]
    return li

print(fu_map(1.5, 2.75, fu, 0.0, 1.0, 2.0, 3.0, 4.0, 'Sun'))

#2
'''
def fu_map2(*x):
    tup = (lambda a, b, x: (a * x) + b )'''

#3
def sort(li):
    return sorted(set(li), key=li.index)

print(sort([6, 1, 2, 20, 6, 210, 6]))

#4
def smallest(num):
    for i in range(2, num+1):
        if num % i == 0:
            return i

print(smallest(32))

'''
#5
def area(my_file, dct):
    try:
        my_file = open(my_file, "rt")
        try:
            dct = ([line.split() for line in my_file])
        finally:
            my_file.close()
    except IOError as e:
        print(e)



    print(dct)

dct = {}
print(area("C:/Users/Michal/Desktop/file.txt", dct))'''
