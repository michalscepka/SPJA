class Counter(object):

    counters = 0

    def __init__(self, count = 0):
        self.count_ = count
        Counter.counters += 1

    def __str__(self):
        return "count %s, counters %s." % (self.count, Counter.counters)

    def inc_counter(self):
        self.count_ += 1

    def get_count(self):
        return self.count_

    def set_count(self, value):
        self.count_ = value
    
    count = property(get_count, set_count)

    def __add__(self, other):
        if not isinstance(other, object):
            return None
        return Counter(self.count + other.count)

    def __del__(self):
        Counter.counters -= 1

'''
count1 = Counter()
count2 = Counter()
count3 = Counter()
print(count1)

count1.inc_counter()
print(count1)

count1.count = 4
print(count1.count)
'''
a = Counter(4)
b = Counter(3)
c = a + b
print(c)
c.count = 0
print(c)

print ("{} counters".format(Counter.counters))

c = 123
print ("{} counters".format(Counter.counters))
