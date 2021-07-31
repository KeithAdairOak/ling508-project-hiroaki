import abc
from model.generators import LexicalEntry


class Repository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def load_lexicon(self) -> list[LexicalEntry]:
        raise NotImplementedError
