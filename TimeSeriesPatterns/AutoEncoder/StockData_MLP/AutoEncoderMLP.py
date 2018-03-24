import pandas as pd
import numpy as np
import copy
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn import preprocessing
from keras.layers import Input, Dense, Conv2D, MaxPooling2D, UpSampling2D
from keras.models import Model
from keras import backend as K
from keras.callbacks import TensorBoard

def AutoEncoderMLP(nCompanies, nDays, encDim): ## This function use time series of data and turn them into autoencoders ##
    # this is the size of our encoded representations
    encoding_dim = encDim  # 32 floats -> compression of factor 24.5, assuming the input is 784 floats
    nL=len(encDim) # number of layers # 
    # this is our input placeholder # 
    (x,y)=(nDays, nCompanies)
    inputSize=x*y
    input_img = Input(shape=(x*y,))
    enc_img = Input(shape=(encoding_dim[nL-1],))
#    print enc_img
    #print input_img
    # "encoded" is the encoded representation of the input
    encoded = Dense(encoding_dim[0], activation='relu' )(input_img)
    # "encoded" is the encoded representation of the input
    for i in range(1,nL):
        encoded = Dense(encoding_dim[i], activation='relu' )(encoded)
        
    decoded = Dense(encoding_dim[nL-2], activation='relu')(encoded)    
    #print encoded.shape[1:]
    for j in range(nL-3,-1,-1):
        decoded = Dense(encoding_dim[j], activation='relu')(decoded)
    
    decoded = Dense(inputSize, activation='tanh')(decoded)
    ## Start compiling CNN autoencoders 
    autoencoder = Model(input_img, decoded)
    encoder=Model(input_img, encoded)

    L=len(autoencoder.layers)
    Z=autoencoder.layers[L-nL](enc_img)
#    Z.summary()
    for i in range(L-nL+1,L):
        Z=autoencoder.layers[i](Z)

    decoder=Model(enc_img,Z) 
    autoencoder.compile(optimizer='adam', loss='mean_squared_error')#, metrics=['accuracy'])

    return (autoencoder,encoder, decoder) 