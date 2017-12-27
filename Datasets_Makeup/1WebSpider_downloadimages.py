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

def mkdir(foldname):
		if not os.path.exists(foldname):
			os.mkdir(foldname)

def get_image(html,i,foldname):
    #regx = r'http://[\S]*\.jpg'  #baidu
    # regx = r'http:[^s]*?(jpg|png|gif)'
    #regx = r'<img src=\"(.*?)\"'  #360
    regx = r'data-original=\"(.*?)\"'
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
        with open('%s/%d_%s.jpg' %(foldname,i,num), 'wb') as fp:
            fp.write(image)
            time.sleep(1)
            print("download %s" % num)
            num += 1	
    return

def scratch_imgs_from_zhe800():
	foldname = "T_shirt"
	url= ["https://search.zhe800.com/search?keyword=%E7%9F%AD%E8%A2%96T%E6%81%A4%E5%A5%B3%E7%AB%A5",]
	mkdir(foldname)
	for index, item in enumerate(url):
		html = download_page(item)
		get_image(html,index+15,foldname)

	
def scratch_imgs_from_vancl():
	foldname = "T_shirt"
	url="http://catalog.vancl.com/xbxx.html#ref=hp-hp-head-nav_6-v:n"
	mkdir(foldname)
	html = download_page(url)
	get_image(html,111,foldname)

def scratch_imgs():
	print("scratch_imgs clothes start!")
	scratch_imgs_from_zhe800()
	#scratch_imgs_from_vancl()

			
scratch_imgs()

gc.collect()
#t = threading.Thread(target=target)	
#t.start()
#t.join()	