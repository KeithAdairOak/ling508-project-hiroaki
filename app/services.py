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


class Services:

    @staticmethod
    def pronounce(param):

        filename = param + '.mp3'
        tts = gTTS(text=param, lang='fr')
        tts.save(filename)
#    os.system('mpg123 "' + filename + '"')
#    os.system('rm "' + filename + '"')
        return filename
