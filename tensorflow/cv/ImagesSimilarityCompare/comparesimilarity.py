'''
name:comparesimilarity.py
create date:8/23/2017
author:jimchen
function:a class that use hist to count the two images's similarity
'''


from PIL import Image
import matplotlib.image as mpimg


class histcomparesimilar(object):
	def __init__(self,regular_size_width,regular_size_height,partial_size,radio):
		self.regular_size_width = regular_size_width
		self.regular_size_height = regular_size_height
		self.partial_size = partial_size
		self.radio = radio

	def resizeimage(self,img):
		img_size_width = self.regular_size_width
		img_size_height = self.regular_size_height
		#print("resizeimage img_size_width:", img_size_width)
		#print("resizeimage img_size_height:", img_size_height)
		img_resize = img.resize((img_size_width,img_size_height))
		#print("resizeimage img_resize:", img_resize)
		img_rbg = img_resize.convert('RGB')
		#print("resizeimage img_rbg:", img_rbg)
		return img_rbg
		
	def split_image(self,img):
	    w, h = img.size
	    #print("split_image img:", img)
	    pw = self.partial_size
	    ph = self.partial_size
	    assert w % pw == h % ph == 0
	    return [img.crop((i, j, i+pw, j+ph)).copy() \
	        for i in range(0, w, pw) \
	        for j in range(0, h, ph)]

	def hist_similar(self,lh, rh):
		hist_similar =0.0
		sim= 0.0
		assert len(lh) == len(rh)
		for l, r in zip(lh, rh):
			if l == r:
				sim= 1.0
			else:
				sim = 0.0
			hist_similar = hist_similar+sim
		
		hist_similar = hist_similar/len(lh)
		#print("hist_similar hist_similar:", hist_similar)
		return hist_similar

	def calc_histsimilar(self,li, ri):
		total_histsimilar = 0
		for l, r in zip(self.split_image(li), self.split_image(ri)):
			#hist_sim = self.hist_similar(l.getdata(), r.getdata())
			hist_sim = self.hist_similar(l.histogram(), r.histogram())
			total_histsimilar =total_histsimilar +hist_sim
		sum_histsimilar = total_histsimilar / self.radio
		#print("calc_histsimilar sum_histsimilar:", sum_histsimilar)
		return sum_histsimilar

	def calcsimilar_twoimages(self,lf,rf):
		#print("calcsimilar_twoimages lf:%s,rf:%s"%(lf,rf))
		image_lf=Image.open(lf)
		image_rf=Image.open(rf)
		#img_mode = image_lf.mode
		#img_size = image_lf.size
		#print("calcsimilar_twoimages img_mode:%s,img_size:%s"%(img_mode,img_size))
		#lf_data=image_lf.getdata()
		#rf_data=image_rf.getdata()
		#print("calc_histsimilar lf_data:", lf_data)
		#lf_bands=image_lf.getbands()
		#print("calc_histsimilar lf_bands:", lf_bands)
		#lf_format=image_lf.format
		#print("calc_histsimilar lf_format:", lf_format)
		li = self.resizeimage(image_lf)
		ri = self.resizeimage(image_rf)
		return self.calc_histsimilar(li,ri)
		
