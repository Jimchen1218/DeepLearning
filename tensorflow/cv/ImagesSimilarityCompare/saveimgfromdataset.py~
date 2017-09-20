'''
name:saveimgfromdataset.py
create date:8/28/2017
author:jimchen
'''

import tensorflow as tf
import seaborn as sb
from matplotlib.pylab import date2num
import matplotlib.pyplot as plt
import matplotlib.finance as mpf
import matplotlib.image as mpimg
import numpy as np   
from scipy import misc  
from PIL import Image
import pandas as pd
import os
import json
import re
import datetime
import argparse
import sys
import tempfile
import time


KLINE_DATA_PLACE_DIR = "/origdata/"
IMGS_PLACE_DIR = "/images/"

def CheckIsExist(fullpath):
	fullpath=fullpath.strip()
	if(not os.path.exists(fullpath)):
		print("CheckIsExist file is not exist!")
		return False
	else:
		return True
		
def CreateDirectory(dirname):
    cwd=os.getcwd()
    full_path=cwd+dirname
    full_path=full_path.strip()
    #print("CreateDirectory full_path:",full_path)
    if(not os.path.exists(full_path)):
        print("CreateDirectory file is not exist!")
        os.mkdir(full_path)
    return full_path


def parseDatasetfromfile(filename):
	lows=[]
	opens=[]
	highs=[]
	closes=[]
	cwd=os.getcwd()
	full_path=cwd+filename
	print("full_path:",full_path)
	isExist=CheckIsExist(full_path)
	if not isExist:
		return lows,highs,opens,closes
	f=open(full_path, 'rb')
	lines=f.readlines()
	i=0
	for line in lines:
		line=line.strip()[:-2][1:]
		info=str(line).split(',')
		#print("info[0]:%s,info[1]:%s,info[3]:%s,info[4]:%s,info[5]:%s"%(info[0],info[1],info[3],info[4],info[5]))
		low = info[0].split(':')[1]
		low=low.strip('"')
		f_low=float(low)
		#print("f_low:",f_low)
		lows.append(f_low)
		opens.append(float(info[1].split(':')[1].strip('"')))
		highs.append(float(info[4].split(':')[1].strip('"')))
		closes.append(float(info[5][:-1].split(':')[1].strip('"')))
		i=i+1
	f.close()
	return lows,highs,opens,closes

def showKLine(opens,closes,highs,lows):
	fig = plt.figure()
	ax = fig.add_subplot(111)
	mpf.candlestick2_ochl(ax, opens, closes, highs, lows, width=0.3, colorup='r', colordown='g', alpha=1)
	plt.show()
	
def saveKLine(i,opens,closes,highs,lows,image_path):
	fig = plt.figure()
	ax = fig.add_subplot(111)
	mpf.candlestick2_ochl(ax, opens, closes, highs, lows, width=0.3, colorup='r', colordown='g', alpha=1)
	images_path = CreateDirectory(image_path)
	save_name = str(i+1)+".png"
	images_full_path= images_path+save_name
	print("saveKLine images_full_path:",images_full_path)
	plt.savefig(images_full_path)
	plt.close('all')

def main(_):
    dataset_filename = KLINE_DATA_PLACE_DIR+"1.txt"
    print("main dataset_filename:",dataset_filename)
    lows,highs,opens,closes = parseDatasetfromfile(dataset_filename)
    num_k=len(lows)
    print("parseDatasetfromfile num_k:%s \nlows:%s,\nopens:%s,\nhighs:%s,\ncloses:%s"%(num_k,lows,opens,highs,closes))
    starttime=time.time()
    for i in range(3000):
        lows[i%num_k]=lows[i%num_k]+0.001*i
        opens[i%num_k]=opens[i%num_k]+0.001*i
        highs[i%num_k]=highs[i%num_k]+0.001*i
        closes[i%num_k]=closes[i%num_k]+0.001*i
        saveKLine(i,opens,closes,highs,lows,IMGS_PLACE_DIR)
    duration=time.time()-starttime
    print("main duration:",duration)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.register("type", "bool", lambda v: v.lower() == "true")
    FLAGS, unparsed = parser.parse_known_args()
    tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)
