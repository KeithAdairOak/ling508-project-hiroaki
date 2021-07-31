import os
from gtts import gTTS


def sound(param):
    filename = param + '.mp3'
    tts = gTTS(text=param, lang='fr')
    tts.save(filename)
    os.system('mpg123 "' + filename + '"')
    os.system('rm "' + filename + '"')
    return
