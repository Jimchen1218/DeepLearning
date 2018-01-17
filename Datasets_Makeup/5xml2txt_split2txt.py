'''
filename:xml2txt_split2txt_new.py
author:jimchen1218@sina.com
create date:1/2/2018
'''
import os    

print(__doc__)

'''
  name: "Overcoat_UpperWear"
  name: "Coat_UpperWear"
  name: "Sweater_UpperWear"
  name: "Shirt_UpperWear"
  name: "Fleece_UpperWear"
  name: "TShirt_UpperWear"

  name: "Suitpants_Trousers"
  name: "Casualpants_Trousers"
  name: "Jeans_Trousers"
  name: "Sportspants_Trousers"

  name: "Suspenderskirt_Skirt"
  name: "Bustdress_Skirt"  	
  name: "Onepiecesdress_Skirt"

  name: "Gymshoes_Shoes"
  name: "Leisureshoes_Shoes"
  name: "Leathershoes_Shoes"
  name: "Boots_Shoes"  	
  name: "Sandal_Shoes"  	
  name: "Slipper_Shoes"
  
  name: "Backpack_BagsandCases"
  name: "ShoulderBag_BagsandCases" 	
  name: "Handbag_BagsandCases"  	
  name: "ClutchHandbag_BagsandCases"
  name: "Wallet_BagsandCases"  	
  name: "Suitcase_BagsandCases"

  name: "Hat_ACC"
  name: "Tie_ACC"  	
  name: "Bowtie_ACC"  	
  name: "Belt_ACC"
  name: "Glove_ACC"  	
  name: "Glasses_ACC"
  name: "Watch_ACC"
  	

  name: "Necklace_Jewelry"  	
  name: "Earrings_Jewelry"  	
  name: "Fingerring_Jewelry"  
  name: "Bangle_Jewelry" 
  name: "Bracelet_Jewelry"
'''
def main(): 
mergefiledir = os.getcwd()+'\\xmls'
print("mergefiledir:",mergefiledir)
filenames=os.listdir(mergefiledir)
#txt_filename= filenames[0].split('.')[0].split('_')[0]+'.txt'
txt_list= 'list.txt'
print("txt_list:",txt_list)
file_list=open(txt_list,'w')
  
for filename in filenames:
	print("filename:",filename)
	if 'Overcoat' in filename:
		file_list.writelines(filename.split('.')[0]+' 1 1 1')	
	elif 'Coat' in filename:
		file_list.writelines(filename.split('.')[0]+' 2 1 2')
	elif 'Sweater' in filename:
		file_list.writelines(filename.split('.')[0]+' 3 1 3')	
	elif 'Shirt' in filename:
		file_list.writelines(filename.split('.')[0]+' 4 1 4')	
	elif 'Fleece' in filename:
		file_list.writelines(filename.split('.')[0]+' 5 1 5')
	elif 'Tshirt' in filename:
		file_list.writelines(filename.split('.')[0]+' 6 1 6')
	elif 'Suitpants' in filename:
		file_list.writelines(filename.split('.')[0]+' 7 2 1')		
	elif 'Casualpants' in filename:
		file_list.writelines(filename.split('.')[0]+' 8 2 2')
	elif 'Jeans' in filename:
		file_list.writelines(filename.split('.')[0]+' 9 2 3')
	elif 'Sportspants' in filename:
		file_list.writelines(filename.split('.')[0]+' 10 2 4')
	elif 'Suspenderskirt' in filename:
		file_list.writelines(filename.split('.')[0]+' 11 3 1')		
	elif 'Bustdress' in filename:
		file_list.writelines(filename.split('.')[0]+' 12 3 2')		
	elif 'Onepiecesdress' in filename:
		file_list.writelines(filename.split('.')[0]+' 13 3 3')
	elif 'Gymshoes_Shoes' in filename:
		file_list.writelines(filename.split('.')[0]+' 14 4 1')
	elif 'Leisureshoes_Shoes' in filename:
		file_list.writelines(filename.split('.')[0]+' 15 4 2')		
	elif 'Leathershoes_Shoes' in filename:
		file_list.writelines(filename.split('.')[0]+' 16 4 3')
	elif 'Boots_Shoes' in filename:
		file_list.writelines(filename.split('.')[0]+' 17 4 4')		
	elif 'Sandal_Shoes' in filename:
		file_list.writelines(filename.split('.')[0]+' 18 4 5')
	elif 'Slipper_Shoes' in filename:
		file_list.writelines(filename.split('.')[0]+' 19 4 6')
	elif 'Backpack' in filename:
		file_list.writelines(filename.split('.')[0]+' 20 5 1')
	elif 'ShoulderBag' in filename:
		file_list.writelines(filename.split('.')[0]+' 21 5 2')		
	elif 'Handbag' in filename:
		file_list.writelines(filename.split('.')[0]+' 22 5 3')		
	elif 'Clutchhandbag' in filename:
		file_list.writelines(filename.split('.')[0]+' 23 5 4')
	elif 'Wallet' in filename:
		file_list.writelines(filename.split('.')[0]+' 24 5 5')
	elif 'Suitcase' in filename:
		file_list.writelines(filename.split('.')[0]+' 25 5 6')
	elif 'Hat' in filename:
		file_list.writelines(filename.split('.')[0]+' 26 6 1')	
	elif 'Tie' in filename:
		file_list.writelines(filename.split('.')[0]+' 27 6 2')			
	elif 'Bowtie' in filename:
		file_list.writelines(filename.split('.')[0]+' 28 6 3')
	elif 'Belt' in filename:
		file_list.writelines(filename.split('.')[0]+' 29 6 4')
	elif 'Glove' in filename:
		file_list.writelines(filename.split('.')[0]+' 30 6 5')		
	elif 'Glasses' in filename:
		file_list.writelines(filename.split('.')[0]+' 31 6 6')		
	elif 'Watch' in filename:
		file_list.writelines(filename.split('.')[0]+' 32 6 7')
	elif 'Necklace' in filename:
		file_list.writelines(filename.split('.')[0]+' 33 7 1')		
	elif 'Earrings' in filename:
		file_list.writelines(filename.split('.')[0]+' 34 7 2')	
	elif 'Fingerring' in filename:
		file_list.writelines(filename.split('.')[0]+' 35 7 3')				
	elif 'Bangle' in filename:
		file_list.writelines(filename.split('.')[0]+' 36 7 4')
											
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

if __name__ == "__main__":
	main()



