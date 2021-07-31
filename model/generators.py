from model.enums import PartOfSpeech, Gender, VerbClass

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
        self.form: str
        self.pos: PartOfSpeech
        self.noun_gender: Gender
        self.verb_class: VerbClass
        self.adj_f: str
        self.adj_p: str
        self.adj_fp: str
        self.definition: str
        self.origin_form: str
