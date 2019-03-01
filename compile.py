import os
from PIL import Image
os.chdir(r'C:\Users\james_000\Documents\GitHub\gentlegiantJGC.github.io')
with open('main.jgc', 'r') as mainf:
	main = mainf.read()
main = main.split('\n')
dataDivNum = [i for i, s in enumerate(main) if '<div class="data"></div>' in s]
if len(dataDivNum) != 1:
	raise Exception()
else:
	dataDivNum = dataDivNum[0]
dataTabNum = len(main[dataDivNum])-len(main[dataDivNum].lstrip('\t'))

for dirpath, dirnames, filenames in os.walk('.'):
	if 'addon' in dirpath or dirpath.split(os.sep)[-1] in ['css','.git','mainIcons']:
		continue
	elif 'list.jgc' in filenames:
		with open(os.path.join(dirpath, 'list.jgc'), 'r') as dataf:
			data = dataf.read()
		data = data.split('\n')
		element = '{}<div class="data">\n'.format(dataTabNum * '\t')
		for n in range(len(data)):
			if n%2 == 0:
				side = 'left'
			else:
				side = 'right'
			path, title, desc = data[n].split(';')
			element += '{}<div class="dataline{}">\n'.format((dataTabNum+1) * '\t', side)
			element += '{}<a class="elementlink" href="/{}"></a>\n'.format((dataTabNum+2) * '\t', path)
			if 'thumb.jpg' in os.listdir('./{}'.format(path)):
				thumbs = [a for a in os.listdir('./{}'.format(path)) if a.startswith('thumb') and a.endswith('.jpg')]
				if len(thumbs) > 1:
					for thumb in thumbs:
						if thumb != 'thumb.jpg':
							os.remove(os.path.join(path, thumb))
				thumbs = []
				thumb = Image.open(os.path.join(path, 'thumb.jpg'))
				width, height = thumb.size
				while width > 100:
					thumb2 = thumb.copy()
					thumb2.thumbnail((width, height))
					thumb2.save(os.path.join(path, 'thumb{}.jpg'.format(width)), "JPEG", quality=60, optimize=True)
					thumbs.append(['thumb{}.jpg'.format(width), width])
					width = int(width/1.5)
				thumbs.reverse()
				if len(thumbs) > 0:
					element += '{}<img class="elementimg" src="/{}/thumb.jpg" alt="{}" srcset="{}" />\n'.format(
						(dataTabNum + 3) * '\t',
						path, path,
						', '.join(['/{}/{} {}w'.format(path, a[0], a[1]*2) for a in thumbs]))
				else:
					raise Exception('failed creating thumbs at {}'.format(path))
			else:
				raise Exception('no thumb.jpg given at {}'.format(path))
			element += '{}<div class="elementdescript">\n'.format((dataTabNum+2) * '\t')
			
			element += '{}<b class="descriptTitle">{}</b>\n'.format((dataTabNum+3) * '\t', title)
			element += '{}<p class="descriptMain">{}</p>\n'.format((dataTabNum+3) * '\t', desc)

			element += '{}</div>\n'.format((dataTabNum+2) * '\t')
			
			element += '{}</div>\n'.format((dataTabNum+1) * '\t')
		element += '{}</div>'.format(dataTabNum * '\t')
		
		maintemp = main
		maintemp[dataDivNum] = element
		maintemp = '\n'.join(maintemp)
		
		print(dirpath)
		index = open(dirpath+os.sep+'index.html', 'w')
		index.write(maintemp)
		index.close()
	elif 'data.jgc' in filenames:
		with open(dirpath + os.sep + 'data.jgc', 'r') as dataf:
			data = dataf.read()
		data = data.split('\n')
		for n in range(len(data)):
			data[n] = dataTabNum * '\t'+data[n]
		data = '\n'.join(data)
		
		maintemp = main
		maintemp[dataDivNum] = data
		maintemp = '\n'.join(maintemp)
		
		print(dirpath)
		index = open(dirpath+os.sep+'index.html', 'w')
		index.write(maintemp)
		index.close()
		
	# else:
		# index = open(dirpath+os.sep+'index.html', 'w')
		# index.write('under construction')
		# index.close()