import urllib
import urllib.request
import re
import ssl
import bs4
import time
import threading
import os
import gc


def download_page(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}
    request = urllib.request.Request(url, headers=headers)
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(request, context=context)
    data = response.read()
    return data


def get_image(html,name,foldname):
    regx = r'http://[\S]*\.jpg'
    # regx = r'http:[^s]*?(jpg|png|gif)'
    pattern = re.compile(regx)
    print(pattern)
    # pattern = r'(http:[^s]*?(jpg|png|gif))'
    get_img = re.findall(pattern, repr(html))
    len_imglist= len(get_img)
    print("len_imglist:\n",len_imglist)
    num = 1
    
    for img in get_img:
        print(img)
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
		#os.chdir(foldname)

"""
def get_image(url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    get_image = response.read()

    with open('001.jpg', 'wb') as fp:
        fp.write(get_image)
        print("download 001.jpg")

"""

#url = "https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&fm=detail&lm=-1&st=-1&sf=2&fmq=&fm=detail&pv=&ic=0&nc=1&z=&se=&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&hs=2&word=jewelry"
#url = "https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=jewelry%20image&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=111111"
#jewelry
#url="https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1513675580925_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&hs=2&word=hairpin"

#bags_suitcases
url="http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=%C6%A4%D0%AC&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=000000"
#print(bs4)

def target():
	foldname = "jewelry"
	mkdir(foldname)
	for i in range(555,1000,111):
		html = download_page(url+str(i))
		get_image(html,i,foldname)
	
def scratch_imgs(url):
	foldname = "shoes"
	name="shoe25"
	mkdir(foldname)
	print("scratch_imgs start!")
	html = download_page(url)
	get_image(html,name,foldname)
	print("scratch_imgs success!")
	
	
scratch_imgs(url)	
gc.collect()
#t = threading.Thread(target=target)	
#t.start()
#t.join()	