#!/usr/bin/env python3
import tensorflow.keras as K
"""
write a function that optimize the model 
"""


def optimize_model(network, alpha, beta1, beta2):
    """
    optimize the model 
    """
    network.compile(optimizer = K.optimizers.Adam(lr = alpha, beta_1 = beta1, beta_2 = beta2),
                    loss = 'categorical_crossentropy', metrics = ['accuracy'])
  
