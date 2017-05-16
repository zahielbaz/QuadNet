import keras
import numpy as np

def net():
    resnet=keras.applications.ResNet50(include_top=False,input_shape=[476, 633, 3],pooling='avg',weights='imagenet')
    model=keras.models.load_model('15-5-2017-A/20170515-151603-09-0.1007.hdf5')
    return resnet, model

def coder(images,resnet):
    coded = resnet.predict(images)
    return coded

def control(coded, model, mini, maxi):
    coded = np.expand_dims(coded,axis=0)
    normout = model.predict(coded)
    out=[normout[0]*(maxi[:4]-mini[:4])+mini[:4], normout[1]*(maxi[4:]-mini[4:])+mini[4:]]
    return out

if __name__ == '__main__':
    images = np.load('ds1images.npy')
    images = images[:3]
    resnet, model=net()
    mini = np.load('15-5-2017-A/min.npy')
    maxi = np.load('15-5-2017-A/max.npy')
    coded=coder(images,resnet)
    out=control(coded, model, mini, maxi)