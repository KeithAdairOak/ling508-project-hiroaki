from app.French import *

def test_initial(param):
    initial()
    sound("Je peux parler en français,")
    sound("mais je ne suis pas française.")

    print(repr(Tense.PASSsimple))
