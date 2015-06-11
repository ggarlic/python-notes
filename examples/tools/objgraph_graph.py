import objgraph

class Value(object):
    def __init__(self, v):
        object.__init__(self)
        self.v = v
    def get(self):
        return self.v
    def set(self, v):
        self.v = v

class Container(object):
    def __init__(self):
        object.__init__(self)
        self.children = []
    def get(self, idx):
        return self.children[idx]
    def pop(self):
        c = self.children.pop()
        return c
    def push(self, c):
        return self.children.append(c)

if __name__== '__main__':
    c1 = Container()
    c1.push(Value(100))

    objgraph.show_backrefs([c1.get(0)], filename='backref.png')

    c1 = Container()
    v = Value(c1)
    c1.push(v) #circular reference

    objgraph.show_backrefs([c1.get(0)], max_depth=5, filename='circular.png')
    objgraph.show_most_common_types()
