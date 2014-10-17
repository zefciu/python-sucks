class A(object):
    def __init__(self):
        super(A, self).__init__()
        print('A')

class B(A):
    def __init__(self):
        A.__init__(self)
        print('B')

class C(A):
    def __init__(self):
        super(C, self).__init__()
        print('C')

class D(B, C):
    def __init__(self):
        B.__init__(self)
        C.__init__(self)
        print('D')


if __name__ == '__main__':
    D()
