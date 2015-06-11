import gc
gc.disable()
class Leak(object):
    def __init__(self):
        print "id %d is born" % id(self)

while True:
    A = Leak()
    B = Leak()
    A.b = B
    B.a = A
    A = None
    B = None

