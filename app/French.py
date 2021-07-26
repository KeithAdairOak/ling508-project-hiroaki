from enum import Enum, Flag, auto
import os
from gtts import gTTS
from io import BytesIO


class Person(Enum):
    PREMIER = auto()
    DEUXIÈME = auto()
    TROISIÈME = auto()

    def __init__(self):
        self.dic = {self.PREMIER: "Première personne",
                    self.DEUXIÈME: "Deuxième personne",
                    self.TROISIÈME: "Troisième personne"}

    def description(self):
        return self.dic[self.value]


class VerbClass(Enum):
    PREMIER = auto()
    DEUXIÈME = auto()
    TROISIÈME = auto()


#   def __init__(self):
#       self.description = {self.PREMIER: "Premier groupe",
#                           self.DEUXIÈME: "Deuxième groupe",
#                           self.TROISIÈME: "Troisième groupe"}


class Tense(Enum):
    PRES = auto()
    IMPARF = auto()
    FUTUR = auto()
    PASS = auto()
    PASCOM = auto()
    PLUSQPARF = auto()
    PASSANT = auto()
    FUTURANT = auto()

    def __init__(self):
        self.description = {self.PRES: "Présent",
                            self.IMPARF: "Imparfait",
                            self.FUTUR: "Futur",
                            self.PASS: "Passé simple",
                            self.PASCOM: "Passé composé",
                            self.PLUSQPARF: "Plus‐que‐parfait",
                            self.PASSANT: "Passé antérieur",
                            self.FUTURANT: "Futur antérieur"}


class Mood(Enum):
    INDICATIF = auto()
    SUBJONCTIF = auto()
    CONDITIONNEL = auto()
    IMPÉRATIF = auto()

    def __init__(self):
        self.description = {self.PRES: "Indicatif",
                            self.PLUSQPARF: "Subjonctif",
                            self.PASSANT: "Conditionnel",
                            self.FUTURANT: "Impératif"}


class Aspect(Enum):
    ACCOMPLI = auto()
    NONACOMPLI = auto()

    def __init__(self):
        self.description = {self.ACCOMPLI: "Accompli",
                            self.NONACOMPLI: "Non accompli"}


class Voice(Enum):
    ACTIF = auto()
    PASSIF = auto()
    PRONOMINAL = auto()

    def __init__(self):
        self.description = {self.ACTIF: "Voix active",
                            self.PASSIF: "Voix passive",
                            self.PRONOMINAL: "Voix pronominale"}


class Word:

    def __init__(self, param):
        self.surface_form = param

        self.lex_entry = ""  # entry


class Number(Enum):
    SINGULIER = auto()
    PLURIEL = auto()

    def __init__(self):
        self.description = {self.SINGULIER: "Singulier",
                            self.PLURIEL: "Pluriel"}


class Gender(Enum):
    MASCULIN = auto()
    FÉMININ = auto()

    def __init__(self):
        self.description = {self.MASCULIN: "Masculin",
                            self.FÉMININ: "Féminin"}


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
