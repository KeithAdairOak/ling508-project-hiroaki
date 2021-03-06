from model.enums import *


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


class LexicalEntry:
    def __init__(self):
        self.entry = ""
        self.form = ""
        self.pos = ""#: PartOfSpeech
        self.noun_gender = ""#: Gender
        self.verb_class = ""#: VerbClass
        self.form_f = ""#: str
        self.form_p = ""#: str
        self.form_fp = ""#: str
        self.definition = ""#: str
        self.origin_form = ""#: str
        self.origin_lang = ""#: str


class LexicalEntries:
    def __init__(self):
        self = list(LexicalEntry)
