from app.services import Services
import os


# pronounce("mais je ne suis pas française.")
filepath = pronounce()
os.system('mpg123 "' + filepath + '"')
os.system('rm "' + filepath + '"')
