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

def scratch_imgs_from_multiURL(url,foldname):
	mkdir(foldname)
	for i in range(0,10,1):
		html = download_page(url+str(i))
		get_image(html,i,foldname)
	
def scratch_imgs_bags():
	foldname = "taobao_boxes"
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E7%AE%B1%E5%8C%85&page="
	mkdir(foldname)
	for i in range(0,10,1):
		html = download_page(url+str(i))
		get_image(html,i,foldname)	
	
def scratch_imgs_shoes():
	foldname = "taobao_shoes"
	#shoe
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E9%9E%8B&page="
	#afwx
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E9%9D%B4&page="
	mkdir(foldname)
	for i in range(0,20,1):
		html = download_page(url+str(i))
		get_image(html,i+30,foldname)
	
def scratch_imgs_jewelry():
	foldname = "taobao_jewelry"
	url="http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=508712bfca2dd4cea1baa3a486d10036&keyword=%E9%A6%96%E9%A5%B0&page="
	mkdir(foldname)
	for i in range(0,20,1):
		html = download_page(url+str(i))
		get_image(html,i,foldname)	
	
#jewelry


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
		
def scratch_imgs_clothes():		
		scratch_imgs_clothes_overcoat()
		scratch_imgs_clothes_coat()
		scratch_imgs_clothes_sweater()
		scratch_imgs_clothes_shirt()
		scratch_imgs_clothes_fleece()
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
		
def scratch_imgs_suit():
	scratch_imgs_clothes_tailored_suit()
	scratch_imgs_clothes_sweat_suit()
	scratch_imgs_clothes_leisure_suit()


def scratch_imgs():
	print("scratch_imgs clothes start!")
	scratch_imgs_clothes()
	print("scratch_imgs pants start!")
	scratch_imgs_pants()
	print("scratch_imgs skirt start!")
	scratch_imgs_skirt()
	print("scratch_imgs suit start!")
	scratch_imgs_suit()
	
			
scratch_imgs()

gc.collect()
#t = threading.Thread(target=target)	
#t.start()
#t.join()	