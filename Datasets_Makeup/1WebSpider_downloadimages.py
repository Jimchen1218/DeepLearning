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
		return data

def mkdir(foldname):
		if not os.path.exists(foldname):
			os.mkdir(foldname)

def get_image(html,i,foldname):
    regx = r'\"middleURL\":\"(https:\/\/.*?\.jpg)\"'
    pattern = re.compile(regx)
    get_img = re.findall(pattern, repr(html))
    for img in get_img:
    	print(img)
    print('\n')
    len_imglist= len(get_img)
    print("len_imglist:\n",len_imglist)
    num = 1
    for img in get_img:
        print(img)
        if not img.startswith('http'):
        	img= "http:"+img
        
        image = download_page(img)
        with open('%s/%d_%s.jpg' %(foldname,i,num), 'wb') as fp:
            fp.write(image)
            time.sleep(1)
            print("download %s" % num)
            num += 1
    return

#----------------------------------------	
#1.Upperwear
#----------------------------------------	
def scratch_imgs_overcoat():
	print("scratch_imgs_overcoat start!")
	foldname = "1_1Overcoat"
	url= [#"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515121431325_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E5%A4%A7%E8%A1%A3",
	#"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515121446628_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E5%A4%A7%E8%A1%A32018",
	"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515121832590_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E5%A4%A7%E8%A1%A32017",]
	mkdir(foldname)
	for index, item in enumerate(url):
		html = download_page(item)
		get_image(html,index+1,foldname)
		
def scratch_imgs_coat():
	print("scratch_imgs_coat start!")
	foldname = "1_2Coat"
	url= [#"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515121918794_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E5%A4%96%E5%A5%972017",
	"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515121948321_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E5%A4%96%E5%A5%972018",]
	mkdir(foldname)
	for index, item in enumerate(url):
		html = download_page(item)
		get_image(html,index+1,foldname)		
			
def scratch_imgs_sweater():
	print("scratch_imgs_coat start!")
	foldname = "1_3Sweater"
	url= [#"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515121974907_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E6%AF%9B%E8%A1%A32018",
	"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515122085815_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E6%AF%9B%E8%A1%A3",]
	mkdir(foldname)
	for index, item in enumerate(url):
		html = download_page(item)
		get_image(html,index+1,foldname)	

def scratch_imgs_shirt():
	print("scratch_imgs_shirt start!")
	foldname = "1_4Shirt"
	url= [#"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515122128626_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E8%A1%AC%E8%A1%AB",
	"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515122138903_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E8%A1%AC%E8%A1%AB2018",]
	mkdir(foldname)
	for index, item in enumerate(url):
		html = download_page(item)
		get_image(html,index+1,foldname)		
		
def scratch_imgs_fleece():
	print("scratch_imgs_fleece start!")
	foldname = "1_5Fleece"
	url= [#"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515122181978_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E5%8D%AB%E8%A1%A3",
	"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515122193847_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E5%8D%AB%E8%A1%A32018",]
	mkdir(foldname)
	for index, item in enumerate(url):
		html = download_page(item)
		get_image(html,index+1,foldname)			

def scratch_imgs_Tshirt():
	print("scratch_imgs_Tshirt start!")
	foldname = "1_6Tshirt"
	url= [#"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515122286990_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=T%E6%81%A4",
	"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515122302157_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=T%E6%81%A42018",]
	mkdir(foldname)
	for index, item in enumerate(url):
		html = download_page(item)
		get_image(html,index+1,foldname)
		

#----------------------------------------			
#2.Trousers		
#----------------------------------------	
def scratch_imgs_Tailoredtrousers():
	print("scratch_imgs_Tailoredtrousers start!")
	foldname = "2_1Tailoredtrousers"
	url= [#"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515122462397_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E8%A5%BF%E8%A3%A4",
	"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515122474084_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E8%A5%BF%E8%A3%A42018",]
	mkdir(foldname)
	for index, item in enumerate(url):
		html = download_page(item)
		get_image(html,index+1,foldname)		
		
def scratch_imgs_Casualtrousers():
	print("scratch_imgs_Casualtrousers start!")
	foldname = "2_2Casualtrousers"
	url= [#"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515122785302_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E4%BC%91%E9%97%B2%E8%A3%A4",
	"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515122794386_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E4%BC%91%E9%97%B2%E8%A3%A42018",]
	mkdir(foldname)
	for index, item in enumerate(url):
		html = download_page(item)
		get_image(html,index+1,foldname)				
					
def scratch_imgs_Jeanstrousers():
	print("scratch_imgs_Jeanstrousers start!")
	foldname = "2_3Jeanstrousers"
	url= [#"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515122856467_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E7%89%9B%E4%BB%94%E8%A3%A4",
	"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515122866981_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E7%89%9B%E4%BB%94%E8%A3%A42018",]
	mkdir(foldname)
	for index, item in enumerate(url):
		html = download_page(item)
		get_image(html,index+1,foldname)				
					
def scratch_imgs_Sporttrousers():
	print("scratch_imgs_Sporttrousers start!")
	foldname = "2_4Sporttrousers"
	url= [#"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515122915822_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E8%BF%90%E5%8A%A8%E8%A3%A4",
	"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515122950574_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E8%BF%90%E5%8A%A8%E8%A3%A42018",]
	mkdir(foldname)
	for index, item in enumerate(url):
		html = download_page(item)
		get_image(html,index+1,foldname)				


#----------------------------------------	
#3.Skirt	
#----------------------------------------		
def scratch_imgs_Suspenderskirt():
	print("scratch_imgs_Suspenderskirt start!")
	foldname = "3_1Suspenderskirt"
	url= [#"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515123042423_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E5%8D%8A%E8%BA%AB%E8%A3%99",
	"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515123053780_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E5%8D%8A%E8%BA%AB%E8%A3%992018",]
	mkdir(foldname)
	for index, item in enumerate(url):
		html = download_page(item)
		get_image(html,index+1,foldname)						

def scratch_imgs_Bustdress():
	print("scratch_imgs_Bustdress start!")
	foldname = "3_2Bustdress"
	url= [#"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515123139107_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E8%BF%9E%E8%A1%A3%E8%A3%99&f=3&oq=%E8%BF%9E&rsp=0",
	"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515123152488_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E8%BF%9E%E8%A1%A3%E8%A3%992018",]
	mkdir(foldname)
	for index, item in enumerate(url):
		html = download_page(item)
		get_image(html,index+1,foldname)		
									
def scratch_imgs_Onepieceskirt():
	print("scratch_imgs_Onepieceskirt start!")
	foldname = "3_3Onepieceskirt"
	url= [#"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515123257074_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E8%83%8C%E5%B8%A6%E8%A3%99",
	"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515123275343_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E8%83%8C%E5%B8%A6%E8%A3%992018",]
	mkdir(foldname)
	for index, item in enumerate(url):
		html = download_page(item)
		get_image(html,index+1,foldname)										


#----------------------------------------	
#5.Shoes	
#----------------------------------------		
def scratch_imgs_Gymshoes():
	print("scratch_imgs_Gymshoes start!")
	foldname = "5_1Gymshoes"
	url= [#"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515123340547_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E8%BF%90%E5%8A%A8%E9%9E%8B&f=3&oq=%E8%BF%90%E5%8A%A8&rsp=1",
	"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515123349997_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E8%BF%90%E5%8A%A8%E9%9E%8B2018",]
	mkdir(foldname)
	for index, item in enumerate(url):
		html = download_page(item)
		get_image(html,index+1,foldname)						

def scratch_imgs_Leisureshoes():
	print("scratch_imgs_Leisureshoes start!")
	foldname = "5_2Leisureshoes"
	url= [#"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515123397643_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E4%BC%91%E9%97%B2%E9%9E%8B",
	"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515123424475_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E4%BC%91%E9%97%B2%E9%9E%8B2018",]
	mkdir(foldname)
	for index, item in enumerate(url):
		html = download_page(item)
		get_image(html,index+1,foldname)		
									
def scratch_imgs_Leathershoes():
	print("scratch_imgs_Leathershoes start!")
	foldname = "5_3Leathershoes"
	url= [#"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515123474468_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E7%9A%AE%E9%9E%8B",
	"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515123488588_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E7%9A%AE%E9%9E%8B2018",]
	mkdir(foldname)
	for index, item in enumerate(url):
		html = download_page(item)
		get_image(html,index+1,foldname)

def scratch_imgs_Bootsshoes():
	print("scratch_imgs_Bootsshoes start!")
	foldname = "5_4Bootsshoes"
	url= [#"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515123602476_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E9%9D%B4",
	"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515123623017_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E9%9D%B42018",]
	mkdir(foldname)
	for index, item in enumerate(url):
		html = download_page(item)
		get_image(html,index+1,foldname)						

def scratch_imgs_Sandalshoes():
	print("scratch_imgs_Sandalshoes start!")
	foldname = "5_5Sandalshoes"
	url= [#"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515123697551_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E5%87%89%E9%9E%8B",
	"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515123706752_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E5%87%89%E9%9E%8B2018",]
	mkdir(foldname)
	for index, item in enumerate(url):
		html = download_page(item)
		get_image(html,index+1,foldname)		

def scratch_imgs_Slippershoes():
	print("scratch_imgs_Slippershoes start!")
	foldname = "5_6Slippershoes"
	url= [#"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515123724519_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E6%8B%96%E9%9E%8B",
	"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515123734232_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E6%8B%96%E9%9E%8B2018",]
	mkdir(foldname)
	for index, item in enumerate(url):
		html = download_page(item)
		get_image(html,index+1,foldname)
						
								
#----------------------------------------													
#6.bagsandcases		
#----------------------------------------	
def scratch_imgs_Backpack():
	print("scratch_imgs_Backpack start!")
	foldname = "6_1Backpack"
	url= [#"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515123839273_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E5%8F%8C%E8%82%A9%E5%8C%85",
	"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515123851766_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E5%8F%8C%E8%82%A9%E5%8C%852018",]
	mkdir(foldname)
	for index, item in enumerate(url):
		html = download_page(item)
		get_image(html,index+1,foldname)						

def scratch_imgs_Shoulderbag():
	print("scratch_imgs_Shoulderbag start!")
	foldname = "6_2Shoulderbag"
	url= [#"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515123887875_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E5%8D%95%E8%82%A9%E5%8C%85",
	"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515123898750_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E5%8D%95%E8%82%A9%E5%8C%852018",]
	mkdir(foldname)
	for index, item in enumerate(url):
		html = download_page(item)
		get_image(html,index+1,foldname)		

def scratch_imgs_Handbag():
	print("scratch_imgs_Handbag start!")
	foldname = "6_3Handbag"
	url= [#"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515123949098_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E6%89%8B%E6%8F%90%E5%8C%85",
	"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515123961238_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E6%89%8B%E6%8F%90%E5%8C%852018",]
	mkdir(foldname)
	for index, item in enumerate(url):
		html = download_page(item)
		get_image(html,index+1,foldname)

def scratch_imgs_Clutchbag():
	print("scratch_imgs_Clutchbag start!")
	foldname = "6_4Clutchbag"
	url= [#"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515124001694_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E6%89%8B%E6%8B%BF%E5%8C%85",
	"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515124017386_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E6%89%8B%E6%8B%BF%E5%8C%852018",]
	mkdir(foldname)
	for index, item in enumerate(url):
		html = download_page(item)
		get_image(html,index+1,foldname)						

def scratch_imgs_Wallet():
	print("scratch_imgs_Wallet start!")
	foldname = "6_5Wallet"
	url= [#"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515124048671_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E9%92%B1%E5%8C%85",
	"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515124106044_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E9%92%B1%E5%8C%852018",]
	mkdir(foldname)
	for index, item in enumerate(url):
		html = download_page(item)
		get_image(html,index+1,foldname)		

def scratch_imgs_Suitcase():
	print("scratch_imgs_Suitcase start!")
	foldname = "6_6Suitcase"
	url= [#"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515124151968_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E6%97%85%E8%A1%8C%E7%AE%B1",
	"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515124170893_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E6%97%85%E8%A1%8C%E7%AE%B12018",]
	mkdir(foldname)
	for index, item in enumerate(url):
		html = download_page(item)
		get_image(html,index+1,foldname)												
	

#----------------------------------------	
#7.Accessory		
#----------------------------------------
def scratch_imgs_Hat():
	print("scratch_imgs_Hat start!")
	foldname = "7_1Hat"
	url= ["https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515124447990_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E5%B8%BD%E5%AD%90",]
	mkdir(foldname)
	for index, item in enumerate(url):
		html = download_page(item)
		get_image(html,index+1,foldname)						

def scratch_imgs_Tie():
	print("scratch_imgs_Tie start!")
	foldname = "7_2Tie"
	url= ["https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515124484142_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E9%A2%86%E5%B8%A6",]
	mkdir(foldname)
	for index, item in enumerate(url):
		html = download_page(item)
		get_image(html,index+1,foldname)		

def scratch_imgs_Bowtie():
	print("scratch_imgs_Bowtie start!")
	foldname = "7_3Bowtie"
	url= ["https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515124523477_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E9%A2%86%E7%BB%93",]
	mkdir(foldname)
	for index, item in enumerate(url):
		html = download_page(item)
		get_image(html,index+1,foldname)

def scratch_imgs_Belt():
	print("scratch_imgs_Belt start!")
	foldname = "7_4Belt"
	url= ["https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515124554033_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E8%85%B0%E5%B8%A6",]
	mkdir(foldname)
	for index, item in enumerate(url):
		html = download_page(item)
		get_image(html,index+1,foldname)						

def scratch_imgs_Glove():
	print("scratch_imgs_Glove start!")
	foldname = "7_5Glove"
	url= ["https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515124583531_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E6%89%8B%E5%A5%97",]
	mkdir(foldname)
	for index, item in enumerate(url):
		html = download_page(item)
		get_image(html,index+1,foldname)		

def scratch_imgs_Glasses():
	print("scratch_imgs_Glasses start!")
	foldname = "7_6Glasses"
	url= ["https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515124626011_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E7%9C%BC%E9%95%9C",]
	mkdir(foldname)
	for index, item in enumerate(url):
		html = download_page(item)
		get_image(html,index+1,foldname)

def scratch_imgs_Watch():
	print("scratch_imgs_Watch start!")
	foldname = "7_7Watch"
	url= ["https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515124667607_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E6%89%8B%E8%A1%A8",]
	mkdir(foldname)
	for index, item in enumerate(url):
		html = download_page(item)
		get_image(html,index+1,foldname)				
		
		
#----------------------------------------	
#8.Jewelry		
#----------------------------------------
def scratch_imgs_Necklace():
	print("scratch_imgs_Necklace start!")
	foldname = "8_1Necklace"
	url= ["https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515124780773_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E9%A1%B9%E9%93%BE",]
	mkdir(foldname)
	for index, item in enumerate(url):
		html = download_page(item)
		get_image(html,index+1,foldname)						

def scratch_imgs_Earrings():
	print("scratch_imgs_Earrings start!")
	foldname = "8_2Earrings"
	url= ["https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515124831642_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E8%80%B3%E9%A5%B0",]
	mkdir(foldname)
	for index, item in enumerate(url):
		html = download_page(item)
		get_image(html,index+1,foldname)		
										
def scratch_imgs_Fingerring():
	print("scratch_imgs_Fingerring start!")
	foldname = "8_3Fingerring"
	url= ["https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515124865242_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E6%88%92%E6%8C%87",]
	mkdir(foldname)
	for index, item in enumerate(url):
		html = download_page(item)
		get_image(html,index+1,foldname)

def scratch_imgs_Bangle():
	print("scratch_imgs_Bangle start!")
	foldname = "8_4Bangle"
	url= ["https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515124926257_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E6%89%8B%E9%95%AF",]
	mkdir(foldname)
	for index, item in enumerate(url):
		html = download_page(item)
		get_image(html,index+1,foldname)						
		
			
def scratch_imgs():
	#1.Upperwear
	scratch_imgs_overcoat()
	scratch_imgs_coat()
	scratch_imgs_sweater()
	scratch_imgs_shirt()
	scratch_imgs_fleece()
	scratch_imgs_Tshirt()
	#2.Trousers		
	scratch_imgs_Tailoredtrousers()
	scratch_imgs_Casualtrousers()
	scratch_imgs_Jeanstrousers()
	scratch_imgs_Sporttrousers()
	#3.Skirt	
	scratch_imgs_Suspenderskirt()
	scratch_imgs_Bustdress()
	scratch_imgs_Onepieceskirt()
	#5.Shoes	
	scratch_imgs_Gymshoes()
	scratch_imgs_Leisureshoes()
	scratch_imgs_Leathershoes()
	scratch_imgs_Bootsshoes()
	scratch_imgs_Sandalshoes()
	scratch_imgs_Slippershoes()
	#6.bagsandcases							
	scratch_imgs_Backpack()		
	scratch_imgs_Shoulderbag()			
	scratch_imgs_Handbag()
	scratch_imgs_Clutchbag()
	scratch_imgs_Wallet()
	scratch_imgs_Suitcase()
	#7.Accessory	
	scratch_imgs_Hat()
	scratch_imgs_Tie()				
	scratch_imgs_Bowtie()
	scratch_imgs_Belt()
	scratch_imgs_Glove()		
	scratch_imgs_Glasses()	
	scratch_imgs_Watch()	
	#8.Jewelry	
	scratch_imgs_Necklace()
	scratch_imgs_Earrings()
	scratch_imgs_Fingerring()
	scratch_imgs_Bangle()
			
												
def main():
		starttime=time.time()
		scratch_imgs()
		gc.collect()
		duration=time.time()-starttime
		print("main duration:",duration)

if __name__ == "__main__":
	main()

