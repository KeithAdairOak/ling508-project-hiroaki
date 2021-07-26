from enum import Enum, Flag, auto
import os
from gtts import gTTS
from io import BytesIO

class Common(Enum):
    def description(self,dic):
        return self.dic[self.value]

class Person(Common):
    PREMIER = auto()
    DEUXIÈME = auto()
    TROISIÈME = auto()

    def __init__(self, dic):
        dic = {1: "Première personne",
               2: "Deuxième personne",
               3: "Troisième personne"}
        self.dic = dic




class VerbClass(Enum):
    PREMIER = auto()
    DEUXIÈME = auto()
    TROISIÈME = auto()

    def __init__(self, dic):
        dic = {1: "Premier groupe",
               2: "Deuxième groupe",
               3: "Troisième groupe"}
        self.dic = dic

class Tense(Enum):
    PRES = auto()
    IMPARF = auto()
    FUTUR = auto()
    PASS = auto()
    PASCOM = auto()
    PLUSQPARF = auto()
    PASSANT = auto()
    FUTURANT = auto()

    def __init__(self, dic):
        dic = {1: "Présent",
               2: "Imparfait",
               3: "Futur",
               4: "Passé simple",
               5: "Passé composé",
               6: "Plus‐que‐parfait",
               7: "Passé antérieur",
               8: "Futur antérieur"}
        self.dic = dic


class Mood(Enum):
    INDICATIF = auto()
    SUBJONCTIF = auto()
    CONDITIONNEL = auto()
    IMPÉRATIF = auto()

    def __init__(self, dic):
        dic = {1: "Indicatif",
               2: "Subjonctif",
               3: "Conditionnel",
               4: "Impératif"}
        self.dic = dic


class Aspect(Enum):
    ACCOMPLI = auto()
    NONACOMPLI = auto()

    def __init__(self, dic):
        dic = {1: "Accompli",
               2: "Non accompli"}
        self.dic = dic

class Voice(Enum):
    ACTIF = auto()
    PASSIF = auto()
    PRONOMINAL = auto()

    def __init__(self, dic):
        dic = {1: "Voix active",
               2: "Voix passive",
               3: "Voix pronominale"}
        self.dic = dic

class Number(Enum):
    SINGULIER = auto()
    PLURIEL = auto()

    def __init__(self, dic):
        dic = {1: "Singulier",
               2: "Pluriel"}
        self.dic = dic

class Gender(Enum):
    MASCULIN = auto()
    FÉMININ = auto()

    def __init__(self, dic):
        dic = {1: "Masculin",
               2: "Féminin"}
        self.dic = dic


class Word:

    def __init__(self, param):
        self.surface_form = param

        self.lex_entry = ""  # entry


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


def sound(param):
    os.system("gtts-cli '" + param + "' --lang fr | play -t mp3 -")
    return
