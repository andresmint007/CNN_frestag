from unittest import result
import numpy as np
import tensorflow as tf 
import keras
import cv2 
import os
from keras.models import Sequential,Input,Model

model_3=keras.models.load_model("frestagFnl2_mnist.h5py") #charge the model Frestag, Accuracy: 67.81
chartec = { "ETAPA 1": 20,"ETAPA 2": 40,"ETAPA 3": 60, "ETAPA 4": 80, "ETAPA 5": 100,}

def analizeregsiters(registers):
    average=[]
    img_size=224
    for link in registers:
     rtX=[]
     img_arr = cv2.imread(os.path.join(link))[...,::-1] #convert BGR to RGB format
     resized_arr = cv2.resize(img_arr, (img_size, img_size)) # Reshaping images to preferred size
     rtX.append(resized_arr)
     nprt=np.array(rtX)
     test_X = nprt / 255.
     inteliss=modelGet(test_X)
     add=chartec[inteliss]
     average.append(add)
    
    return average
def modelGet(nparryImg): 
    labels = ['ETAPA 1', 'ETAPA 2','ETAPA 3', 'ETAPA 4','ETAPA 5']
    predicted_classes2 = model_3.predict(nparryImg)
    predicted_classes2
    for i,img_tagged in enumerate(predicted_classes2):
     resultProduc= labels[img_tagged.tolist().index(max(img_tagged))]
    
    return resultProduc
