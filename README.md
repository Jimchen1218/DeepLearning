# Notes
#1.tensorflow_facedetect_orl
#it is a face detect model built in tensorflow that has very high predict accuracy.

#2.tensorflow_trafficsigns
#it is a traffic signs model built in tensorflow.

#3.opencv_objectextraction
#it is a object extraction in opencv.

#4.tensorflow_cifar10
#it is a cifar10 using cnn train and evaluate in tensorflow.

#5.tensorflow_changeclothesbg
@it is a clothes change bg model that use ssd_mobilenet_v1_clothes train.
	1)create a directory:SSD_MOBILENET_CLOTHES and subdirectory data and models\model
	2)build a dataset includes  100 pics of clothes.
	3)create a clothes_labelmap.pbtxt
	4)use create_clothes_tf_record.py to transform datasets to tfrecord
			python create_clothes_tf_record.py
									--data_dir=datasets_clothes[datasets directory]
									--output_dir=tfrecord[directory]
	5)create a ssd_mobilenet_v1_clothes.config by simulating sample\config\ssd_mobilenet_v1_pet.config
	5)train own dataset:
			python train.py --logtostderr 
											--pipeline_config_path=SSD_MOBILENET_CLOTHES\models\model\ssd_mobilenet_v1_clothes.config
			                --train_dir=SSD_MOBILENET_CLOTHES\models\model\train
	



                                                  