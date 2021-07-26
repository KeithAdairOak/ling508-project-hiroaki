from enum import Enum, Flag, auto
import os
from gtts import gTTS
from io import BytesIO


class VerbClass(Enum):
    PREMIER = auto()
    DUEXE = auto()
    TROISE = auto()


class Tense(Enum):
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
        self.lex_entry = ""  # entry
        self.surface_form = ""  # entry


class Gender(Enum):
    singulier = auto()
    pluriel = auto()


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


class PartOfSpeech(Enum):
    adjectif = auto()
    adverbe = auto()
    article = auto()
    conjonction = auto()
    interjection = auto()
    nom = auto()
    préposition = auto()
    pronom = auto()
    verbe = auto()


class LexicalEntry():

    def __init__(self):
        self.form: str
        self.pos: PartOfSpeech
        self.noun_gender: Gender
        self.verb_class: VerbClass
        self.adj_feminin: str
        self.adj_plural: str
        self.adj_feminin_plural: str
        self.definition: str
        self.origin_form: str


def initial():
    a = Tense(1)
    print(a)


def sound(param):

    os.system("gtts-cli '" + param + "' --lang fr | play -t mp3 -")
    return
