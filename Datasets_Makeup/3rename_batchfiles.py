'''
filename:rename files 
author:jimchen1218@sina.com
created date:1/16/2018
'''

import os
import gc

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
		if os.path.splitext(file)[1] == '.xml':
			s_index = str(index+1)
			newname=prefix_name+s_index.zfill(s_num_files)+'.xml'
			os.rename(os.path.join(path_name,file),os.path.join(path_name,newname))
			print('newname:',newname)
		
def rename_filelist_replacename():
	prefix_oldname = "ClutchHandbag"
	prefix_newname = "Clutchhandbag"
	prefix_pathname="\\"
	curpath = os.getcwd()
	
	path_fullname=curpath+prefix_pathname
	print("path_fullname:",path_fullname)
	for filename in os.listdir(path_fullname):
		#print("rename_filelist_replacename filename:",filename)
		short_filename= filename.split('.')[0]
		suffix_filename= filename.split('.')[-1]
		if prefix_oldname in short_filename:
			short_filename = short_filename.replace(prefix_oldname,prefix_newname)
			#print("rename_filelist_replacename filename:",filename)
			new_filename= short_filename+'.'+suffix_filename
			print("rename_filelist_replacename new_filename:",new_filename)
			os.rename(os.path.join(path_fullname,filename),os.path.join(path_fullname,new_filename))
			
def rename_generate2anotherdir():
	path = os.getcwd()
	imgs = os.listdir(path+"\\imgs\\")
	if os.path.exists('JPEGImages') == False:
		os.mkdir('JPEGImages')
	if os.path.exists('Annotations') == False:
		os.mkdir('Annotations')
	if os.path.exists('ImageSets') == False:
		os.mkdir('ImageSets')
		os.mkdir('ImageSets/Main')
	cnt = 1
	prename = "000000"
	for img in imgs:
		temp=cv2.imread(path+"\\imgs\\"+img)
		#os.remove(path+"\\imgs\\"+img)
		cv2.imwrite(path+"\\JPEGImages\\"+prename[0:len(prename)-len(str(cnt))]+str(cnt)+".jpg",temp)
		print("renamed "+img+" to "+prename[0:len(prename)-len(str(cnt))]+str(cnt)+".jpg")
		cnt+=1
	print('done!')			

def rename_filelist(dirname,prefix_name):
	path = os.getcwd()
	path_name=path+"\\"+dirname
	print("path_name:",path_name)
	
	fileslist_in_dir = os.listdir(path_name)
	num_files = len(fileslist_in_dir)
	print('num_files:',num_files)
	s_num_files = len(str(num_files))
	for index,file in enumerate(fileslist_in_dir):
		print("index:"+str(index)+" file:"+file)
		if os.path.splitext(file)[1] == '.jpg':
			if dirname== "1_1Overcoat":
				newname=prefix_name+"_"+str(index+1).zfill(s_num_files)+'.jpg'
				os.rename(os.path.join(path_name,file),os.path.join(path_name,newname))
				print('newname:',newname)
			elif dirname== "1_2Coat":
				newname=prefix_name+"_"+str(index+1).zfill(s_num_files)+'.jpg'
				os.rename(os.path.join(path_name,file),os.path.join(path_name,newname))
				print('newname:',newname)
			elif dirname== "1_3Sweater":
				newname=prefix_name+"_"+str(index+1).zfill(s_num_files)+'.jpg'
				os.rename(os.path.join(path_name,file),os.path.join(path_name,newname))
				print('newname:',newname)
			elif dirname== "1_4Shirt":
				newname=prefix_name+"_"+str(index+1).zfill(s_num_files)+'.jpg'
				os.rename(os.path.join(path_name,file),os.path.join(path_name,newname))
				print('newname:',newname)
			elif dirname== "1_5Fleece":
				newname=prefix_name+"_"+str(index+1).zfill(s_num_files)+'.jpg'
				os.rename(os.path.join(path_name,file),os.path.join(path_name,newname))
				print('newname:',newname)
			elif dirname== "1_6Tshirt":
				newname=prefix_name+"_"+str(index+1).zfill(s_num_files)+'.jpg'
				os.rename(os.path.join(path_name,file),os.path.join(path_name,newname))
				print('newname:',newname)
			elif dirname== "2_1Tailoredtrousers":
				newname=prefix_name+"_"+str(index+1).zfill(s_num_files)+'.jpg'
				os.rename(os.path.join(path_name,file),os.path.join(path_name,newname))
				print('newname:',newname)
			elif dirname== "2_2Casualtrousers":
				newname=prefix_name+"_"+str(index+1).zfill(s_num_files)+'.jpg'
				os.rename(os.path.join(path_name,file),os.path.join(path_name,newname))
				print('newname:',newname)
			elif dirname== "2_3Jeanstrousers":
				newname=prefix_name+"_"+str(index+1).zfill(s_num_files)+'.jpg'
				os.rename(os.path.join(path_name,file),os.path.join(path_name,newname))
				print('newname:',newname)
			elif dirname== "2_4Sporttrousers":
				newname=prefix_name+"_"+str(index+1).zfill(s_num_files)+'.jpg'
				os.rename(os.path.join(path_name,file),os.path.join(path_name,newname))
				print('newname:',newname)
			elif dirname== "3_1Suspenderskirt":
				newname=prefix_name+"_"+str(index+1).zfill(s_num_files)+'.jpg'
				os.rename(os.path.join(path_name,file),os.path.join(path_name,newname))
				print('newname:',newname)
			elif dirname== "3_2Bustdress":
				newname=prefix_name+"_"+str(index+1).zfill(s_num_files)+'.jpg'
				os.rename(os.path.join(path_name,file),os.path.join(path_name,newname))
				print('newname:',newname)
			elif dirname== "3_3Onepieceskirt":
				newname=prefix_name+"_"+str(index+1).zfill(s_num_files)+'.jpg'
				os.rename(os.path.join(path_name,file),os.path.join(path_name,newname))
				print('newname:',newname)
			elif dirname== "5_1Gymshoes":
				newname=prefix_name+"_"+str(index+1).zfill(s_num_files)+'.jpg'
				os.rename(os.path.join(path_name,file),os.path.join(path_name,newname))
				print('newname:',newname)
			elif dirname== "5_2Leisureshoes":
				newname=prefix_name+"_"+str(index+1).zfill(s_num_files)+'.jpg'
				os.rename(os.path.join(path_name,file),os.path.join(path_name,newname))
				print('newname:',newname)
			elif dirname== "5_3Leathershoes":
				newname=prefix_name+"_"+str(index+1).zfill(s_num_files)+'.jpg'
				os.rename(os.path.join(path_name,file),os.path.join(path_name,newname))
				print('newname:',newname)
			elif dirname== "5_4Bootsshoes":
				newname=prefix_name+"_"+str(index+1).zfill(s_num_files)+'.jpg'
				os.rename(os.path.join(path_name,file),os.path.join(path_name,newname))
				print('newname:',newname)
			elif dirname== "5_5Sandalshoes":
				newname=prefix_name+"_"+str(index+1).zfill(s_num_files)+'.jpg'
				os.rename(os.path.join(path_name,file),os.path.join(path_name,newname))
				print('newname:',newname)
			elif dirname== "5_6Slippershoes":
				newname=prefix_name+"_"+str(index+1).zfill(s_num_files)+'.jpg'
				os.rename(os.path.join(path_name,file),os.path.join(path_name,newname))
				print('newname:',newname)
			elif dirname== "6_1Backpack":
				newname=prefix_name+"_"+str(index+1).zfill(s_num_files)+'.jpg'
				os.rename(os.path.join(path_name,file),os.path.join(path_name,newname))
				print('newname:',newname)
			elif dirname== "6_2Shoulderbag":
				newname=prefix_name+"_"+str(index+1).zfill(s_num_files)+'.jpg'
				os.rename(os.path.join(path_name,file),os.path.join(path_name,newname))
				print('newname:',newname)
			elif dirname== "6_3Handbag":
				newname=prefix_name+"_"+str(index+1).zfill(s_num_files)+'.jpg'
				os.rename(os.path.join(path_name,file),os.path.join(path_name,newname))
				print('newname:',newname)
			elif dirname== "6_4Clutchbag":
				newname=prefix_name+"_"+str(index+1).zfill(s_num_files)+'.jpg'
				os.rename(os.path.join(path_name,file),os.path.join(path_name,newname))
				print('newname:',newname)
			elif dirname== "6_5Wallet":
				newname=prefix_name+"_"+str(index+1).zfill(s_num_files)+'.jpg'
				os.rename(os.path.join(path_name,file),os.path.join(path_name,newname))
				print('newname:',newname)
			elif dirname== "6_6Suitcase":
				newname=prefix_name+"_"+str(index+1).zfill(s_num_files)+'.jpg'
				os.rename(os.path.join(path_name,file),os.path.join(path_name,newname))
				print('newname:',newname)
			elif dirname== "7_1Hat":
				newname=prefix_name+"_"+str(index+1).zfill(s_num_files)+'.jpg'
				os.rename(os.path.join(path_name,file),os.path.join(path_name,newname))
				print('newname:',newname)
			elif dirname== "7_2Tie":
				newname=prefix_name+"_"+str(index+1).zfill(s_num_files)+'.jpg'
				os.rename(os.path.join(path_name,file),os.path.join(path_name,newname))
				print('newname:',newname)
			elif dirname== "7_3Bowtie":
				newname=prefix_name+"_"+str(index+1).zfill(s_num_files)+'.jpg'
				os.rename(os.path.join(path_name,file),os.path.join(path_name,newname))
				print('newname:',newname)
			elif dirname== "7_4Belt":
				newname=prefix_name+"_"+str(index+1).zfill(s_num_files)+'.jpg'
				os.rename(os.path.join(path_name,file),os.path.join(path_name,newname))
				print('newname:',newname)
			elif dirname== "7_5Glove":
				newname=prefix_name+"_"+str(index+1).zfill(s_num_files)+'.jpg'
				os.rename(os.path.join(path_name,file),os.path.join(path_name,newname))
				print('newname:',newname)
			elif dirname== "7_6Glasses":
				newname=prefix_name+"_"+str(index+1).zfill(s_num_files)+'.jpg'
				os.rename(os.path.join(path_name,file),os.path.join(path_name,newname))
				print('newname:',newname)												
			elif dirname== "7_7Watch":
				newname=prefix_name+"_"+str(index+1).zfill(s_num_files)+'.jpg'
				os.rename(os.path.join(path_name,file),os.path.join(path_name,newname))
				print('newname:',newname)
			elif dirname== "8_1Necklace":
				newname=prefix_name+"_"+str(index+1).zfill(s_num_files)+'.jpg'
				os.rename(os.path.join(path_name,file),os.path.join(path_name,newname))
				print('newname:',newname)
			elif dirname== "8_2Earrings":
				newname=prefix_name+"_"+str(index+1).zfill(s_num_files)+'.jpg'
				os.rename(os.path.join(path_name,file),os.path.join(path_name,newname))
				print('newname:',newname)
			elif dirname== "8_3Fingerring":
				newname=prefix_name+"_"+str(index+1).zfill(s_num_files)+'.jpg'
				os.rename(os.path.join(path_name,file),os.path.join(path_name,newname))
				print('newname:',newname)
			elif dirname== "8_4Bangle":
				newname=prefix_name+"_"+str(index+1).zfill(s_num_files)+'.jpg'
				os.rename(os.path.join(path_name,file),os.path.join(path_name,newname))
				print('newname:',newname)


def rename_multidir():
	rename_filelist("1_1Overcoat","Overcoat_UpperWear")	
	rename_filelist("1_2Coat","Coat_UpperWear")
	rename_filelist("1_3Sweater","Sweater_UpperWear")	
	rename_filelist("1_4Shirt","Shirt_UpperWear")
	rename_filelist("1_5Fleece","Fleece_UpperWear")	
	rename_filelist("1_6Tshirt","Tshirt_UpperWear")
	rename_filelist("2_1Tailoredtrousers","Suitpants_Trousers")
	rename_filelist("2_2Casualtrousers","Casualpants_Trousers")
	rename_filelist("2_3Jeanstrousers","Jeans_Trousers")	
	rename_filelist("2_4Sporttrousers","Sportspants_Trousers")
	rename_filelist("3_1Suspenderskirt","Suspenderskirt_Skirt")	
	rename_filelist("3_2Bustdress","Bustdress_Skirt")
	rename_filelist("3_3Onepieceskirt","Onepiecesdress_Skirt")
	rename_filelist("5_1Gymshoes","Gymshoes_Shoes")	
	rename_filelist("5_2Leisureshoes","Leisureshoes_Shoes")
	rename_filelist("5_3Leathershoes","Leathershoes_Shoes")	
	rename_filelist("5_4Bootsshoes","Boots_Shoes")
	rename_filelist("5_5Sandalshoes","Sandal_Shoes")	
	rename_filelist("5_6Slippershoes","Slipper_Shoes")
	rename_filelist("6_1Backpack","Backpack_BagsandCases")	
	rename_filelist("6_2Shoulderbag","ShoulderBag_BagsandCases")
	rename_filelist("6_3Handbag","Handbag_BagsandCases")	
	rename_filelist("6_4Clutchbag","Clutchhandbag_BagsandCases")
	rename_filelist("6_5Wallet","Wallet_BagsandCases")	
	rename_filelist("6_6Suitcase","Suitcase_BagsandCases")
	rename_filelist("7_1Hat","Hat_ACC")	
	rename_filelist("7_2Tie","Tie_ACC")
	rename_filelist("7_3Bowtie","Bowtie_ACC")	
	rename_filelist("7_4Belt","Belt_ACC")
	rename_filelist("7_5Glove","Glove_ACC")	
	rename_filelist("7_6Glasses","Glasses_ACC")
	rename_filelist("7_7Watch","Watch_ACC")
	rename_filelist("8_1Necklace","Necklace_Jewelry")
	rename_filelist("8_2Earrings","Earrings_Jewelry")
	rename_filelist("8_3Fingerring","Fingerring_Jewelry")
	rename_filelist("8_4Bangle","Bangle_Jewelry")

xml_subdir_path = "\\xmls\\"
		
def rename_uniform_add_number(subdir_path):
	paths=[]
	cwd_dir = os.getcwd()
	full_dir_path = cwd_dir + subdir_path
	fileslist_in_dir = os.listdir(full_dir_path)
	num_files = len(fileslist_in_dir)
	print('num_files:',num_files)
	s_num_files = len(str(num_files))	
	
	for path_name in fileslist_in_dir:
		print("rename_uniform_add_number path_name:",path_name)
		old_number = path_name.split('.')[0].split('_')[-1]
		new_number = str(int(old_number)+600).zfill(3)
		print("rename_uniform_add_number name:",new_number)
		short_filename= path_name.split('.')[0]
		suffix_filename= path_name.split('.')[-1]
		short_filename = short_filename.replace(old_number,new_number)
		new_filename= short_filename+'.'+suffix_filename
		print("rename_filelist_replacename new_filename:",new_filename)
		os.rename(os.path.join(full_dir_path,path_name),os.path.join(full_dir_path,new_filename))
	



def	main():			
	rename_uniform_add_number(xml_subdir_path)
	
	gc.collect()
			
			
			
if __name__ == '__main__':
	main()


