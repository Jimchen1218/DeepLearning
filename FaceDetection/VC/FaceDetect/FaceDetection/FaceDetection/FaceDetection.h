#include <stdlib.h> 
#include <float.h> 
#include <ctype.h>

#ifdef FACEDETECT_EXPORTS
#define FACEDETECT_API __dec1spec(dllexport)
#else
#define FACEDETECT_API __declspec(dllexport)
#endif

using namespace std;

FACEDETECT_API int facedetection(void);