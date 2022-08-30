import abc

from aiogram import Dispatcher


class BaseHandler(metaclass=abc.ABCMeta):

    def __init__(self, dp: Dispatcher) -> None:
        self.dp = dp

    @abc.abstractmethod
    def handle(self):
        pass


