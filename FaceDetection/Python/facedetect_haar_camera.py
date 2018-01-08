# -*- coding: utf-8 -*-
"""
name:objectextraction.py
@author: jimchen1218@sina.com
"""


import cv2

print(__doc__)
 

#size = (int(capture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
 #       int(capture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))

#video=cv2.VideoWriter("VideoTest.avi", cv2.cv.CV_FOURCC('I','4','2','0'), 30, (100,100))



#img = cv2.imread("girls.jpg")
 
def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.3,
                                    minNeighbors=5, minSize=(30, 30))
    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]
    print rects
    return rects

def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
 

cascade_fn = 'haarcascades/haarcascade_frontalface_alt.xml'


capture=cv2.VideoCapture(0)
print(capture.isOpened())
num=0

while True:
	ret,img=capture.read()
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	gray = cv2.equalizeHist(gray)
	cascade = cv2.CascadeClassifier(cascade_fn)
	rects = detect(gray, cascade)
	#video.write(img)
	vis = img.copy()
	draw_rects(vis, rects, (0, 255, 0))
	cv2.imshow('facedetect', vis)
	cv2.imshow('Video',img)
	key=cv2.waitKey(1)
	#cv2.imwrite('%s.jpg'%(str(num)),img)
	num=num+1
	if key==ord('q'):
		break

capture.release()
cv2.destroyAllWindows()


