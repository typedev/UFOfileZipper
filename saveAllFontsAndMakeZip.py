import os
import shutil
from mojo import *

def zippUFO (font):
	fontpath = font.path
	zippath = fontpath + '.zip'
	backzippath = fontpath + '.back.zip'

	if os.path.exists(zippath):
		shutil.copyfile(zippath, backzippath)

	print ('Making zip for:', font.info.familyName, font.info.styleName)
	print ('\tcurrent version:', zippath.split('/')[-1])
	shutil.make_archive(fontpath, 'zip', fontpath)
	print ('\tprevious version:', backzippath.split('/')[-1])

for font in AllFonts():
	font.save()
	zippUFO(font)
print (len(AllFonts()), 'fonts saved')