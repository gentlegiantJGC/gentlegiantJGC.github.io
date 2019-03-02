import os
from PIL import Image

def create_mip_map(img_path):
	if os.path.isfile(img_path):
		img_folder, img_extension = os.path.splitext(img_path)
		img_folder = img_folder.split(os.sep)
		img_name = img_folder[-1]
		path = os.sep.join(img_folder[:-1])
		path = os.path.relpath(path).replace('\\', '/')

		thumbs = []
		thumb = Image.open(img_path)
		width, height = thumb.size
		while width > 100:
			thumb2 = thumb.copy()
			thumb2.thumbnail((width, height))
			thumb2.save(os.path.join(path, '{}{}.jpg'.format(img_name, width)), "JPEG", quality=75, optimize=True)
			thumbs.append(['{}{}.jpg'.format(img_name, width), width])
			width = int(width / 1.5)
		thumbs.reverse()
		if len(thumbs) > 0:
			print('<img src="/{}/{}{}" alt="{}" srcset="{}" />\n'.format(path, img_name, img_extension, path,
				', '.join(['/{}/{} {}w'.format(path, a[0], a[1]) for a in thumbs])))
		else:
			raise Exception('failed creating thumbs at {}'.format(path))
	else:
		print('"{}" is not a valid file'.format(img_path))

create_mip_map(r"C:\Users\james_000\Documents\GitHub\gentlegiantJGC.github.io\ASOUE\cover.jpg")