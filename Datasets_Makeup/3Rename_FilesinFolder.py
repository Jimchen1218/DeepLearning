'''
filename:rename files 
author:jimchen1218@sina.com
created date:12/28/2017
'''

import os
import gc

prefix_name = "Earrings_Jewelry_"
path = os.getcwd()
print("path:",path)
path_rename=path+"\\8_earrings"

def rename_filelist(path_name):
	for index,file in enumerate(os.listdir(path_name)):
		print("index:",index)
		if os.path.splitext(file)[1] == '.jpg':
			newname=prefix_name+str(index+1)+'.jpg'
			os.rename(os.path.join(path_name,file),os.path.join(path_name,newname))
			print('newname:',newname)

def rename_filelist_prefixadd0(path_name):
	fileslist_in_dir = os.listdir(path_name)
	num_files = len(fileslist_in_dir)
	print('num_files:',num_files)
	s_num_files = len(str(num_files))
	print("s_num_files:",s_num_files)

	for index,file in enumerate(fileslist_in_dir):
		print("index:",index)
		if os.path.splitext(file)[1] == '.jpg':
			s_index = str(index+1)
			newname=prefix_name+s_index.zfill(s_num_files)+'.jpg'
			os.rename(os.path.join(path_name,file),os.path.join(path_name,newname))
			print('newname:',newname)
			
if __name__ == '__main__':
	#rename_filelist(path_rename)
	rename_filelist_prefixadd0(path_rename)
	gc.collect()


