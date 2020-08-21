import numpy as np

import layers
import gradient_check


input_features = 87
out_features = 57
x = np.random.randn(10, input_features) * 1.5
layer = layers.LinearLayer(input_features, out_features)
out = layer.forward(x)

dout = np.random.randn(*out.shape)
dx, dw, db = layer.backward(dout)

gradient_check.eval_numerical_gradient_array(lambda w_: layers.LinearLayer.for_grad_check(x=x, w=w_, b=layer.b), layer.w, dw, dout)
gradient_check.eval_numerical_gradient_array(lambda x_: layers.LinearLayer.for_grad_check(x=x_, w=layer.w, b=layer.b), x, dx, dout)
gradient_check.eval_numerical_gradient_array(lambda b_: layers.LinearLayer.for_grad_check(x=x, w=layer.w, b=b_), layer.b, db, dout)
