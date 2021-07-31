from enum import Enum

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
