#include <cv.h>
#include <opencv2\opencv.hpp>
#include <stdio.h>  
#include <stdlib.h>  
#include <string.h>  
#include <assert.h>  
#include <math.h>  
#include <float.h>  
#include <limits.h>  
#include <time.h>  
#include <ctype.h>  
using namespace std;

static CvMemStorage* storage = 0;
static CvHaarClassifierCascade* cascade = NULL;

const char* haarcascade_name = "haarcascade_frontalface_alt2.xml";

void detect_and_draw(IplImage* img)
{
	static CvScalar colors[] =
	{
		{ { 0, 0, 255 } },
		{ { 0, 128, 255 } },
		{ { 0, 255, 255 } },
		{ { 0, 255, 0 } },
		{ { 255, 128, 0 } },
		{ { 255, 255, 0 } },
		{ { 255, 0, 0 } },
		{ { 255, 0, 255 } }
	};


	double scale = 1.3;
	IplImage* gray = cvCreateImage(cvSize(img->width, img->height), 8, 1);
	IplImage* small_img = cvCreateImage(cvSize(cvRound(img->width / scale),
		cvRound(img->height / scale)), 8, 1);
	int i;

	cvCvtColor(img, gray, CV_BGR2GRAY);
	cvResize(gray, small_img, CV_INTER_LINEAR);
	cvEqualizeHist(small_img, small_img);
	cvClearMemStorage(storage);


	if (cascade)
	{
		double t = (double)cvGetTickCount();
		CvSeq* faces = cvHaarDetectObjects(small_img, cascade, storage, 1.1, 2, 0, cvSize(50, 50));
		t = (double)cvGetTickCount() - t;
		//printf("detection time = %gms/n", t / ((double)cvGetTickFrequency()*1000.));
		for (i = 0; i < (faces ? faces->total : 0); i++)
		{
			CvRect* r = (CvRect*)cvGetSeqElem(faces, i);
			//CvPoint center;
			//int radius;
			//center.x = cvRound((r->x + r->width*0.5)*scale);
			//center.y = cvRound((r->y + r->height*0.5)*scale);
			//radius = cvRound((r->width + r->height)*0.25*scale);
			//cvCircle(img, center, radius, colors[i % 8], 3, 8, 0);
			printf("detect_and_draw rect i:%,x:%d ,y:%d ,dx:%d,dy:%d\n", (i,r->x, r->y, r->x + r->width, r->y + r->height));
			cvRectangle(img, cvPoint(r->x, r->y), cvPoint(r->x + r->width*1.4, r->y + r->height*1.6), cvScalar(201, 102, 62), 3, 4, 0);
		}
	}

	cvReleaseImage(&gray);
	cvReleaseImage(&small_img);
}



int main() 
{ 
	//test show ok!!!
	//IplImage * test;
	//test = cvLoadImage ("Bangle_Jewelry_069.jpg"); 
	//cvNamedWindow("test_demo", 1); 
	//cvShowImage("test_demo", test); 
	//cvWaitKey(0); 
	//cvDestroyWindow("test_demo");
	//cvReleaseImage(&test); 

	CvCapture* capture;
	capture = cvCreateCameraCapture(0);

	cascade = (CvHaarClassifierCascade*)cvLoad(haarcascade_name, 0, 0, 0);
	if (!cascade)
	{
		fprintf(stderr, "ERROR: Could not load classifier cascade/n");
		return -1;
	}

	storage = cvCreateMemStorage(0);
	assert(capture != NULL);

	IplImage* frame;
	frame = cvQueryFrame(capture); //����ͷ��һ֡
	while (1) {
		frame = cvQueryFrame(capture);//�ڶ�֡
		detect_and_draw(frame);
		//if (!frame) break; 
		//if(i>0)  
		cvShowImage("facedetection", frame);
		char c = cvWaitKey(10);
		if (c == 27) break;
		//i++;  
	}
	cvReleaseCapture(&capture);
	cvDestroyWindow("face");
	cvWaitKey(0);
	return 0;
}