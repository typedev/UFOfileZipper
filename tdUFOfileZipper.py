from mojo.events import addObserver
import os
import shutil

# dropboxdir = '/Users/alexander/Dropbox/UFOfileZipper'
# copyUFOZIP2dropbox = False

# def printDBsize(path = dropboxdir):
# 	total_size = 0
# 	filecount = 0
# 	for dirpath, dirnames, filenames in os.walk(path):
# 		for i in filenames:
# 			if i.endswith('.zip'):
# 				f = os.path.join(dirpath, i)
# 				total_size += os.path.getsize(f)
# 				filecount +=1
# 	total_size = round((total_size / 1000) / 1000, 1)
# 	if total_size:
# 		print ('*' * 80)
# 		print ('Archives of %i ufo files take %s MB in the DropBox folder.' % (filecount, str(total_size)))
# 		print ('Don\'t forget to delete unnecessary files...')
# 		print ('*' * 80)


class UFOFileZipper(object):
		
	def __init__(self):		
		addObserver(self, "zippUFO", "fontDidSave")
		print ('*' * 80)
		print ('UFOfileZipper service is started...')
		# printDBsize(dropboxdir)
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
		# if copyUFOZIP2dropbox:
		# 	print ('\tPlacing copy to Dropbox...')
		# 	shutil.copy(zippath, dropboxdir)
		# 	print ('Done.')
		# self.savecount += 1
		# if self.savecount == 10:
		# 	printDBsize(dropboxdir)
		# 	self.savecount = 0
				
UFOFileZipper()