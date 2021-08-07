from typing import List

from db.repository import *
import mysql.connector
from model.generators import LexicalEntry, LexicalEntries


class MysqlRepository(Repository):

    def __init__(self):
        config = {
            'user': 'root',
            #            'password': 'sakila',
            #            'host': 'mysql',  # When you run this on your machine change it to 'localhost'
            #            'port': '3306',  # When you run this on your machine change it to '32000'
            'password': 'root',
            'host': 'localhost',  # When you run this on your machine change it to 'localhost'
            'port': '32000',  # When you run this on your machine change it to '32000'
            'database': 'french_words'
        }
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def mapper(self, entry: dict) -> LexicalEntry:
        lexical_entry = LexicalEntry()
        #
        lexical_entry.entry = entry["entry"]
        lexical_entry.form = entry["form"]
        lexical_entry.pos = entry["pos"]
        lexical_entry.origin_form = entry["origin_form"]
        #        lexical_entry.noun_gender=entry.get(entry),
        #        lexical_entry.noun_declension=self.map_noun_declension(entry),
        #        lexical_entry.chapter=entry.get('chapter'))
        return lexical_entry

    def select_lexicon(self, param) -> LexicalEntries:
        cond = '"' + param + '"'
        sql = ("SELECT * from lexicon where entry = " + cond)

        self.cursor.execute(sql)
        entries = [{"id": id,
                    "entry": entry,
                    "form": form,
                    "pos": pos,
                    "gender": gender,
                    "verb_class": verb_class,
                    "form_f": adj_f,
                    "form_p": adj_p,
                    "form_fp": adj_fp,
                    "definition": definition,
                    "origin_form": origin_form
                    } for (id, entry, form, pos, gender, verb_class, adj_f,
                           adj_p, adj_fp, definition, origin_form) in self.cursor]

        return [self.mapper(entry) for entry in entries]

    def insert_lexicon(self, entries) -> None:
        for entry in entries:
            sql = ('INSERT INTO lexicon '
                   '(entry, '
                   'form, '
                   'pos, '
                   'gender, '
                   'verb_class, '
                   'form_f, '
                   'form_p, '
                   'form_fp, '
                   'definition, '
                   'origin_form)'
                   'VALUES (' +
                   '"' + entry.entry + '",' +
                   '"' + entry.form + '",' +
                   '"' + entry.pos + '",' +
                   '""'  # entry.noun_gender
                   + ',' +
                   '""'  # entry.verb_class
                   + "," +
                   '""'  # entry.adj_f + "," +
                   + "," +
                   '""'  # entry.adj_p + "," +
                   + "," +
                   '""'  # entry.adj_fp
                   + "," +
                   '""'  # entry.definition
                   + "," +
                   '"' + entry.origin_form + '")')
            self.cursor.execute(sql)
            self.connection.commit()
