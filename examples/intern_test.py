'foo' is 'foo'
'foo!' is 'foo!'
print 'foo' + 'bar' is 'foobar' #byte code optimization
print ''.join(['f']) is ''.join(['f'])
print ''.join(['f', 'o', 'o']) is ''.join(['f', 'o', 'o'])
print 'a' * 20 is 'aaaaaaaaaaaaaaaaaaaa'
print 'a' * 21 is 'aaaaaaaaaaaaaaaaaaaaa'
'foooooooooooooooooooooooooooooo' is 'foooooooooooooooooooooooooooooo'

import dis
def a():
    return "foo" + "bar"

dis.dis(a)
