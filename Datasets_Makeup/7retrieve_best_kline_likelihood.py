'''
name:retrieve_best_kline_likelihood.py
create date:1/3/2018
author:jimchen
'''

from comparesimilarity import histcmpsimilar

#import tensorflow as tf
import sys
import os
import shutil
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image
import matplotlib.finance as mpf
import math
import glob
import time
import operator


#micro define here...
HIGHEST_SIMILARITY_IMAGES_NUMBER = 3

IMAGE_RESIZE_WIDTH = 640
IMAGE_RESIZE_HEIGHT = 480
IMAGE_CMPSIZE_WIDTH = 32
IMAGE_CMPSIZE_HEIGHT = 32

MANUAL_SELECTION_IMAGE_ID= '600130'

KLINE_DATA_PLACE_DIR = "/origdata/"
IMGS_PLACE_DIR = "/kline_images/"

PREFER_IMGS_PLACE_DIR = "/pickup_kline_image/"

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

def getallklinedatainpath():
    paths=[]
    cwd=os.getcwd()
    klinedata_path=cwd+KLINE_DATA_PLACE_DIR
    isExist = CheckIsExist(klinedata_path)
    if(not isExist):
        return Null
        
    for file_name in os.listdir(klinedata_path):
        if file_name.endswith('txt'):
            #filefullpath = os.path.join(klinedata_path, file_name)
            paths.append(file_name)
     
    paths.sort(key= lambda x:int(x[:-4]))
    #print("generatefullpath paths:", paths)
    #for i in range(len(paths)):
    #    paths[i] = os.path.join(klinedata_path, paths[i])
    return paths

def parseDatasetfromfile(filename):
	lows=[]
	opens=[]
	highs=[]
	closes=[]
	kline_data = []
	cwd=os.getcwd()
	full_path=cwd+KLINE_DATA_PLACE_DIR+filename
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
	len = i
	#print("generateklineimgs len:",len)
	j = 0
	for j in range(len):
		kline_data.append(lows[j])
		kline_data.append(highs[j])
		kline_data.append(opens[j])
		kline_data.append(closes[j])
	return kline_data


def generateklineimgs():
		#dataset_filename= []
		dataset_filename = getallklinedatainpath()
		totalnum_files = len(dataset_filename)
		print("generateklineimgs totalnum_files:",totalnum_files)
		for i in range(totalnum_files):
				kline_data = parseDatasetfromfile(dataset_filename[i])
				print("generateklineimgs \nkline_data:%s"%(kline_data))
				#name_id = os.path.splitext(dataset_filename[i].split('/'))[-1]
				name_id = dataset_filename[i].split("/")[-1].split(".")[0]
				print("generateklineimgs name_id:",name_id)
				#if not math.isclose(opens[0],0.0):
				#saveKLine(name_id,opens,closes,highs,lows,IMGS_PLACE_DIR)
		num_k=len(kline_data)
		print("generateklineimgs num_k:",num_k)
	
def distance(vector1,vector2):  
	d=0;  
	for a,b in zip(vector1,vector2):
		d+=(a-b)**2;  
	return d**0.5;


def calc_twoklinesimilar(prefer_kline, current_kline):
	similarity = distance(prefer_kline,current_kline)
	print("calc_twoklinesimilar similarity:",similarity)
	return similarity	

def retrieve_preferid(input_num):
	cwd=os.getcwd()
	prefer_image_oldpath = cwd + IMGS_PLACE_DIR
	prefer_image_newpath = cwd + PREFER_IMGS_PLACE_DIR
	CreateDirectory(PREFER_IMGS_PLACE_DIR)
	isExist = CheckIsExist(prefer_image_newpath)
	if(not isExist):
		return Null
	shutil.copyfile(prefer_image_oldpath+input_num+".png",prefer_image_newpath+input_num+".png")
	filefullpath = os.path.join(prefer_image_newpath, input_num+".png")
	#print("retrieve_preferid filefullpath:", filefullpath)
	return filefullpath

def gethighestsimilarity3imgs(input_num):
	similarities = []
	filepath = []
	high_images = []
	filepath = getallklinedatainpath()
	if(not filepath):
		return Null

	select = retrieve_preferid(input_num)
	prefer_kline = parseDatasetfromfile(select)
	print("gethighestsimilarity3imgs select:\n", select)
	print("gethighestsimilarity3imgs prefer_kline:\n", prefer_kline)
	num = len(filepath)
	print("num:", num)
	for i in range(num):
		fullpath = filepath[i]
		current_kline = parseDatasetfromfile(fullpath)
		similarity = calc_twoklinesimilar(prefer_kline, current_kline)
		similarities.append(similarity)
	#print("gethighestsimilarity3imgs similarities[%d]:%.8f" % (i, similarities[i]))

	for i in range(num):
		name_id = filepath[i].split("/")[-1].split(".")[0]
		high_images = gethighestsimilarityimages(high_images, i, name_id, similarities[i])
		print("gethighestsimilarity3imgs high_images:\n", high_images)
	return high_images

def main():
	starttime=time.time()
	stock_id = MANUAL_SELECTION_IMAGE_ID
	#generateklineimgs()
	gethighestsimilarity3imgs(stock_id)
	duration=time.time()-starttime
	print("main duration:",duration)

if __name__ == "__main__":
	main()
    


