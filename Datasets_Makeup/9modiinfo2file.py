import os
import sys
import re
import os.path


def addinfo2file(fullpath):		
		fileold = open(fullpath,"rb+")
		totallines = fileold.readlines()
		print("length:",totallines.__len__())
		fileold.close()
		tarline=0
		for i in range(totallines.__len__()):
			#print("totallines[i]:",totallines[i].decode())
			if '/segmented>' in totallines[i].decode():
				tarline = int(i)+1
				print("add <object> ... at line:",tarline)
				addinfo = '''  <object>\n'''
				addinfo = addinfo +'''    <name>notclothes</name>\n'''
				addinfo = addinfo +'''		<pose>Unspecified</pose>\n'''
				addinfo = addinfo +'''	  <truncated>1</truncated>\n'''
				addinfo = addinfo +'''		<difficult>0</difficult>\n'''
				addinfo = addinfo +'''		<bndbox>\n'''
				addinfo = addinfo +'''		  <xmin>0</xmin>\n'''
				addinfo = addinfo +'''		  <ymin>0</ymin>\n'''
				addinfo = addinfo +'''		  <xmax>500</xmax>\n'''
				addinfo = addinfo +'''		  <ymax>500</ymax>\n'''
				addinfo = addinfo +'''    </bndbox>\n'''
				addinfo = addinfo +'''  </object>\n'''		
				totallines.insert(tarline,addinfo.encode(encoding='utf-8'))
				#print("length of after change:",totallines.__len__())
				filenew= open(fullpath,"wb")
				for item in totallines:
					filenew.write(item)
				filenew.close()
				break
				
		fileold.close()
		
		
def mofiinfo2file(fullpath):		
		fileold = open(fullpath,"rb+")
		totallines = fileold.readlines()
		print("mofiinfo2file length:",totallines.__len__())
		filenew= open(fullpath,"wb")
		#for i in range(totallines.__len__()):
		for line in totallines:
			if '<object>' in line.decode() or '<bndbox>' in line.decode() or '/name' in line.decode() or '/pose>' in line.decode() or '/truncated>' in line.decode() or '/difficult>' in line.decode():
				continue
			if '/xmin>' in line.decode() or '/ymin>' in line.decode()	or '/xmax>' in line.decode() or '/ymax>' in line.decode() or '/ymax>' in line.decode() or '</bndbox>' in line.decode() or '</object>' in line.decode():
				continue			
			filenew.write(line)
			
		filenew.close()
		fileold.close()
		
import re

def modifycontent_name(relapath,path):
	cur_path = os.getcwd()
	fullpath = cur_path+"\\"+ path +relapath
	prefix = relapath.split(".")[0][:-5]
	print("modifycontent_name prefix:",prefix)
	fileold = open(fullpath,"rb+")
	totallines = fileold.readlines()
	filenew= open(fullpath,"wb")
	txt_buf =""
	for line in totallines:
		if '<name>' in line.decode():
			print("modifycontent_name line.decode():",line.decode())
			replacedStr =re.sub(r"<name>(\S+)", "<name>"+prefix+"</name>", line.decode());
			print("modifycontent_name replacedStr:",replacedStr)
			txt_buf +=replacedStr
			continue
		txt_buf += line.decode()	
	filenew.write(txt_buf.encode())
		
	filenew.close()
	fileold.close()		

		
def modifycontent_filename(relapath,path):
	cur_path = os.getcwd()
	fullpath = cur_path+"\\"+ path +relapath
	prefix = relapath.split(".")[0]
	print("modifyfilename prefix:",prefix)
	fileold = open(fullpath,"rb+")
	totallines = fileold.readlines()
	filenew= open(fullpath,"wb")
	txt_buf =""
	for line in totallines:
		if '<filename>' in line.decode():
			print("modifycontent_filename line.decode():",line.decode())
			replacedStr =re.sub(r"<filename>(\S+)", "<filename>"+prefix+".jpg"+"</filename>", line.decode());
			print("modifycontent_filename replacedStr:",replacedStr)
			txt_buf +=replacedStr
			continue
		txt_buf += line.decode()	
	filenew.write(txt_buf.encode())
		
	filenew.close()
	fileold.close()		
				
def replace_str_in_xmlline_split(old_line_str,new_file_name):
	pure_fullpath =re.findall("<path>(.*)</path>", old_line_str);
	print("replace_str_in_xmlline_split pure_fullpath:",pure_fullpath)
	filename = pure_fullpath.split("\\")[-1]
	#print("get_fullpath_except_name filename:",filename)
	len_suffix=len(filename)
	path_ex_name = fullpath[:-len_suffix]
	#print("get_fullpath_except_name path_ex_name:",path_ex_name)
	return path_ex_name
		

def replace_str_in_xmlline(old_line_str,new_file_name):	
	pure_fullpath =re.findall("<path>(.*)</path>", old_line_str);
	print("replace_str_in_xmlline pure_fullpath:\n",pure_fullpath)
	splitpath=os.path.split(pure_fullpath[0])
	print("replace_str_in_xmlline splitpath:\n",splitpath)
	newfullpath = splitpath[0]+"\\"+new_file_name+"."+splitpath[1].split(".")[-1]
	print("replace_str_in_xmlline newfullpath:\n",newfullpath)
	new_line_str = "  <path>"+	newfullpath+	"</path>\n"
	return 	new_line_str
	
def replace_str_in_xmlline_repl(old_line_str,new_file_name):
	pure_fullpath =re.findall("<path>(.*)</path>", old_line_str);
	print("replace_str_in_xmlline pure_fullpath:\n",pure_fullpath)
	splitpath=os.path.split(pure_fullpath[0])
	print("replace_str_in_xmlline splitpath:\n",splitpath)
	
	newfullpath = splitpath[0]+"\\"+new_file_name+"."+splitpath[1].split(".")[-1]
	print("replace_str_in_xmlline newfullpath:\n",newfullpath)
	new_line_str = "  <path>"+	newfullpath+	"</path>\n"
	return 	new_line_str	
		
		
def modifycontent_path(relapath,path):
	cur_path = os.getcwd()
	fullpath = cur_path+"\\"+ path +relapath
	newfilename = fullpath.split("\\")[-1].split(".")[0]
	print("modifycontent_path newfilename:\n",newfilename)
	fileold = open(fullpath,"rb+")
	totallines = fileold.readlines()
	filenew= open(fullpath,"wb")
	txt_buf =""
	for line in totallines:
		if '<path>' in line.decode():
			txt_buf +=replace_str_in_xmlline(line.decode(),newfilename)
			continue
		txt_buf += line.decode()
	filenew.write(txt_buf.encode())
		
	filenew.close()
	fileold.close()

def modifycontent(path):
	cur_path = os.getcwd()
	for root,dirs,files in os.walk(cur_path + path):
		print(" files:",files)
		for name in files:
			if name.split('.')[-1] == 'xml':
				modifycontent_filename(name,path)
				modifycontent_path(name,path)
				modifycontent_name(name,path)


def main():
	modifycontent("\\annotations\\xml\\")
	

if __name__ == "__main__":
	main()


#sys.exit(0)


