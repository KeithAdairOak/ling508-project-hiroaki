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
    origin_lang = str
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


        l_obj = Larousse(param)
        bs = l_obj.get_content().find("div", {"class":"Zone-Entree1 header-article"})
        entries, origin_form, origin_lang = add_entry(bs, param, entries, origin_form, origin_lang)

        for bs in l_obj.get_content().find_all("div", {"class":"Zone-Entree header-article"}):
            entries, origin_form, origin_lang = add_entry(bs, param, entries, origin_form,origin_lang)
        print("\nretrieved from web")

        MySQL.insert_lexicon(entries)

    return entries


def add_entry(bs, param, entries, origin_form, origin_lang) -> (LexicalEntries, str):


    entry = LexicalEntry()
    entry.entry = param

    form = bs.find("h2")
    form.find("span").decompose()
    form.find("audio").decompose()
    entry.form = re.sub("\n", "", form.get_text())

    pos = bs.find("p", {"class": "CatgramDefinition"})
#        pos.find("a",{"class": "lienconj"}).decompose()
    mco = pos.get_text().split(" ")
   #     mco = re.match("(^.+?) (.+?) ", pos.get_text())
    entry.pos = mco[0]
    if entry.pos == "verbe":
        set_verb_class(entry)
    if entry.pos == "nom":
        try:
            entry.noun_gender = mco[1]
        except IndexError:
            entry.noun_gender = ""

#        elif i == 1:
 #           extra = m
#        elif i == 3:
  #          extra2 = m
#        re.sub(" (.+)", "", pos.get_text())

    check_origin_form = bs.find("p", {"class": "OrigineDefinition"})
    if check_origin_form:
        italic_form = check_origin_form.find("i").get_text()
        origin_lang = ""
        origin_form = check_origin_form.get_text()
        origin_form = re.sub("^\(", "", origin_form)
        origin_form = re.sub("\)$", "", origin_form)
        for c in origin_form.split(" "):
            origin_lang = origin_lang + " " + c
            if italic_form in origin_lang:
                origin_lang = re.sub("^ ", "", origin_lang).replace(italic_form,"")
                origin_lang = " ".join([_ for _ in origin_lang.split(" ") if re.match("\w+", _)])
                entry.origin_lang = origin_lang
                break
            
        origin_form = re.sub(origin_lang + " ", "", origin_form)
        entry.origin_form = origin_form
#            set_verb_class(entry)

    if [_ for _ in entries if _.pos == entry.pos and _.form == entry.form]:
        pass
    else:
        entry.origin_lang = origin_lang
        entry.origin_form = origin_form
        entries.append(entry)
    return entries, origin_form, origin_lang


def set_verb_class(entry):
    try:
        html = urlopen("https://la-conjugaison.nouvelobs.com/du/verbe/" + entry.form + ".php")
    except Exception as e:
        print("\nError:", e)
        return []
    bs2 = BeautifulSoup(html.read(), 'html.parser')
    grammar_desc = bs2.find("div", {"class": "bloc"}).get_text()
    pos_verbclass = re.match("^.* du ([123]).* groupe", grammar_desc).groups()
#    entry.pos = pos_verbclass[0]
    entry.verb_class = pos_verbclass[0]
