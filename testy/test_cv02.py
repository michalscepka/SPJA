import numbers

#uloha 1
def invert(s):
    new_s = ""
    for c in s:
        if c.islower():
            new_s += c.upper()
        else:
            new_s += c.lower()
    return new_s

print(invert("Hello World!"))

#uloha 2
def translate(eng_word, dct={"one": "jedna", "two": "dve", "three": "tri", "four": "ctyri", "five": "pet"}):
    if eng_word not in dct:
        print("Slovo neni ve slovniku")
        print(sorted(dct))
        return None
    return dct[eng_word]

print(translate("twooo"))

#uloha 3
def fu(x):
    return 3*x + 5

def fu_map(f, lst):
    results = [f(item) for item in lst if isinstance(item, numbers.Number)]
    return results

print(fu_map(fu, ["Hello World", 3.14, 0, 5j]))

#uloha 4
def factorial(number):
    result = 1
    while number > 0:
        result *= number
        number = number - 1
    return result

print(factorial(5))

#uloha 5
def integrate(f, a, b, dx=0.1):
    i = a
    s = 0
    while i <= b:
        s += f(i)*dx
        i += dx
    return s

def linear(x):
    return (1/3)*x**3 - 2*x**2 + x + 8

print(integrate(linear, 0, 6))
