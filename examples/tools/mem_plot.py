import pylab as pl
import numpy as np
from memory_profiler import profile
from memory_profiler import memory_usage
import time

class User(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
      
def f(count):
    data = { }
    for idx in xrange(count):
        data[idx] = User("user%d" % idx, idx)
    s = "\n".join([ u.name for k, u in data.iteritems() ])
    names = s.split("\n")

if __name__ == '__main__':
    mem_usage = memory_usage((f, (100000,)), interval=0.005)
    pl.plot(np.arange(len(mem_usage)) * 0.005, mem_usage, label="do_sth")
    pl.xlabel('Time (in seconds)')
    pl.ylabel('Memory consumption (in MB)')
    pl.show()
