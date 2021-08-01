from app.main import *


def test_fetch():
    vb = VerbClass
    assert vb.DEU.value == "Deuxième groupe"
    p = Person
    assert p.TRO.value == "Troisième personne"

    print("\n", [(_.entry, _.form, _.origin_form) for _ in fetch("aimer")])
