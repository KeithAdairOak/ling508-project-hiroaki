from enum import Enum,Flag, auto

class Verbclass(Enum):
    PREMIER = auto()
    DUEXE = auto()
    TROISE = auto()

class Tence(Enum):
    PRES = auto()
    IMPARF = auto()
    FUTUR = auto()
    PASSsimple = auto()
    Passécomposé = auto()
    Plusqueparfait = auto()
    Passéantérieur = auto()
    Futurantérieur = auto()


class Word():

    def __init__(self):
        self.lex_entry = entry
        self.surface_form = entry



class Noun(Word):

    def __init__(self):
        self.number = ""
        self.gender = ""

class Verb(Word):

    def __init__(self):
        self.person = ""
        self.number = ""
        self.tense = ""
        self.voice = ""
        self.mood = ""
        self.aspect = ""

def initial():
    a = Tence(1)
    print(a)