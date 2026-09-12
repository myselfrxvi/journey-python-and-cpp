import torch as T 
import numpy as np 

w = T.tensor(2.0, requires_grad=True)
b = T.tensor(1.0, requires_grad=True)

x = T.tensor(3.0, requires_grad=True)
y = 10

loss = (y - (w * x + b)) ** 2 

print(loss.backward())

print(w.grad, b.grad)

