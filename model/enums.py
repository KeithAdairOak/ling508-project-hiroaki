import enum

class Person(enum):
    PRE = "Première personne"
    DEU = "Deuxième personne"
    TRO = "Troisième personne"


class VerbClass(enum):
    PRE = "Premier groupe"
    DEU = "Deuxième groupe"
    TRO = "Troisième groupe"


class Tense(enum):
    PRE = "Présent"
    IMP = "Imparfait"
    FUT = "Futur"
    PSS = "Passé simple"
    PSC = "Passé composé"
    PQP = "Plus‐que‐parfait"
    PAN = "Passé antérieur"
    FAN = "Futur antérieur"


class Mood(enum):
    IND = "Indicatif"
    SUB = "Subjonctif"
    CON = "Conditionnel"
    IMP = "Impératif"


class Aspect(enum):
    ACC = "Accompli"
    NAC = "Non accompli"


class Voice(enum):
    ACT = "Voix active"
    PAS = "Voix passive"
    PRO = "Voix pronominale"


class Number(enum):
    S = "Singulier"
    P = "Pluriel"


class Gender(enum):
    M = "Masculin"
    F = "Féminin"


class PartOfSpeech(enum):
    ADJ = "adjectif"
    ADV = "adverbe"
    ATC = "article"
    CON = "conjonction"
    INT = "interjection"
    NOM = "nom"
    PRE = "préposition"
    PRO = "pronom"
    VRB = "verbe"


