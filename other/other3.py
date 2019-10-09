class Battlestar(object):

    def __init__(self, name, commnader):
        self.name = name
        self.commander = commnader

    def toString(self):
        return "This is Battlestar %s, commanded by %s." \
            % (self.name, self.commander)

galactica = Battlestar('Galactica', 'Bill Adama')
pegasus = Battlestar('Pegasus', 'Helena Cain')

print(galactica.toString())
print(pegasus.toString())

class eg(object):
    cla = []

    def __init__(self):
        self.ins = {}
    
    def meth1(self, x):
        self.cla.append(x)
    
    def meth2(self, y, z):
        self.ins[y] = z
    
es1 = eg()
es2 = eg()

#print(es1.cla)
#print(es1.ins)

es1.meth1(1)
es1.meth2(2, 3)

print(es1.cla)
print(es1.ins)

class sub(eg):
    def meth2(self, x, y = 1):  #override
        eg.meth2(self, x, y)    #super-call
        
class repeater(list):
    def append(self, x):
        for i in 1, 2:
            list.append(self, x)

class data_overrider(sub):
    cla = repeater()



