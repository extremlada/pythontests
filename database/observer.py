from abc import ABCMeta, abstractmethod, ABC


class IObservable(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def subscriber(observer):
        """Add an observer to the list of observers"""

    @staticmethod
    @abstractmethod
    def unsubscribe(observer):
        """Remove an observer from the list of observers"""

    @staticmethod
    @abstractmethod
    def notify(observer):
        """Notify all observers"""


class Subject(IObservable):
    def __init__(self):
        self._observers = set()

    def subscriber(self, observer):
        self._observers.add(observer)

    def unsubscribe(self, observer):
        self._observers.remove(observer)

    def notify(self, *args, **kwargs):
        for observer in self._observers:
            observer.notify(self, *args, **kwargs)


class IObserver(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def notify(observable, *args, **kwargs):
        """receive notification from subject"""


class Observer(IObserver):
    def __init__(self, observable):
        observable.subscriber(self)

    def notify(self, observable, *args, **kwargs):
        print("observer triggered", args, kwargs)
