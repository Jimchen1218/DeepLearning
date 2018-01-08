#include <opencv2\core\core.hpp>
#include <opencv2\highgui\highgui.hpp>
#include <opencv2\opencv.hpp>
using namespace cv;//�����ռ�
int main()
{
	VideoCapture capture(0);//����VideoCapture����
	if (!capture.isOpened())//�ж��Ƿ������ͷ����isOpened����ture
		return 1;
	bool stop(false);//����һ������ֹͣѭ���ı���
	Mat frame;//������Ŷ�ȡ����Ƶ���У�����ÿһ֡��ͼ�� ��Mat�������ڱ���ͼ���Լ������������ݵ����ݽṹ

	namedWindow("Camera");//����һ�����ڣ���ʾÿһ֡�Ĵ���
	while (!stop)
	{
		if (!capture.read(frame))//���û�ж�ȡ�����ж�
		{
			break;
		}
		imshow("Camera", frame);//������ʾ���ѻ�ȡ����Ƶ��䵽������

		char c = cvWaitKey(33);
		if (c == 32)break; //ʹ�ÿո����ֹͣASCII Ϊ32
	}
	capture.release();//�ͷ�
}