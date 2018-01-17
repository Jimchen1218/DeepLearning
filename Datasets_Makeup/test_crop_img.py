from PIL import Image
import string
import time
import os

time_start = time.time()
time.sleep(5)
'''
data =[]
path=[]
for line in open("info.txt"):
		print("line:\n",line,)
		data.append(line.split(" "))
		
print("data:\n",data)

l = len(data)
for i in range(l):
	path = data[i][0]
	print("\npath:%s"%(path))
	x,y,w,h = data[i][2],data[i][3],data[i][4],data[i][5]
	print("i:%d\nx:%s,y:%s,w:%s,h:%s\n"%(i,x,y,w,h))
	img=Image.open(path)
	#box=(x,y,w,h)
	roi=img.crop((int(x),int(y),int(w),int(h)))
	name = str(i+1)+".bmp"
	roi.save(name)
'''

time_duration=time.time()-time_start
print("time_duration:%ss"%time_duration)
