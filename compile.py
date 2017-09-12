import os
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

# for dirpath, dirnames, filenames in os.walk('.'):
	# if dirpath == '.'

for dirpath, dirnames, filenames in os.walk('.'):
	if 'addon' in dirpath:
		continue
	if dirpath.split(os.sep)[-1] in ['css','.git','mainIcons']:
		continue
	elif 'list.jgc' in filenames:
		with open(dirpath + os.sep + 'list.jgc', 'r') as dataf:
			data = dataf.read()
		data = data.split('\n')
		element = dataTabNum * '\t'+'<div class="data">\n'
		for n in range(len(data)):
			if n%2 == 0:
				side = 'left'
			else:
				side = 'right'
			path, title, desc = data[n].split(';')
			element += (dataTabNum+1) * '\t'+'<div class="dataline'+side+'">\n'
			element += (dataTabNum+2) * '\t'+'<a class="elementlink" href="/'+path+'"></a>\n'
			element += (dataTabNum+2) * '\t'+'<img class="elementimg" src="/'+path+'/thumb.png" alt="'+path+'" />\n'
			element += (dataTabNum+2) * '\t'+'<div class="elementdescript">\n'
			
			element += (dataTabNum+3) * '\t'+'<b class="descriptTitle">'+title+'</b>\n'
			element += (dataTabNum+3) * '\t'+'<p class="descriptMain">'+desc+'</p>\n'

			element += (dataTabNum+2) * '\t'+'</div>\n'
			
			element += (dataTabNum+1) * '\t'+'</div>\n'
		element += dataTabNum * '\t'+'</div>'
		
		maintemp = main
		maintemp[dataDivNum] = element
		maintemp = '\n'.join(maintemp)
		
		print dirpath
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
		
		print dirpath
		index = open(dirpath+os.sep+'index.html', 'w')
		index.write(maintemp)
		index.close()
		
	# else:
		# index = open(dirpath+os.sep+'index.html', 'w')
		# index.write('under construction')
		# index.close()