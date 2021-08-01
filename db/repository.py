import abc
from model.generators import LexicalEntries


class Repository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def select_lexicon(self, param) -> LexicalEntries:
        raise NotImplementedError
