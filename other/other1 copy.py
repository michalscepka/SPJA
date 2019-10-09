def filter_numbers(lst):
    sorted = [item for item in lst if isinstance(item, (int, float)) and not isinstance(item, bool)]
    sorted.sort()
    return sorted
         
print(filter_numbers([1.2, "sdas", 4, [12], 3.4, "12", -3, True, 5, 8.1]))

def check_brackets(str):
    count = 0
    for item in str:
        if item == "(":
            count += 1
        elif item == ")":
            count -= 1
        if count < 0:
            return False
    
    if count != 0:
        return False
    return True

print(check_brackets("(a+b)/(b*(a+c))"))
print(check_brackets("(a+b))/((b*(a+c))"))
print(check_brackets("(a+b)/(b*(a+c)"))

'''def fun_extrems(fce, a, b):


def f(x):
    return x*(x-2)

fun_extrems(f, -5, 5)'''
'''
def number_of_letters(lst):
    lst.lower()
    samohlasky = { "a": 0, "e": 0, "i": 0, "o": 0, "u": 0 }
    for 

print(number_of_letters('Technical University Ostrava'))
'''