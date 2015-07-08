from guppy import hpy
hp = hpy()
h1 = hp.heap()
l = [range(i) for i in xrange(2**10)]
h2 = hp.heap()
print (h2-h1).bytype
print (h2-h1).bysize
