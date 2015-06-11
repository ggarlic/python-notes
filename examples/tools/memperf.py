from memory_profiler import profile
from memory_profiler import memory_usage
import time

 
@profile
def my_func():
    b = [0] * (2 * 10 ** 7)
    del b

 
def cur_python_mem():
    mem_usage = memory_usage(-1, interval=0.2, timeout=1)
    return mem_usage

 
@profile
def f(a, n=100):
    time.sleep(1)
    b = []
    for i in range(n):
        b.append(a)
    time.sleep(1)
    return b

if __name__ == '__main__':
    a = my_func()
    print cur_python_mem()
    print memory_usage((f, (1,), {'n': int(1e6)}), interval=0.5)
    "mprof run --python python memperf.py -f 100 100 -s 100 100 10"
