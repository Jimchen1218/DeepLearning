1¡¢How to use Floyd cloud to train your own model?
   1)setup environment :pip install -U floyd-cli
   2)floyd login
   3)create a project ,cd project_name 
   4)floyd init project_name
   5)floyd run --env tensorflow-1.4 --gpu "python *.py"
       the cloud end use GPU with Tesla K80 16G
   6)floyd status
      can show train log or fresh web page.
   7)floyd stop 
      can stop the train ,but I try failed.
      
2¡¢Set which works? CPU or GPU
   import os
   os.environ['CUDA_VISIBLE_DEVICES']='0' first GPU
   
