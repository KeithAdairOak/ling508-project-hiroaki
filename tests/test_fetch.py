
from app.services import Services

s = Services()

def test_fetch():
    vb = VerbClass
    assert vb.DEU.value == "Deuxième groupe"
    p = Person
    assert p.TRO.value == "Troisième personne"

    entries = s.fetch("aimer")



    print("\n", [(_.entry, _.form, _.pos, _.verb_class, _.noun_gender, _.origin_form, _.origin_lang) for _ in entries[:1]])
#    assert len(entries) == 3




    entries = s.fetch("cheval")
    print("\n", [(_.entry, _.form, _.pos, _.verb_class, _.noun_gender, _.origin_form, _.origin_lang) for _ in entries[:1]])

 #   assert len(entries) == 2

    entries = s.fetch("difficile")
    print("\n", [(_.entry, _.form, _.pos, _.verb_class, _.noun_gender, _.origin_form, _.origin_lang) for _ in entries[:1]])

  #  assert len(entries) == 2
    entries = s.fetch("cet")
    print("\n", [(_.entry, _.form, _.pos, _.verb_class, _.noun_gender, _.origin_form, _.origin_lang) for _ in entries[:1]])

    entries = s.fetch("etre")