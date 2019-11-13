from abc import ABCMeta, abstractmethod


class List(metaclass=ABCMeta):

    def __init__(self):
        pass

    def list(self) -> int:
        print(self.__str__())
        return 0

    def __str__(self):
        return "No implementation this method."


class Create(metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def create(self) -> int:
        raise NotImplementedError()

