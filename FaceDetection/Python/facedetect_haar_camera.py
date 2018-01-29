# -*- coding: utf-8 -*-
'''
filename:facedetect_haar_camera.py 
author:jimchen1218@sina.com
created date:1/9/2018
'''
import cv2
import gc

print(__doc__)
 
cascade_fn_face = 'haarcascade_frontalface_alt2.xml' 
cascade_fn_eye = 'haarcascade_eye.xml' 
#cascade_fn_mouth = 'haarcascade_mcs_mouth.xml'
#cascade_fn_nose = 'haarcascade_mcs_nose.xml'
 
def objectdetect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.3,
                                    minNeighbors=5, minSize=(200, 200))
    count_rects = len(rects)
    print("objectdetect count_rects:",count_rects)
    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]
    print("rects:",rects)
    return rects
       
def draw_roi_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
        

def facedetection_pic():
	img = cv2.imread("img_414.jpg")
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	gray = cv2.equalizeHist(gray)
	cascade = cv2.CascadeClassifier(cascade_fn_face)
	rects = objectdetect(gray, cascade)
	draw_roi_rects(img, rects, (0, 255, 0))
	cv2.imshow('Image face detect',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()		
	

def facedetection_camera():
	capture=cv2.VideoCapture(0)
	print("capture.isOpened:",capture.isOpened())
	num=0

	while True:
		ret,img=capture.read()
		gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
		gray = cv2.equalizeHist(gray)
		cascade_face = cv2.CascadeClassifier(cascade_fn_face)		
		cascade_eye = cv2.CascadeClassifier(cascade_fn_eye)
#		cascade_nose = cv2.CascadeClassifier(cascade_fn_nose)	
#		cascade_mouth = cv2.CascadeClassifier(cascade_fn_mouth)		
					
		vis = img.copy()				
		rects_face = objectdetect(gray, cascade_face)
		draw_roi_rects(vis, rects_face, (0, 255, 0))
		rects_eye = objectdetect(gray, cascade_eye)
		draw_roi_rects(vis, rects_eye, (255, 0, 0))
		#rects_nose = objectdetect(gray, cascade_nose)
		#draw_roi_rects(vis, rects_nose, (0, 0,255))		
		#rects_mouth = objectdetect(gray, cascade_mouth)
		#draw_roi_rects(vis, rects_mouth, (0, 0,255))				
		cv2.imshow('facedetect', vis)
		key=cv2.waitKey(1)
		#cv2.imwrite('%s.jpg'%(str(num)),img)
		num=num+1
		if key==ord('q'):
			break

	capture.release()
	cv2.destroyAllWindows()		

def main():
	facedetection_pic()
	#facedetection_camera()
	
if __name__ == '__main__':
	main()
	gc.collect()


