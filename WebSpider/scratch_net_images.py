import urllib
import urllib.request
import re
import ssl
import bs4
import time
import threading
import os
import gc
import chardet


def download_page(url):
		headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) '
		                     'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}
		request = urllib.request.Request(url, headers=headers)
		context = ssl._create_unverified_context()
		response = urllib.request.urlopen(request, context=context,timeout=120)
		data = response.read()
		#encoding_dict = chardet.detect(data)
		#web_encoding = encoding_dict['encoding']
		#print("web_encoding:",web_encoding)
		#if web_encoding == 'utf-8' or web_encoding == 'UTF-8':
		#		html = data
		#else :
		#		html = data.decode('gbk','ignore').encode('utf-8')
		return data


def get_image(html,name,foldname):
    #regx = r'http://[\S]*\.jpg'  #baidu
    # regx = r'http:[^s]*?(jpg|png|gif)'
    #regx = r'<img src=\"(.*?)\"'  #360
    regx = r'<img data-ks-lazyload=\"(.*?)\"'
    pattern = re.compile(regx)
    #print(pattern)
    # pattern = r'(http:[^s]*?(jpg|png|gif))'
    get_img = re.findall(pattern, repr(html))
    for img in get_img:
    	print(img)
    print('\n')
    #print("get_img:\n",get_img)
    len_imglist= len(get_img)
    print("len_imglist:\n",len_imglist)
    num = 1
    for img in get_img:
        print(img)
        if not img.startswith('http'):
        	img= "http:"+img
        
        image = download_page(img)
        with open('%s/%s_%s.jpg' %(foldname,name,num), 'wb') as fp:
            fp.write(image)
            time.sleep(1)
            print("download %s" % num)
            num += 1	
    return

def mkdir(foldname):
		if not os.path.exists(foldname):
			os.mkdir(foldname)


def scratch_imgs(url,foldname):
	name="box2"
	mkdir(foldname)
	print("scratch_imgs start!")
	html = download_page(url)
	get_image(html,name,foldname)
	print("scratch_imgs success!")


#1.1 overcoat
def scratch_imgs_clothes_overcoat():
	foldname = "1_overcoat"
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E5%A4%A7%E8%A1%A3%E7%94%B7&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i,foldname)
		
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E5%A4%A7%E8%A1%A3%E5%A5%B3&page="
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i+5,foldname)		
	
#1.2 coat
def scratch_imgs_clothes_coat():
	foldname = "1_coat"
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E5%A4%96%E5%A5%97%E7%94%B7&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i,foldname)
		
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E5%A4%96%E5%A5%97%E5%A5%B3&page="
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i+5,foldname)
		
#1.3 sweater
def scratch_imgs_clothes_sweater():
	foldname = "1_sweater"
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E6%AF%9B%E8%A1%A3%E7%94%B7&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i,foldname)
		
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E6%AF%9B%E8%A1%A3%E5%A5%B3&page="
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i+5,foldname)		
		
#1.4 shirt
def scratch_imgs_clothes_shirt():
	foldname = "1_shirt"
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E8%A1%AC%E8%A1%AB%E7%94%B7&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i,foldname)
		
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E8%A1%AC%E8%A1%AB%E5%A5%B3&page="
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i+5,foldname)		
		
#1.5 fleece
def scratch_imgs_clothes_fleece():
	foldname = "1_fleece"
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E5%8D%AB%E8%A1%A3%E7%94%B7&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i,foldname)
		
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E5%8D%AB%E8%A1%A3%E5%A5%B3&page="
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i+5,foldname)		
	
#1.6 T_shirt
def scratch_imgs_clothes_T_shirt():
	foldname = "1_T_shirt"
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=T%E6%81%A4%E7%94%B7&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i,foldname)
		
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=T%E6%81%A4%E5%A5%B3&page="
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i+5,foldname)
		
#1 clothes		
def scratch_imgs_clothes():		
		#scratch_imgs_clothes_overcoat()
		#scratch_imgs_clothes_coat()
		#scratch_imgs_clothes_sweater()
		#scratch_imgs_clothes_shirt()
		#scratch_imgs_clothes_fleece()
		scratch_imgs_clothes_T_shirt()
		
#2.1 suit_pants
def scratch_imgs_clothes_suit_pants():
	foldname = "2_suit_pants"
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E8%A5%BF%E8%A3%A4%E7%94%B7&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i,foldname)
		
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E8%A5%BF%E8%A3%A4%E5%A5%B3&page="
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i+5,foldname)

#2.2 casual_pants
def scratch_imgs_clothes_casual_pants():
	foldname = "2_casual_pants"
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E4%BC%91%E9%97%B2%E8%A3%A4%E7%94%B7&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i,foldname)
		
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E4%BC%91%E9%97%B2%E8%A3%A4%E5%A5%B3&page="
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i+5,foldname)		

#2.3 jeans
def scratch_imgs_clothes_jeans():
	foldname = "2_jeans"
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E7%89%9B%E4%BB%94%E8%A3%A4%E7%94%B7&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i,foldname)
		
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E7%89%9B%E4%BB%94%E8%A3%A4%E5%A5%B3&page="
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i+5,foldname)

#2.4 sport_pants
def scratch_imgs_clothes_sport_pants():
	foldname = "2_sport_pants"
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E8%BF%90%E5%8A%A8%E8%A3%A4%E7%94%B7&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i,foldname)
		
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E8%BF%90%E5%8A%A8%E8%A3%A4%E5%A5%B3&page="
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i+5,foldname)

#2 pants
def scratch_imgs_pants():		
	scratch_imgs_clothes_suit_pants()
	scratch_imgs_clothes_casual_pants()
	scratch_imgs_clothes_jeans()
	scratch_imgs_clothes_sport_pants()


#3.1 skirt
def scratch_imgs_clothes_skirt():
	foldname = "3_skirt"
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E5%8D%8A%E8%BA%AB%E8%A3%99&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i,foldname)

#3.2 dress
def scratch_imgs_clothes_dress():
	foldname = "3_dress"
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E8%BF%9E%E8%A1%A3%E8%A3%99%E7%A7%8B%E5%86%AC&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i,foldname)

#3.3 suspender_skirt
def scratch_imgs_clothes_suspender_skirt():
	foldname = "3_suspender_skirt"
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E8%83%8C%E5%B8%A6%E8%A3%99%E7%A7%8B%E5%86%AC&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i,foldname)

#3 skirt		
def scratch_imgs_skirt():		
	scratch_imgs_clothes_skirt()
	scratch_imgs_clothes_dress()
	scratch_imgs_clothes_suspender_skirt()
	
#4.1 tailored_suit
def scratch_imgs_clothes_tailored_suit():
	foldname = "4_tailored_suit"
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E8%A5%BF%E6%9C%8D%E5%A5%97%E8%A3%85%E7%94%B7&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i,foldname)
	
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E8%A5%BF%E6%9C%8D%E5%A5%97%E8%A3%85%E5%A5%B3&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i+5,foldname)
		
#4.2 sweat_suit
def scratch_imgs_clothes_sweat_suit():
	foldname = "4_sweat_suit"
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E8%BF%90%E5%8A%A8%E5%A5%97%E8%A3%85%E7%94%B7&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i,foldname)
	
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E8%BF%90%E5%8A%A8%E5%A5%97%E8%A3%85%E5%A5%B3&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i+5,foldname)		
			
#4.3 leisure_suit
def scratch_imgs_clothes_leisure_suit():
	foldname = "4_leisure_suit"
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E4%BC%91%E9%97%B2%E5%A5%97%E8%A3%85%E7%94%B7&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i,foldname)
	
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E4%BC%91%E9%97%B2%E5%A5%97%E8%A3%85%E5%A5%B3&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i+5,foldname)		
		
#4 suit		
def scratch_imgs_suit():
	scratch_imgs_clothes_tailored_suit()
	scratch_imgs_clothes_sweat_suit()
	scratch_imgs_clothes_leisure_suit()

#5.1 gym_shoes
def scratch_imgs_gym_shoes():
	foldname = "5_gym_shoes"
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E8%BF%90%E5%8A%A8%E9%9E%8B%E7%94%B7&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i,foldname)
	
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E8%BF%90%E5%8A%A8%E9%9E%8B%E5%A5%B3&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i+5,foldname)		

#5.2 leisure_shoes
def scratch_imgs_leisure_shoes():
	foldname = "5_leisure_shoes"
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E4%BC%91%E9%97%B2%E9%9E%8B%E7%94%B7&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i,foldname)
	
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E4%BC%91%E9%97%B2%E9%9E%8B%E5%A5%B3&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i+5,foldname)	

#5.3 leather_shoes
def scratch_imgs_leather_shoes():
	foldname = "5_leather_shoes"
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E7%9A%AE%E9%9E%8B%E7%94%B7&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i,foldname)
	
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E7%9A%AE%E9%9E%8B%E5%A5%B3&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i+5,foldname)	

#5.4 boots
def scratch_imgs_boots():
	foldname = "5_boots"
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E9%9D%B4%E7%94%B7&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i,foldname)
	
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E9%9D%B4%E5%A5%B3&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i+5,foldname)	
		
#5.5 sandal
def scratch_imgs_sandal():
	foldname = "5_sandal"
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E5%87%89%E9%9E%8B%E7%94%B7&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i,foldname)
	
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E5%87%89%E9%9E%8B%E5%A5%B3&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i+5,foldname)		
		
#5.6 slipper
def scratch_imgs_slipper():
	foldname = "5_slipper"
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E6%8B%96%E9%9E%8B%E7%94%B7&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i,foldname)
	
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E6%8B%96%E9%9E%8B%E5%A5%B3&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i+5,foldname)				
		
#5 shoes		
def scratch_imgs_shoes():	
	#scratch_imgs_gym_shoes()
	#scratch_imgs_leisure_shoes()
	scratch_imgs_leather_shoes()
	scratch_imgs_boots()
	scratch_imgs_sandal()
	scratch_imgs_slipper()
		
#6.1 backpack
def scratch_imgs_backpack():
	foldname = "6_backpack"
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E5%8F%8C%E8%82%A9%E5%8C%85%E7%94%B7&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i,foldname)
	
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E5%8F%8C%E8%82%A9%E5%8C%85%E5%A5%B3&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i+5,foldname)			
		
#6.2 single_shoulder_bag
def scratch_imgs_single_shoulder_bag():
	foldname = "6_single_shoulder_bag"
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E5%8D%95%E8%82%A9%E5%8C%85%E7%94%B7&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i,foldname)
	
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E5%8D%95%E8%82%A9%E5%8C%85%E5%A5%B3&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i+5,foldname)			
		
#6.3 handbag
def scratch_imgs_handbag():
	foldname = "6_handbag"
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E6%89%8B%E6%8F%90%E5%8C%85%E7%94%B7&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i,foldname)
	
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E6%89%8B%E6%8F%90%E5%8C%85%E5%A5%B3&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i+5,foldname)		
			
#6.4 clutch_handbag
def scratch_imgs_clutch_handbag():
	foldname = "6_clutch_handbag"
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E6%89%8B%E6%8B%BF%E5%8C%85%E7%94%B7&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i,foldname)
	
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E6%89%8B%E6%8B%BF%E5%8C%85%E5%A5%B3&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i+5,foldname)		
		
#6.5 wallet
def scratch_imgs_wallet():
	foldname = "6_wallet"
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E9%92%B1%E5%8C%85%E7%94%B7&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i,foldname)
	
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E9%92%B1%E5%8C%85%E5%A5%B3&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i+5,foldname)	
		
#6.6 suitcase
def scratch_imgs_suitcase():
	foldname = "6_suitcase"
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E6%97%85%E8%A1%8C%E7%AE%B1%E7%94%B7&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i,foldname)
	
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E6%97%85%E8%A1%8C%E7%AE%B1%E5%A5%B3&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i+5,foldname)
						
#6 bags		
def scratch_imgs_bags():	
	scratch_imgs_backpack()
	scratch_imgs_single_shoulder_bag()
	scratch_imgs_handbag()
	scratch_imgs_clutch_handbag()
	scratch_imgs_wallet()
	scratch_imgs_suitcase()

#7.1 hat
def scratch_imgs_hat():
	foldname = "7_hat"
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E5%B8%BD%E5%AD%90%E7%94%B7&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i,foldname)
	
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E5%B8%BD%E5%AD%90%E5%A5%B3&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i+5,foldname)
		
#7.2 scaf
def scratch_imgs_scaf():
	foldname = "7_scaf"
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E5%9B%B4%E5%B7%BE%E7%94%B7&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i,foldname)
	
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E5%9B%B4%E5%B7%BE%E5%A5%B3&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i+5,foldname)		
		
#7.3 kerchief
def scratch_imgs_kerchief():
	foldname = "7_kerchief"
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E6%96%B9%E5%B7%BE%E7%94%B7&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i,foldname)
	
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E6%96%B9%E5%B7%BE%E5%A5%B3&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i+5,foldname)		
		

#7.4 tie
def scratch_imgs_tie():
	foldname = "7_tie"
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E9%A2%86%E5%B8%A6%E7%94%B7&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i,foldname)
	
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E9%A2%86%E5%B8%A6%E5%A5%B3&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i+5,foldname)			
		

#7.5 bowtie
def scratch_imgs_bowtie():
	foldname = "7_bowtie"
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E9%A2%86%E7%BB%93%E7%94%B7&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i,foldname)
	
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E9%A2%86%E7%BB%93%E5%A5%B3&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i+5,foldname)	
		

#7.6 belt
def scratch_imgs_belt():
	foldname = "7_belt"
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E8%85%B0%E5%B8%A6%E7%94%B7&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i,foldname)
	
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E8%85%B0%E5%B8%A6%E5%A5%B3&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i+5,foldname)		
		
#7.7 glove
def scratch_imgs_glove():
	foldname = "7_glove"
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E6%89%8B%E5%A5%97%E7%94%B7&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i,foldname)
	
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E6%89%8B%E5%A5%97%E5%A5%B3&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i+5,foldname)	

#7.8 glasses
def scratch_imgs_glasses():
	foldname = "7_glasses"
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E7%9C%BC%E9%95%9C%E7%94%B7&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i,foldname)
	
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E7%9C%BC%E9%95%9C%E5%A5%B3&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i+5,foldname)	
		
#7.9 watch
def scratch_imgs_watch():
	foldname = "7_watch"
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E6%89%8B%E8%A1%A8%E7%94%B7&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i,foldname)
	
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E6%89%8B%E8%A1%A8%E5%A5%B3&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i+5,foldname)			
		
#7.10 hair_jewelry
def scratch_imgs_hair_jewelry():
	foldname = "7_hair_jewelry"
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E5%8F%91%E9%A5%B0&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i,foldname)			
		
def scratch_imgs_accessory():
	scratch_imgs_hat()
	scratch_imgs_scaf()
	scratch_imgs_kerchief()
	scratch_imgs_tie()
	scratch_imgs_bowtie()
	scratch_imgs_belt()
	scratch_imgs_glove()
	scratch_imgs_glasses()
	scratch_imgs_watch()
	scratch_imgs_hair_jewelry()
	
	
#8.1 necklace
def scratch_imgs_necklace():
	foldname = "8_necklace"
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E9%A1%B9%E9%93%BE%E7%94%B7&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i,foldname)
	
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E9%A1%B9%E9%93%BE+%E5%A5%B3&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i+5,foldname)	
		
#8.2 earrings
def scratch_imgs_earrings():
	foldname = "8_earrings"
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E8%80%B3%E7%8E%AF%E7%94%B7&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i,foldname)
	
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E8%80%B3%E7%8E%AF%E5%A5%B3&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i+5,foldname)	
		
#8.3 earstud
def scratch_imgs_earstud():
	foldname = "8_earstud"
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E8%80%B3%E9%92%89%E7%94%B7&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i,foldname)
	
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E8%80%B3%E9%92%89%E5%A5%B3&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i+5,foldname)				
		
#8.4 fingerring
def scratch_imgs_fingerring():
	foldname = "8_fingerring"
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E6%88%92%E6%8C%87%E7%94%B7&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i,foldname)
	
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E6%88%92%E6%8C%87%E5%A5%B3&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i+5,foldname)		
		
#8.5 bracelet
def scratch_imgs_bracelet():
	foldname = "8_bracelet"
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E6%89%8B%E9%93%BE%E5%A5%B3&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i,foldname)
	
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E6%89%8B%E9%93%BE%E7%94%B7&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i+5,foldname)				
		
#8.6 bangle
def scratch_imgs_bangle():
	foldname = "8_bangle"
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E6%89%8B%E9%95%AF%E7%94%B7&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i,foldname)
	
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E6%89%8B%E9%95%AF%E5%A5%B3&page="
	mkdir(foldname)
	for i in range(1,5,1):
		html = download_page(url+str(i))
		get_image(html,i+5,foldname)			
		
def scratch_imgs_jewelry():
	scratch_imgs_necklace()
	scratch_imgs_earrings()
	scratch_imgs_earstud()
	scratch_imgs_fingerring()
	scratch_imgs_bracelet()
	scratch_imgs_bangle()


def scratch_imgs():
	print("scratch_imgs clothes start!")
	#scratch_imgs_clothes()
	print("scratch_imgs pants start!")
	#scratch_imgs_pants()
	print("scratch_imgs skirt start!")
	#scratch_imgs_skirt()
	print("scratch_imgs suit start!")
	#scratch_imgs_suit()
	
	print("scratch_imgs shoes start!")
	scratch_imgs_shoes()
	print("scratch_imgs bags start!")
	scratch_imgs_bags()
	print("scratch_imgs accessory start!")
	scratch_imgs_accessory()
	
			
scratch_imgs()

gc.collect()
#t = threading.Thread(target=target)	
#t.start()
#t.join()	