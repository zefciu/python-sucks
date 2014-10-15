from abc import ABCMeta, abstractmethod

class Duck(object):
    __metaclass__ = ABCMeta

    """An abstract duck."""

    @abstractmethod
    def quack(self):
        """Make a quacking sound."""

class Duffy(object):
    """Duffy - he talks."""

Duck.register(Duffy)

if __name__ == '__main__':
    duffy = Duffy()
    print(isinstance(duffy, Duck))
    duffy.quack()
