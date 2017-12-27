'''
filename:xml2txt.py
author:jimchen1218@sina.com

'''
import os    

print(__doc__)

mergefiledir = os.getcwd()+'\\img2xml'
print("mergefiledir:",mergefiledir)
filenames=os.listdir(mergefiledir)
#txt_filename= filenames[0].split('.')[0].split('_')[0]+'.txt'
txt_list= 'list.txt'
print("txt_list:",txt_list)
file_list=open(txt_list,'w')

for filename in filenames:
	print("filename:",filename)
	if 'Boots' in filename:
		file_list.writelines(filename.split('.')[0]+' 1 1 1')
	elif 'Gymshoes' in filename:
		file_list.writelines(filename.split('.')[0]+' 2 1 2')
	elif 'Leathershoes' in filename:
		file_list.writelines(filename.split('.')[0]+' 3 1 3')
	elif 'Leisureshoes' in filename:
		file_list.writelines(filename.split('.')[0]+' 4 1 4')
	elif 'Sandal' in filename:
		file_list.writelines(filename.split('.')[0]+' 5 1 5')
	elif 'Slipper' in filename:
		file_list.writelines(filename.split('.')[0]+' 6 1 6')
	elif 'Coat' in filename:
		file_list.writelines(filename.split('.')[0]+' 7 2 1')
	elif 'Sweater' in filename:
		file_list.writelines(filename.split('.')[0]+' 8 2 2')
	elif 'Bangle' in filename:
		file_list.writelines(filename.split('.')[0]+' 9 3 1')	

	file_list.write('\n')
file_list.close()


txt_trainval= 'trainval.txt'
txt_test= 'test.txt'

file_trainval=open(txt_trainval,'w')
file_test=open(txt_test,'w')

with open(txt_list) as reader, open(txt_trainval, 'w') as writer_trainval, open(txt_test, 'w') as writer_test:
	for index, line in enumerate(reader):
		if index % 10 == 8 or index % 10 == 9:
			writer_test.write(line)
		else:
			writer_trainval.write(line)





reader.close()
writer_trainval.close()
writer_test.close()	





