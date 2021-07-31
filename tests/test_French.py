from app.French import *


def test():
    sound("Je peux parler en français,")
    sound("mais je ne suis pas française.")

    vb = VerbClass
    assert vb.DEU.value == "Deuxième groupe"
    p = Person
    assert p.TRO.value == "Troisième personne"


def sound(param):
    filename = param + '.mp3'
    tts = gTTS(text=param, lang='fr')
    tts.save(filename)
    os.system('mpg123 "' + filename + '"')
    os.system('rm "' + filename + '"')
    return
