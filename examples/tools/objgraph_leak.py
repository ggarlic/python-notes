import objgraph

class Leak(object):
    def __init__(self):
        print "id %d is born" % id(self)

    def __del__(self):
        pass

for i in xrange(10):
    A = Leak()
    B = Leak()
    A.b = B
    B.a = A
    A = None
    B = None
    objgraph.show_growth()
