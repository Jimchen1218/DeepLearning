#include "FaceDetection.h"
#include <stdio.h>  
#include <stdlib.h>  
#include <string.h>  

#define FACEDETECT_API __declspec(dllimport)
#pragma comment(lib,"FaceDetection.lib")

using namespace std;

int main()
{
	printf("this is face detection caller! start to go!!!");
	facedetection();
	printf("this is face detection caller!");
	return 0;
}