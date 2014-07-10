import random

class Animal(object):
    """An abstract animal."""

    def say(self):
        """Tell what this animal says."""
        sound = getattr(self, 'sound', None)
        if sound is None:
            print('This animal is mute')
        else:
            print('This animal says {}'.format(sound))

class Fish(Animal):
    """A fish."""

class Dog(Animal):
    """A dog."""

    sound = 'Hau hau!'

class Duck(Animal):
    """A duck."""

    @property
    def sound(self):
        return ' '.join(['Kwa!'] * random.radnint(2, 10))

if __name__ == '__main__':
    Fish().say()
    Dog().say()
    Duck().say()
