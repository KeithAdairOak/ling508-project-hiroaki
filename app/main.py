import os
import re
import db
from db.repository import *
from db.mysql_repository import *
from model.generators import *
from gtts import gTTS
from app.larousse import Larousse
from urllib.request import urlopen

import bs4.element
from bs4 import BeautifulSoup
import logging
import re

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

        # Here is a logging config if you would like to use it
        logging.basicConfig(filename='scraper.log',
                            encoding='utf-8',
                            level=logging.DEBUG,
                            format='%(asctime)s [%(levelname)s] %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')
        try:
            html = urlopen("https://la-conjugaison.nouvelobs.com/du/verbe/aimer.php")
        except Exception as e:
            print("\nError:", e)
            return []
        bs2 = BeautifulSoup(html.read(), 'html.parser')

        l_obj = Larousse(param)
        bs = l_obj.get_content().find("div", {"class":"Zone-Entree1 header-article"})
        entries, origin_form = add_entry(bs, bs2, param, entries, origin_form)

        for bs in l_obj.get_content().find_all("div", {"class":"Zone-Entree header-article"}):
            entries, origin_form = add_entry(bs, param, entries, origin_form)
        print("\nretrieved from web")

        MySQL.insert_lexicon(entries)

    return entries


def add_entry(bs, bs2, param, entries, origin_form) -> (LexicalEntries, str):
        entry = LexicalEntry()
        grammar_desc = bs2.find("div", {"class": "bloc"}).get_text()
        pos_verbclass = re.match("(^.*) du ([123]).* groupe", grammar_desc).groups()
        entry.pos = pos_verbclass[0]
        entry.verb_class = pos_verbclass[1]

  #      pos = bs.find("p", {"class": "CatgramDefinition"})
#        url = pos.find("a",{"class": "lienconj"}).extract()
#        entry.pos = pos.get_text()
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


