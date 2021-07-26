from enum import Enum
import os


class Person(Enum):
    PREMIER = "Première personne"
    DEUXIÈME = "Deuxième personne"
    TROISIÈME = "Troisième personne"


class VerbClass(Enum):
    PREMIER = "Premier groupe"
    DEUXIÈME = "Deuxième groupe"
    TROISIÈME = "Troisième groupe"


class Tense(Enum):
    PRES = "Présent"
    IMPARF = "Imparfait"
    FUTUR = "Futur"
    PASS = "Passé simple"
    PASCOM = "Passé composé"
    PLUSQPARF = "Plus‐que‐parfait"
    PASSANT = "Passé antérieur"
    FUTURANT = "Futur antérieur"


class Mood(Enum):
    INDICATIF = "Indicatif"
    SUBJONCTIF = "Subjonctif"
    CONDITIONNEL = "Conditionnel"
    IMPÉRATIF = "Impératif"


class Aspect(Enum):
    ACCOMPLI = "Accompli"
    NONACOMPLI = "Non accompli"


class Voice(Enum):
    ACTIF = "Voix active"
    PASSIF = "Voix passive"
    PRONOMINAL = "Voix pronominale"

class Number(Enum):
    SINGULIER = "Singulier"
    PLURIEL =  "Pluriel"


class Gender(Enum):
    MASCULIN = "Masculin"
    FÉMININ =  "Féminin"

class PartOfSpeech(Enum):
    ADJ = "adjectif"
    ADV = "adverbe"
    ATC = "article"
    CONJ = "conjonction"
    INTJ = "interjection"
    NOM = "nom"
    PREP = "préposition"
    PRON = "pronom"
    VERB = "verbe"


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
