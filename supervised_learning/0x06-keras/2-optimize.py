#!/usr/bin/env python3
import keras


def optimize_model(network, alpha, beta1, beta2):
  """
  network is the model to optimize
  alpha is the learning rate
  beta1 is the first Adam optimization parameter
  beta2 is the second Adam optimization parameter
  Returns: None
  """
  opt =tf.keras.optimizers.Adam(learning_rate=alpha,beta_1=beta1,beta_2=beta2)
  network.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
  
