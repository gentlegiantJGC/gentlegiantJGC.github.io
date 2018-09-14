import os
from PIL import Image

def createMipMap(imgPath):
	if os.path.isfile(imgPath):
		imgFolder, imgExtension = os.path.splitext(imgPath)
		imgFolder = imgFolder.split(os.sep)
		imgName = imgFolder[-1]
		path = os.sep.join(imgFolder[:-1])
		path = os.path.relpath(path).replace('\\', '/')

		thumbs = []
		thumb = Image.open(imgPath)
		width, height = thumb.size
		while width > 100:
			thumb2 = thumb.copy()
			thumb2.thumbnail((width, height))
			thumb2.save(os.path.join(path, '{}{}.jpg'.format(imgName, width)), "JPEG", quality=75, optimize=True)
			thumbs.append(['{}{}.jpg'.format(imgName, width), width])
			width = int(width / 1.5)
		thumbs.reverse()
		if len(thumbs) > 0:
			print '<img src="/{}/{}{}" alt="{}" srcset="{}" />\n'.format(path, imgName, imgExtension, path,
				', '.join(['/{}/{} {}w'.format(path, a[0], a[1]) for a in thumbs]))
		else:
			raise Exception('failed creating thumbs at {}'.format(path))
	else:
		print '"{}" is not a valid file'.format(imgPath)

createMipMap(r"C:\Users\james_000\Documents\GitHub\gentlegiantJGC.github.io\gamemodeone\marketplace\cover.jpg")