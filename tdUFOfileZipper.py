from mojo.events import addObserver
import os
import shutil

__doc__ = """
The script runs after saving the file and packs it into a zip archive. The previous version of the zip archive is copied with the "bek" suffix. In this way, you always have the current saved version of the ufo file in the zip archive and the second previous copy.
"""


class UFOFileZipper(object):
	def __init__(self):		
		addObserver(self, "zippUFO", "fontDidSave")
		print ('*' * 80)
		print ('UFOfileZipper service is started...')
		self.savecount = 0

				
	def zippUFO(self, info):
		font = info['font']
		fontpath = info['path']
		zippath = fontpath + '.zip'
		backzippath = fontpath + '.back.zip'
		
		if os.path.exists(zippath):
			shutil.copyfile(zippath, backzippath)		
						
		print ('Making zip for:', font.info.familyName, font.info.styleName)
		print ('\tcurrent version:', zippath.split('/')[-1])
		shutil.make_archive(fontpath, 'zip', fontpath)
		print ('\tprevious version:', backzippath.split('/')[-1])
		self.savecount += 1

				
UFOFileZipper()