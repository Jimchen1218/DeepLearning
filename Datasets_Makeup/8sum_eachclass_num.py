'''
filename:count_eachtype_num.py
author:jimchen1218@sina.com
create date:1/4/2018
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


xml_subdir_path = "\\annotations\\xmls\\"
  
def count_eachtype_num():
	gsum=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	curdir = os.getcwd()
	countnum_dir =curdir + xml_subdir_path
	print("count_eachtype_num countnum_dir:",countnum_dir)	
	filenames=os.listdir(countnum_dir)
	#txt_filename= filenames[0].split('.')[0].split('_')[0]+'.txt'

	for filename in filenames:
		print("filename:",filename)
		if 'Overcoat' in filename:
			gsum[1]=gsum[1]+1
		elif 'Coat' in filename:
			gsum[2]=gsum[2]+1
		elif 'Sweater' in filename:
			gsum[3]=gsum[3]+1
		elif 'Shirt' in filename:
			gsum[4]=gsum[4]+1
		elif 'Fleece' in filename:
			gsum[5]=gsum[5]+1
		elif 'Tshirt' in filename:
			print("Tshirt:")
			gsum[6]=gsum[6]+1
		elif 'Suitpants' in filename:
			gsum[7]=gsum[7]+1
		elif 'Casualpants' in filename:
			gsum[8]=gsum[8]+1
		elif 'Jeans' in filename:
			gsum[9]=gsum[9]+1	
		elif 'Sportspants' in filename:
			gsum[10]=gsum[10]+1	
		elif 'Suspenderskirt' in filename:
			gsum[11]=gsum[11]+1
		elif 'Bustdress' in filename:
			gsum[12]=gsum[12]+1		
		elif 'Onepiecesdress' in filename:
			gsum[13]=gsum[13]+1		
		elif 'Gymshoes_Shoes' in filename:
			gsum[14]=gsum[14]+1
		elif 'Leisureshoes' in filename:
			gsum[15]=gsum[15]+1		
		elif 'Leathershoes' in filename:
			gsum[16]=gsum[16]+1	
		elif 'Boots' in filename:
			gsum[17]=gsum[17]+1
		elif 'Sandal' in filename:
			gsum[18]=gsum[18]+1		
		elif 'Slipper' in filename:
			gsum[19]=gsum[19]+1 
		elif 'Backpack' in filename:
			gsum[20]=gsum[20]+1
		elif 'ShoulderBag' in filename:
			gsum[21]=gsum[21]+1		
		elif 'Handbag' in filename:
			gsum[22]=gsum[22]+1	
		elif 'Clutch' in filename:
			print("Clutch:")
			gsum[23]=gsum[23]+1
		elif 'Wallet' in filename:
			gsum[24]=gsum[24]+1	
		elif 'Suitcase' in filename:
			gsum[25]=gsum[25]+1 
		elif 'Hat' in filename:
			gsum[26]=gsum[26]+1 
		elif 'Tie' in filename:
			gsum[27]=gsum[27]+1
		elif 'Bowtie' in filename:
			gsum[28]=gsum[28]+1	
		elif 'Belt' in filename:
			gsum[29]=gsum[29]+1		
		elif 'Glove' in filename:
			gsum[30]=gsum[30]+1
		elif 'Glasses' in filename:
			gsum[31]=gsum[31]+1
		elif 'Watch' in filename:
			gsum[32]=gsum[32]+1  	
		elif 'Necklace' in filename:
			gsum[33]=gsum[33]+1		
		elif 'Earrings' in filename:
			gsum[34]=gsum[34]+1	
		elif 'Fingerring' in filename:
			gsum[35]=gsum[35]+1
		elif 'Bangle' in filename:
			gsum[36]=gsum[36]+1	
		elif 'Bracelet' in filename:
			gsum[37]=gsum[37]+1

	for i in range(38):
		gsum[0]=gsum[0]+gsum[i]
	
	print("\nOvercoat_UpperWear gsum[1]:",gsum[1])
	print("Coat_UpperWear gsum[2]:",gsum[2])
	print("Sweater_UpperWear gsum[3]:",gsum[3])
	print("Shirt_UpperWear gsum[4]:",gsum[4])
	print("Fleece_UpperWear gsum[5]:",gsum[5])
	print("TShirt_UpperWear gsum[6]:",gsum[6])
	
	print("\nSuitpants_Trousers gsum[7]:",gsum[7])
	print("Casualpants_Trousers gsum[8]:",gsum[8])
	print("Jeans_Trousers gsum[9]:",gsum[9])
	print("Sportspants_Trousers gsum[10]:",gsum[10])
	
	print("\nSuspenderskirt_Skirt gsum[11:",gsum[11])
	print("Bustdress_Skirt gsum[12]:",gsum[12])
	print("Onepiecesdress_Skirt gsum[13]:",gsum[13])
	
	print("\nGymshoes_Shoes gsum[14]:",gsum[14])
	print("Leisureshoes_Shoes gsum[15]:",gsum[15])
	print("Leathershoes_Shoes gsum[16]:",gsum[16])
	print("Boots_Shoes gsum[17]:",gsum[17])		
	print("Sandal_Shoes gsum[18]:",gsum[18])
	print("Slipper_Shoes gsum[19]:",gsum[19])	
	
	print("\nBackpack_BagsandCases gsum[20]:",gsum[20])
	print("ShoulderBag_BagsandCases gsum[21]:",gsum[21])
	print("Handbag_BagsandCases gsum[22]:",gsum[22])
	print("ClutchHandbag_BagsandCases gsum[23]:",gsum[23])		
	print("Wallet_BagsandCases gsum[24]:",gsum[24])
	print("Suitcase_BagsandCases gsum[25]:",gsum[25])		
	
	
	print("\nHat_ACC gsum[26]:",gsum[26])
	print("Tie_ACC gsum[27]:",gsum[27])
	print("Bowtie_ACC gsum[28]:",gsum[28])
	print("Belt_ACC gsum[29]:",gsum[29])		
	print("Glove_ACC gsum[30]:",gsum[30])
	print("Glasses_ACC gsum[31]:",gsum[31])		
	print("Watch_ACC gsum[32]:",gsum[32])			

	print("\nNecklace_Jewelry gsum[33]:",gsum[33])
	print("Earrings_Jewelry gsum[34]:",gsum[34])
	print("Fingerring_Jewelry gsum[35]:",gsum[35])
	print("Bangle_Jewelry gsum[36]:",gsum[36])		
	print("Bracelet_Jewelry gsum[37]:",gsum[37])

	print("\nTotal sum: gsum[0]:",gsum[0])


def main():
	count_eachtype_num()
	

if __name__ == "__main__":
	main()