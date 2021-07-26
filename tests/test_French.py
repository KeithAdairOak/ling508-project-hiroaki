from app.French import *


def test(param):
    sound("Je peux parler en français,")
    sound("mais je ne suis pas française.")

    vb = VerbClass
    assert vb.descrition[1] == "Deuxième groupe"


#   print(repr(Tense.PASSsimple))

test("aimer")
