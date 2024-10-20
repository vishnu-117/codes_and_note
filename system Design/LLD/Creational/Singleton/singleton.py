class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        self.value = None

# Testing Singleton
singleton1 = Singleton()
singleton2 = Singleton()

singleton1.value = 100
print(singleton2.value)  # 100: Both are the same instance
print(singleton1 is singleton2)  # True
