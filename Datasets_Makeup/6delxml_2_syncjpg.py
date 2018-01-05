import os
import sys
import re

xml_subdir_path = "\\annotations\\xmls\\"
jpg_subdir_path = "\\images\\"
jpg_suffix = ".jpg"
xml_suffix = ".xml"

def checkIsExist(fullpath):
	fullpath=fullpath.strip()
	if(not os.path.exists(fullpath)):
		print("CheckIsExist file is not exist!")
		return False
	else:
		return True

def DelFile(full_path):
	full_path=full_path.strip()
	if(os.path.exists(full_path)):
		os.remove(full_path)
		print("DelFile file has deleted!\n full_path:",full_path)
	return True


def del_xml():
	paths=[]
	cwd_dir = os.getcwd()
	print("del_xml cwd_dir:",cwd_dir)
	
	xml_dir_path = cwd_dir + xml_subdir_path
	print("del_xml xml_dir_path:",xml_dir_path)
	jpg_dir_path = cwd_dir + jpg_subdir_path
	print("del_xml jpg_dir_path:",jpg_dir_path)
	
	xmllistdir = os.listdir(xml_dir_path)
	print("del_xml \nxmllistdir:",xmllistdir)
	for path_name in xmllistdir:
		#if path_name.endswith('txt'):
			#filefullpath = os.path.join(xml_dir_path, file_name)
		paths.append(path_name)
  		
	totalnum_files = len(paths)
	print("del_xml totalnum_files:",totalnum_files)
	
	for i in range(totalnum_files):
		filename = paths[i].split('.')[0]
		pulljpgpath= jpg_dir_path + filename + jpg_suffix
		print("\ndel_xml \npulljpgpath:",pulljpgpath)
		if not checkIsExist(pulljpgpath):
			print("del_xml file is not exist,need to delete!")
			pullxmlpath = xml_dir_path + filename + xml_suffix
			print("del_xml \npullxmlpath:",pullxmlpath)
			DelFile(pullxmlpath)
		
def main():
	del_xml()
	print("main del_xml Finished!!!")	

if __name__ == "__main__":
	main()
	
	



