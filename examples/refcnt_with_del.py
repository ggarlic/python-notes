class Leak(object):
    def __init__(self):
        print "id %d is born" % id(self)

    def __del__(self):
        pass

while True:
    A = Leak()
    B = Leak()
    A.b = B
    B.a = A
    A = None
    B = None
