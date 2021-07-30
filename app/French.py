from enum import Enum
from gtts import gTTS
import os


class Person(Enum):
    PRE = "Première personne"
    DEU = "Deuxième personne"
    TRO = "Troisième personne"


class VerbClass(Enum):
    PRE = "Premier groupe"
    DEU = "Deuxième groupe"
    TRO = "Troisième groupe"


class Tense(Enum):
    PRE = "Présent"
    IMP = "Imparfait"
    FUT = "Futur"
    PSS = "Passé simple"
    PSC = "Passé composé"
    PQP = "Plus‐que‐parfait"
    PAN = "Passé antérieur"
    FAN = "Futur antérieur"


class Mood(Enum):
    IND = "Indicatif"
    SUB = "Subjonctif"
    CON = "Conditionnel"
    IMP = "Impératif"


class Aspect(Enum):
    ACC = "Accompli"
    NAC = "Non accompli"


class Voice(Enum):
    ACT = "Voix active"
    PAS = "Voix passive"
    PRO = "Voix pronominale"


class Number(Enum):
    S = "Singulier"
    P = "Pluriel"


class Gender(Enum):
    M = "Masculin"
    F = "Féminin"


class PartOfSpeech(Enum):
    ADJ = "adjectif"
    ADV = "adverbe"
    ATC = "article"
    CON = "conjonction"
    INT = "interjection"
    NOM = "nom"
    PRE = "préposition"
    PRO = "pronom"
    VRB = "verbe"


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
        self.adj_f: str
        self.adj_p: str
        self.adj_fp: str
        self.definition: str
        self.origin_form: str


def sound(param):
    filename = param + '.mp3'
    tts = gTTS(text=param, lang='fr')
    tts.save(filename)
    os.system('mpg123 "' + filename + '"')
    os.system('rm "' + filename + '"')
    return
