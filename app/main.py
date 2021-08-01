import os
import re
import db
from db.repository import *
from db.mysql_repository import *
from model.generators import *
from gtts import gTTS
from app.larousse import Larousse

MySQL = MysqlRepository()


def sound(param):
    filename = param + '.mp3'
    tts = gTTS(text=param, lang='fr')
    tts.save(filename)
    os.system('mpg123 "' + filename + '"')
    os.system('rm "' + filename + '"')
    return


def fetch(param) -> LexicalEntries:
    origin_form = str
    entries = MySQL.select_lexicon(param)
    if entries:
        print("\nretrieved from db")
        pass
    else:

        l_obj = Larousse(param)
        bs = l_obj.get_content().find("div", {"class":"Zone-Entree1 header-article"})
        entries, origin_form = add_entry(bs, param, entries, origin_form)

        for bs in l_obj.get_content().find_all("div", {"class":"Zone-Entree header-article"}):
            entries, origin_form = add_entry(bs, param, entries, origin_form)
        print("\nretrieved from web")

        MySQL.insert_lexicon(entries)

    return entries


def add_entry(bs, param, entries, origin_form) -> (LexicalEntries, str):
        entry = LexicalEntry()
        entry.pos = bs.find("p", {"class": "CatgramDefinition"}).get_text()
        form = bs.find("h2")
        form.find("span").decompose()
        form.find("audio").decompose()
        entry.form = re.sub("\n", "", form.get_text())
        check_origin_form = bs.find("p", {"class": "OrigineDefinition"})
        if check_origin_form:
            origin_form = check_origin_form.find("i").extract().get_text()
            origin_form = origin_form + re.sub(" \)", ")", check_origin_form.get_text())

        if [_ for _ in entries if _.pos == entry.pos and _.form == entry.form]:
            pass
        else:
            entry.entry = param
            entry.origin_form = origin_form
            entries.append(entry)
        return entries, origin_form


