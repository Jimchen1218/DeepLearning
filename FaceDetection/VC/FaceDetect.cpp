#include <opencv2\core\core.hpp>
#include <opencv2\highgui\highgui.hpp>
#include <opencv2\opencv.hpp>
using namespace cv;//命名空间
int main()
{
	VideoCapture capture(0);//创建VideoCapture对象
	if (!capture.isOpened())//判断是否打开摄像头，打开isOpened返回ture
		return 1;
	bool stop(false);//定义一个用来停止循环的变量
	Mat frame;//用来存放读取的视频序列，承载每一帧的图像 ，Mat类是用于保存图像以及其他矩阵数据的数据结构

	namedWindow("Camera");//创建一个窗口，显示每一帧的窗口
	while (!stop)
	{
		if (!capture.read(frame))//如果没有读取到就中断
		{
			break;
		}
		imshow("Camera", frame);//正常显示，把获取的视频填充到窗口中

		char c = cvWaitKey(33);
		if (c == 32)break; //使用空格键来停止ASCII 为32
	}
	capture.release();//释放
}