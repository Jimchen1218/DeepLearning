import os
import gc

prefix_name = "TShirt_UpperWear_"
path = os.getcwd()
print("path:",path)
path_rename=path+"\\T_shirt"

for index,file in enumerate(os.listdir(path_rename)):
	print("index:",index)
	if os.path.splitext(file)[1] == '.jpg':
		newname=prefix_name+str(index+1)+'.jpg'
		os.rename(os.path.join(path_rename,file),os.path.join(path_rename,newname))
		print('newname:',newname)


gc.collect()
