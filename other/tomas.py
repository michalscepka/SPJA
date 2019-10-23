"""
    1 point
    Return a function that will add `n` to its parameter.
    If this function receives no parameter, it should create an incrementor that adds 1 to its parameter.
    Example:
        inc = incrementor(5)
        inc(6) # 11
        inc(1) # 6
        inc = incrementor()
        inc(2) # 3
    """

'''
def incrementor(n = 1):
    return lambda x: x + n

inc = incrementor(5)
print(inc(6))'''

#-------------------------------------------------------------------

"""
2 points
Return a closure that will generate elements of the Fibonacci sequence when called repeatedly.
Example:
    g = fibonacci_closure()
    g() # 1
    g() # 1
    g() # 2
    g() # 3
    ...
"""
'''
def fibonacci_closure():
    n_1 = 0
    n_2 = 0 
    def fib():
        nonlocal n_1, n_2
        if n_1 == 0 and n_2 == 0:
            n_1 = 1
            return n_1
        else:
            n = n_1 + n_2
            n_2 = n_1
            n_1 = n  
            return n
    return fib

g = fibonacci_closure()
print(g())
print(g())
print(g())
print(g())'''

#-------------------------------------------------------------------
"""
2 points
Return a generator that will generate prime numbers when iterated.
Example:
    for i in prime_generator():
        print(i)
    # 2, 3, 5, 7, 11, 13 ...
"""
'''
def prime_generator():
    primes = []
    for possiblePrime in range(2, 30):
        isPrime = True
        for num in range(2, possiblePrime):
            if possiblePrime % num == 0:
                isPrime = False
        
        if isPrime:
            primes.append(possiblePrime)
    
    return primes

for i in prime_generator():
    print(i)'''

#-------------------------------------------------------------------

"""
2 points
Open file located at `src`, keep only lines that contain the `keyword`, sort them in ascending
order and write them to file located at `dst`.
If `src` does not exist, return "file not found".
If everything goes ok, return "ok".
Example:
    transform_file('in.txt', 'out.txt', 'or')
    in.txt:
    barrens
    stormwind
    gondor
    ashenvale
    hogwarts
    yavin
    coruscant
    out.txt:
    coruscant
    gondor
    stormwind
"""

def transform_file(src, dst, keyword):
    lst = []
    with open(src, "r") as my_file:
        for line in my_file:
            if keyword in line:
                lst += [line]
    
    with open(dst, "w") as my_file:
        for item in lst:
            my_file.write(item)
    
transform_file("c:\\Users\\Michal\\Desktop\\in.txt", "c:\\Users\\Michal\\Desktop\\out.txt", "or")



#-------------------------------------------------------------------

def cached(f):
    """
    2 points
    Create a decorator that caches the latest function result.
    When `f` is called multiple times in a row with the same parameter, compute the result just
    once and then return the result from cache.
    When `f` receives a different parameter, reset the cache and compute a new result.
    Assume that `f` receives exactly one parameter.
    Example:
        @cached
        def fn(a):
            return a + 1 # imagine an expensive computation
        fn(1) == 2 # computed
        fn(1) == 2 # returned from cache, `a + 1` is not executed
        fn(3) == 4 # computed
        fn(1) == 2 # computed
    """
    pass


#-------------------------------------------------------------------

def bonus_tree_walker(tree, order):
    """
    1 point (bonus)
    Write a generator that traverses `tree` in the given `order` ('inorder', 'preorder' or 'postorder').
    You should know this from 'Algoritmy II'.
    The tree is represented with nested tuples (left subtree, value, right subtree).
    If there is no subtree, it will be marked as None.
    Example:
        tree = (((None, 8, None), 3, (None, 4, None)), 5, (None, 1, None))
            5
           / \
          3   1
         / \
        8   4
        list(bonus_tree_walker(tree, 'inorder')) == [8, 3, 4, 5, 1]
        list(bonus_tree_walker(tree, 'preorder')) == [5, 3, 8, 4, 1]
        list(bonus_tree_walker(tree, 'postorder')) == [8, 4, 3, 1, 5]
    """
    pass