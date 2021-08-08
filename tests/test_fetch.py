from app.main import *


def test_fetch():
    vb = VerbClass
    assert vb.DEU.value == "Deuxième groupe"
    p = Person
    assert p.TRO.value == "Troisième personne"

    entries = fetch("aimer")
    print("\n", [(_.entry, _.form, _.verb_class, _.noun_gender, _.origin_form, _.origin_lang) for _ in entries])
    assert len(entries) == 3

    entries = fetch("cheval")
    print("\n", [(_.entry, _.form, _.verb_class, _.noun_gender, _.origin_form, _.origin_lang) for _ in entries])
    assert len(entries) == 2

    entries = fetch("difficile")
    print("\n", [(_.entry, _.form, _.verb_class, _.noun_gender, _.origin_form, _.origin_lang) for _ in entries])
  #  assert len(entries) == 2
    entries = fetch("ce")
    print("\n", [(_.entry, _.form, _.verb_class, _.noun_gender, _.origin_form, _.origin_lang) for _ in entries])
