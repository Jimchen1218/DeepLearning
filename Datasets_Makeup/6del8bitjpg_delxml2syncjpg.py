import os
import sys
import re


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


def delxmlsyn2img(xml_subdir_path,jpg_subdir_path):
	jpg_suffix = ".jpg"
	xml_suffix = ".xml"
	paths=[]
	cwd_dir = os.getcwd()
	xml_dir_path = cwd_dir + xml_subdir_path
	jpg_dir_path = cwd_dir + jpg_subdir_path
	
	xmllistdir = os.listdir(xml_dir_path)
	for path_name in xmllistdir:
		paths.append(path_name)
  		
	totalnum_files = len(paths)
	print("delxmlsyn2img totalnum_files:",totalnum_files)
	
	for i in range(totalnum_files):
		filename = paths[i].split('.')[0]
		pulljpgpath= jpg_dir_path + filename + jpg_suffix
		if not checkIsExist(pulljpgpath):
			#print("del_xml file is not exist,need to delete!")
			pullxmlpath = xml_dir_path + filename + xml_suffix
			if checkIsExist(pullxmlpath):
				DelFile(pullxmlpath)

def delimgsyn2xml(jpg_subdir_path,xml_subdir_path):
	jpg_suffix = ".jpg"
	xml_suffix = ".xml"
	paths=[]
	cwd_dir = os.getcwd()
	xml_dir_path = cwd_dir + xml_subdir_path
	jpg_dir_path = cwd_dir + jpg_subdir_path
	
	jpglistdir = os.listdir(jpg_dir_path)
	for path_name in jpglistdir:
		paths.append(path_name)
  		
	totalnum_files = len(paths)
	print("delimgsyn2xml totalnum_files:",totalnum_files)
	
	for i in range(totalnum_files):
		filename = paths[i].split('.')[0]
		pullxmlpath= xml_dir_path + filename + xml_suffix
		#print("delimgsyn2xml \npullxmlpath:",pullxmlpath)
		if not checkIsExist(pullxmlpath):
			print("delimgsyn2xml file is not exist,need to delete!")
			pulljpgpath = jpg_dir_path + filename + jpg_suffix
			print("delimgsyn2xml \npulljpgpath:",pulljpgpath)
			DelFile(pulljpgpath)


def del_allnotjpg(subname):
	from PIL import Image	
	cwd_dir = os.getcwd()
	xml_dir_path = cwd_dir + subname
	xmllistdir = os.listdir(xml_dir_path)
	for filename in xmllistdir:
			path_name=xml_dir_path+filename
			#print("del_allnotjpg path_name:",path_name)
			img = Image.open(path_name)
			if img.format != 'JPEG':
					print("del_allnotjpg img.format:",img.format)
					img.close()
					DelFile(path_name)
		
def main():
	delxmlsyn2img("\\annotations\\xml\\","\\images\\")
	#delimgsyn2xml("\\images\\","\\annotations\\xml\\")
	#del_allnotjpg("\\images\\")
	print("main del_xml Finished!!!")	

if __name__ == "__main__":
	main()
	
	



