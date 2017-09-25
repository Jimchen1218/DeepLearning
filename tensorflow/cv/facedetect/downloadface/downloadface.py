'''
name:test_cnn_predict.py
create_date:9/15/2017
author:jimchen1218@sina.com
purpose:Traffic Sign Recognition .The goal is to build a model that can detect and classify traffic signs in a video stream taken from a moving car.
'''

from bs4 import BeautifulSoup  
import urllib.request  
import urllib.parse  
import os  

import threading  

#import opencv2  as cv2
import numpy as np  

keyword={  
        "face":["http://cn.bing.com/images/async?q=face+people&qft=+filterui%3aface-face+filterui%3aphoto-photo&lostate=r&mmasync=1&dgState=x*410_y*1029_h*166_c*2_i*71_r*12&IG=2F30F17499C7450DBFAFA355CA1BE527&SFX=3&iid=images.5622",  
                "http://cn.bing.com/images/async?q=human&qft=+filterui%3aface-portrait&lostate=r&mmasync=1&dgState=x*694_y*1201_h*164_c*3_i*36_r*7&IG=6D13393FAE2C46C1B74D874BBE395415&SFX=2&iid=images.5725",  
                "http://cn.bing.com/images/async?q=handsome&qft=+filterui%3aface-face&lostate=r&mmasync=1&dgState=x*524_y*1065_h*202_c*3_i*36_r*6&IG=B57823857E2843CE87EDB655B7F7F334&SFX=2&iid=images.5709",  
                "http://cn.bing.com/images/async?q=beautiful+girl&qft=+filterui%3aface-face&lostate=r&mmasync=1&dgState=x*745_y*1194_h*187_c*4_i*36_r*7&IG=55BB00BABF4F478B9060D6A3A19C1B65&SFX=2&iid=images.5670",  
                "http://cn.bing.com/images/async?q=%e5%b8%85%e5%93%a5&relo=3&qft=+filterui%3aface-face&lostate=c&mmasync=1&dgState=c*7_y*1257s1212s1226s1472s1213s1410s1427_i*39_w*181&IG=6D566BBDC2C4448ABB98B2DDBFAED030&SFX=2&iid=images.5754",  
                "http://cn.bing.com/images/async?q=%e7%be%8e%e5%a5%b3&qft=+filterui%3aface-face&lostate=r&mmasync=1&dgState=x*486_y*1004_h*192_c*2_i*36_r*6&IG=40A17665192F4434A72B70C4390C64E8&SFX=2&iid=images.5653",  
                "http://cn.bing.com/images/async?q=%e4%ba%ba%e7%89%a9%e5%9b%be%e7%89%87&relo=3&qft=+filterui%3aface-face&lostate=c&mmasync=1&dgState=c*7_y*1430s1159s1189s1250s1358s1183s1285_i*39_w*181&IG=2245EBFC2E5D4104BAE25B78BD3F9B99&SFX=2&iid=images.5682"],  
        "body":["http://cn.bing.com/images/async?q=Group+photo+friends&qft=+filterui%3aface-portrait&lostate=r&mmasync=1&dgState=x*0_y*0_h*0_c*5_i*211_r*37&IG=61B156F4951A445FABD823619621B21A&SFX=7&iid=images.5622",  
                "http://cn.bing.com/images/async?q=street+young+man+woman+photo&lostate=r&mmasync=1&dgState=x*870_y*1226_h*195_c*3_i*71_r*13&IG=A6DBFAAFB9F246C58CA1C6E48D7B9EC8&SFX=3&iid=images.5678",  
                "http://cn.bing.com/images/async?q=%e5%90%88%e7%85%a7&lostate=r&mmasync=1&dgState=x*0_y*0_h*0_c*4_i*281_r*47&IG=38AADDB045FA476A874BCE211808938A&SFX=9&iid=images.5725"  
                ],  
        "background":["http://cn.bing.com/images/async?q=outdoor&lostate=r&mmasync=1&dgState=x*529_y*1137_h*184_c*2_i*211_r*42&IG=36C7889B63534668B101BA10E4200710&SFX=7&iid=images.5713",  
                      "http://cn.bing.com/images/async?q=%e9%a3%8e%e6%99%af&lostate=r&mmasync=1&dgState=x*0_y*0_h*0_c*5_i*71_r*14&IG=844AED80FBB44BEDA47A7D2201D6D642&SFX=3&iid=images.5725"]  
         }  
  
##############################################################  
  
def checkDir():  
    if os.path.exists("./data")==False:  
        os.mkdir("./data")  
    for subDir in list(keyword.keys()):  
        if os.path.exists("./data/"+subDir)==False:  
            os.mkdir("./data/"+subDir)  
  
def writeData(data,tag,name):  
    image = np.asarray(bytearray(data), dtype="uint8")  
#    image = cv2.imdecode(image, cv2.IMREAD_COLOR)  
#   cv2.imwrite("./data/"+tag+"/"+name+".jpg", cv2.resize(image,(128,128)))  
  
##################################################################  
  
globalSet=set()  
  
class imageUrlGeter:  
    def __init__(self,url,getIndex,start,end):  
        self.url=url  
        self.getIndex=getIndex  
        self.curIndex=start  
        self.maxIndex=end  
        self.urlList=[]  
        self.urlSet=globalSet  
  
    def __iter__(self):  
        return self  
  
    def pushImageUrl(self):  
        while True:  
            try:  
                text=urllib.request.urlopen(self.url+"&count=20&relp=20"+"&first="+str(self.getIndex)).read()  
                break  
            except Exception:  
                print("exception raised when get image url")  
        html=str(text,encoding = "utf-8")  
  
        self.getIndex+=20  
  
        tempList=[]  
        soup=BeautifulSoup(html)  
        images=soup.find_all(name="img",class_="mimg")  
        for image in images:  
            url=image.get("src")  
            param=urllib.parse.parse_qs(urllib.parse.urlparse(url).query)  
            if param["id"][0] in self.urlSet:  
                continue  
            self.urlSet.add(param["id"][0])  
            tempList.append(url)  
        if len(tempList)<=0:  
            raise StopIteration()  
        self.urlList+=tempList  
  
    def __next__(self):  
        if self.curIndex>=self.maxIndex:  
            raise StopIteration()  
        if len(self.urlList)==0:  
            self.pushImageUrl()  
        cur=self.curIndex  
        self.curIndex+=1  
        return self.urlList.pop(0),cur  
  
def downloadFun(geter,key):  
    for url,index in geter:  
        try:  
            data = urllib.request.urlopen(url).read()  
            writeData(data, key, str(index))  
        except Exception:  
            print("image " + str(index) + " skiped")  
  
  
def startDownload(url,key,start,end):  
    numOfThread=32  
    threadList=[]  
    perThread=int((end-start)/numOfThread)  
  
    for i in range(numOfThread):  
        urlGeter=imageUrlGeter(url,i*perThread,start+i*perThread,start+(i+1)*perThread)  
        thread=threading.Thread(target=downloadFun,args=[urlGeter,key])  
        thread.setDaemon(True)  
        threadList.append(thread)  
        thread.start()  
  
    for thread in threadList:  
        thread.join()  
  
def downLoadImages(dic):  
    for key in list(dic):  
        i=0  
        urlList=keyword[key]  
        for url in urlList:  
            startDownload(url,key,i*5000,(i+1)*5000)  
            i+=1  
  
if __name__=="__main__":  
    checkDir()  
    downLoadImages(keyword)  
