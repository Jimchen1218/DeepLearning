'''
filename:rename files 
author:jimchen1218@sina.com
created date:12/28/2017
'''

import os
import gc



def rename_filelist(path_name):
	prefix_name = ""
	path = os.getcwd()
	print("path:",path)
	path_rename=path+"\\"
	for index,file in enumerate(os.listdir(path_name)):
		print("index:",index)
		if os.path.splitext(file)[1] == '.jpg':
			newname=prefix_name+str(index+1)+'.jpg'
			os.rename(os.path.join(path_name,file),os.path.join(path_name,newname))
			print('newname:',newname)

def rename_filelist_prefixadd0(path_name):
	prefix_name = ""
	path = os.getcwd()
	print("path:",path)
	path_rename=path+"\\"	
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
		
		

	
def rename_filelist_replacename():
	prefix_oldname = "TShirt"
	prefix_newname = "Tshirt"
	prefix_pathname = "xml\\"
	curpath = os.getcwd()
	
	path_fullname=curpath+prefix_pathname
	print("path_fullname:",path_fullname)
	for index,filename in enumerate(os.listdir(path_fullname)):
		print("rename_filelist_replacename filename:",filename)
		short_filename= filename.split('.')[0]
		print("rename_filelist_replacename short_filename:",short_filename)
		if prefix_oldname in short_filename:
			short_filename.replace(prefix_oldname,prefix_newname)
			print("rename_filelist_replacename short_filename:",short_filename)
			newname = os.rename(os.path.join(path_fullname,filename),os.path.join(path_fullname,short_filename))
			print('newname:',newname)
			
			
if __name__ == '__main__':
	#rename_filelist(path_rename)
	#rename_filelist_prefixadd0(path_rename)
	rename_filelist_replacename()
	gc.collect()


