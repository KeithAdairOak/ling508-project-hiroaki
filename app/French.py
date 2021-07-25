from enum import Enum, Flag, auto
from gtts import gTTS
import os


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
        self.lex_entry = ""#entry
        self.surface_form = ""#entry


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


def sound(param):
    # This module is imported so that we can
    # play the converted audio

    # The text that you want to convert to audio

    # Language in which you want to convert
    language = 'fr'

    # Passing the text and language to the engine,
    # here we have marked slow=False. Which tells
    # the module that the converted audio should
    # have a high speed
    myobj = gTTS(text=param, lang=language, slow=False)

    # Saving the converted audio in a mp3 file named
    # welcome
    myobj.save(param + ".mp3")

    # Playing the converted file
    os.system("mpg123 " + param + ".mp3")
    return
