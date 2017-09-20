'''
name:cnn_kline_likelihood.py
create date:8/21/2017
author:jimchen
'''

from comparesimilarity import histcomparesimilar

import tensorflow as tf
import sys
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image
import matplotlib.finance as mpf
import math
import glob
import time
import operator

print(__doc__)

HIGHEST_SIMILARITY_IMAGES_NUMBER = 3
TOTAL_NUM_IMAGES= 30
IMAGE_RESIZE_FULLSIZE_WIDTH = 512
IMAGE_RESIZE_FULLSIZE_HEIGHT = 512
IMAGE_RESIZE_COMPARESIZE = 32
# if you want to change the selected image ,update here
MANUAL_SELECTION_IMAGE_NUMBER= '20'
IMGS_PLACE_DIR = "/images/"

def CheckIsExist(full_path):
	full_path=full_path.strip()
	if(not os.path.exists(full_path)):
		print("CheckIsExist file is not exist!")
		return False
	else:
		return True

def sortallimgfile(paths):
		paths_len = len(paths)
    for i in range(paths_len):
    	for j in range(paths_len):
				name_no=int(os.path.splitext(paths[i].split("/")[-1])[0])

		#print("getallimgsinpath name:%d\n"%(int(name[0])))


def getallimgsinpath():
    paths=[]
    cwd=os.getcwd()
    images_path=cwd+IMGS_PLACE_DIR
    isExist = CheckIsExist(images_path)
    if(not isExist):
        return Null
        
    for file_name in os.listdir(images_path):
        if file_name.endswith('png'):
            filefullpath = os.path.join(images_path, file_name)
            paths.append(filefullpath)
            #sorted(paths)
            #paths = paths.sort(key=len)
    
    #sorted(paths)
    
    for i in range(len(paths)):
    	for j in range(len(paths)):
				filename = paths[i].split("/")[-1]
				name=os.path.splitext(paths)
		name_i= int(name[0])
		#print("getallimgsinpath name:%d\n"%(int(name[0])))        
    print("generatefullpath paths:", paths)
    return paths


#get all image files and labels from current directory
def generatefullpath(input_num):
	cwd=os.getcwd()
	images_path = cwd + IMGS_PLACE_DIR
	filefullpath = os.path.join(images_path, input_num+".png")
	#print("generatefullpath filefullpath:", filefullpath)
	return filefullpath

def gethighestsimilarityimages(highimages,i,compareimg):
	len_images= len(highimages)
	print("gethighestsimilarityimages compareimg:", compareimg)
	if len_images < HIGHEST_SIMILARITY_IMAGES_NUMBER:
		highimages.insert(i,(i,compareimg))
		print("gethighestsimilarityimages highimages:", highimages)
		return highimages

	if compareimg > highimages[HIGHEST_SIMILARITY_IMAGES_NUMBER-1][1]:
		print("gethighestsimilarityimages highimages:", highimages)
		highimages.pop(-1)
		highimages.insert(i, (i,compareimg))

	highimages = sorted(highimages, key=operator.itemgetter(1), reverse=True)
	return highimages

def gethighestsimilarity3imgs(input_num):
    similarities = []
    filepath = []
    high_images = []
    filepath = getallimgsinpath()
    if(not filepath):
        return Null
        
    num = len(filepath)
    print("num:", num)
    select = generatefullpath(input_num)
    print("gethighestsimilarity3imgs select:\n", select)

    resize_ratio = (IMAGE_RESIZE_FULLSIZE_WIDTH*IMAGE_RESIZE_FULLSIZE_HEIGHT)/np.power(IMAGE_RESIZE_COMPARESIZE,2)
    print("gethighestsimilarity3imgs resize_ratio:\n", resize_ratio)
    hcs = histcomparesimilar(IMAGE_RESIZE_FULLSIZE_WIDTH, IMAGE_RESIZE_FULLSIZE_HEIGHT, IMAGE_RESIZE_COMPARESIZE, resize_ratio)
    for i in range(num):
        fullpath = filepath[i]
        #filename = fullpath.split("/")[-1]
        #name=os.path.splitext(filename)
        #print("gethighestsimilarity3imgs name:%d\n"%(int(name[0])))
        print("gethighestsimilarity3imgs i:%d ,fullpath:%s\n"%(i,fullpath))
        similarity = hcs.calcsimilar_twoimages(select, fullpath)
        similarities.append(similarity)
        #print("gethighestsimilarity3imgs similarities[%d]:%.8f" % (i, similarities[i]))

    for i in range(num):
        high_images = gethighestsimilarityimages(high_images, i, similarities[i])
    print("gethighestsimilarity3imgs high_images:\n", high_images)
    return high_images

def compare2imgsimilarity(img1_no,img2_no):
    img_1 = generatefullpath(img1_no)
    img_2 = generatefullpath(img2_no)
    print("compare2imgsimilarity img_1:\n", img_1)
    print("compare2imgsimilarity img_2:\n", img_2)
    resize_ratio = (IMAGE_RESIZE_FULLSIZE_WIDTH*IMAGE_RESIZE_FULLSIZE_HEIGHT)/np.power(IMAGE_RESIZE_COMPARESIZE,2)
    hcs = histcomparesimilar(IMAGE_RESIZE_FULLSIZE_WIDTH, IMAGE_RESIZE_FULLSIZE_HEIGHT, IMAGE_RESIZE_COMPARESIZE, resize_ratio)
    similarity = hcs.calcsimilar_twoimages(img_1, img_2)
    print("compare2imgsimilarity similarity:", similarity)
    return similarity

def main(_):
		start_time=time.time()
		gethighestsimilarity3imgs(MANUAL_SELECTION_IMAGE_NUMBER)
		#compare2imgsimilarity('1','2167')
		compute_time=time.time()-start_time
		print("main compute duration time:", compute_time)

if __name__ == "__main__":
    tf.app.run(main=main, argv=[sys.argv[0]])
    


