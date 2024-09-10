
class Message:

    message = None

    def __init__(self, message):
        self.message = message

    def getMessage(self):
        return self.message


class Subject:

    # call attach() to add observers to the observer list
    def attach(self, observer):
        pass
    # call detach() to remove observers from the observer list

    def detach(self, observer):
        pass
    # call notify() to publish all the changes made by the subject

    def notify(self, message):
        pass


class Observer:

    def update(self, m):
        pass

# concrete class inherits the base class


class ConcreteSubject(Subject):

    observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)

# individual child observers inherits the parent observer class


class ObserverA(Observer):
    def update(self, m):
        print("observerA: " + m.getMessage())


class ObserverB(Observer):
    def update(self, m):
        print("observerB: " + m.getMessage())


class ObserverC(Observer):
    def update(self, m):
        print("observerC: " + m.getMessage())


class Demo:
    @staticmethod
    def main(args):

        a = ObserverA()
        b = ObserverB()
        c = ObserverC()

        publisher = ConcreteSubject()

        publisher.attach(a)
        publisher.attach(b)
        publisher.notify(Message("First update\n"))
        publisher.attach(c)
        publisher.detach(b)
        publisher.notify(Message("Second update\n"))


if __name__ == "__main__":
    Demo.main([])
