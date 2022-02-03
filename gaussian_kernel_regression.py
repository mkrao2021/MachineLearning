# -*- coding: utf-8 -*-
"""gaussian_kernel_regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1StXZnvtE8Crqs0UyfnjaEZyCRTgY7UbB
"""

from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

plt.rcParams.update({'font.size': 20})
import numpy as np
import scipy.special

"""# Gaussian Kernel matrix
 
With the above normalized polynomials, the innerproduct in feature space is specified by 
$$\left\langle \phi(x),\phi(y) \right\rangle = \frac{1}{\sqrt{2\pi \sigma^2}} \exp(-\frac{|x-y|^2}{2\sigma^2}) $$

The kernel matrix $\mathbf K$ is obtained from the training data as $$(\mathbf K)_{i,j} = \left\langle \phi(x_i),\phi(x_j) \right\rangle = \frac{1}{\sqrt{2\pi \sigma^2}} \exp(-\frac{|x-y|^2}{2\sigma^2})$$ 
"""

def gausskernel(x,y,sigma):
    constant = 1/np.sqrt(2*np.pi*sigma**2)
    scaleddistance = sum((x-y)**2)/sigma**2/2
    gaussian = constant * np.exp(-scaleddistance)
    return (gaussian)

def kernelmatrix(x,y,sigma):
    Nx = x.size
    Ny = y.size
    K = np.zeros((Nx,Ny))
    for i in range(Nx):
        for j in range(Ny):
            K[i,j] = gausskernel(x[i],y[j],sigma)
    return(K)

"""## Creating some training data"""

npoints = 8

# Noise variance
noisestd = 0.2

xtraining = np.arange(npoints)
yorig = np.sin(xtraining) 
ytraining = yorig + noisestd*np.random.normal(size=npoints)

fig = plt.figure()
ax = fig.gca()
cs = ax.plot(xtraining, ytraining,'ro',label='Training samples')
cs = ax.plot(xtraining, yorig,'b')
cs = ax.plot(xtraining,yorig,'ko',label='Original samples')
legend = ax.legend(loc='upper left', shadow=True, fontsize='x-small')
c=plt.title('Data')

"""## Kernel regression using dual formulation

$$\mathbf w = (\mathbf K + \lambda \mathbf I)^{-1}\mathbf y$$

$$\boldsymbol\theta = \mathbf X^T \mathbf w$$
"""

sigma = 1
K = kernelmatrix(xtraining,xtraining,sigma)
N = xtraining.size
lam = 0.1
w = np.linalg.inv(K+lam*np.eye(N))@ytraining

# Evaluating the function on a fine grid
xtest = np.arange(0,7,0.1)
kvector = kernelmatrix(xtraining,xtest,sigma)
ytest = w@kvector

s=fig = plt.figure()
s=plt.plot(xtraining, ytraining,'ro',yorig)
s=plt.plot(xtest, ytest)
s=plt.ylabel('y')
s=plt.xlabel('x')

sigma = 1
K = kernelmatrix(xtraining,xtraining,sigma)
N = xtraining.size
lam = 0.1
w = np.linalg.inv(K+lam*np.eye(N))@ytraining

# Evaluating the function on a fine grid
xtest = np.arange(0,7,0.1)
kvector = kernelmatrix(xtraining,xtest,sigma)
ytest = w@kvector

s=fig = plt.figure()
s=plt.plot(xtraining, ytraining,'ro',yorig)
s=plt.plot(xtest, ytest)
s=plt.ylabel('y')
s=plt.xlabel('x')