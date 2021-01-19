# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 17:11:13 2021

@author: David Bondesson
"""

import numpy as np
import pywt
from scipy.signal import chirp,sweep_poly
import matplotlib.pyplot as plt
from tfridge_tracking import ridge_tracking as rt

def visualize(signal, tf_transf,ridge,flip_plot=False):
    plt.plot(signal)
    plt.show()
    
    plt.figure()
    if(flip_plot):
        plt.imshow(np.flipud(np.abs(tf_transf)), aspect='auto', vmin=0, vmax=np.max(np.abs(tf_transf)), cmap='jet')
        plt.plot(len(tf_transf)-ridge,linestyle = '--',color='black')
    else:
        plt.imshow(np.abs(tf_transf), aspect='auto', cmap='jet')
        plt.plot(ridge,linestyle = '--',color='black')
    
    plt.show()
    
    
### Example 0: example ridge from similar example as can be found at Mathworks website 'https://de.mathworks.com/help/signal/ref/tfridge.html'    
test_matrix=np.array([[1, 4, 4],[2, 2, 2],[5,5,4]])
fs_test =np.exp(np.array([1,2,3]))

Energy,ridge_idx,_ = rt.extract_fridges(test_matrix,fs_test,penalty=2.0)

print('ridge follows indexes:', ridge_idx)
### Example 1: Two constant frequency signals
    
sig_lgth = 500
t_vec=np.linspace(0,10,sig_lgth)
f1=0.5
f2=2.0
signal_1=np.sin(f1*2*np.pi*t_vec)
signal_2=np.cos(f2*2*np.pi*t_vec)

signal=signal_1+signal_2

nbrVoices=32
nbr_scales=279
scales=np.exp(np.linspace(np.log(1.51),np.log(622.207),nbr_scales))
cwtmatr, freqs = pywt.cwt(signal,scales,'cmor2.0-1.0')

penalty=2.0
# CWT example
Energy,ridge_idx,_ = rt.extract_fridges(cwtmatr,scales,penalty,num_ridges=2,BW=25)
plt.figure()
visualize(signal, cwtmatr, ridge_idx)

### Example 2: Two chirp signals with linear and quadratic frequrncy variation

sign_chirp_1 = chirp(t_vec, f0=2, f1=10, t1=20, method='linear')
sign_chirp_2 = chirp(t_vec, f0=.4, f1=7, t1=20, method='quadratic')

sign_chirp=sign_chirp_1+sign_chirp_2


scales=np.exp(np.linspace(np.log(1.51),np.log(622.207),nbr_scales))
cwtmatr, freqs = pywt.cwt(sign_chirp,scales,'cmor2.0-1.0')

penalty=.3

# CWT example
Energy,ridge_idx,_ = rt.extract_fridges(cwtmatr,scales,penalty,num_ridges=2,BW=25)
plt.figure()
visualize(sign_chirp, cwtmatr, ridge_idx)

#### Example 3: One sweep signal and one constant frequency signal


p1 = np.poly1d([0.025, -0.36, 1.25, 2.0])

sweep_sig = sweep_poly(t_vec, p1)+signal_1

scales=np.exp(np.linspace(np.log(1.51),np.log(622.207),nbr_scales))
cwtmatr, freqs = pywt.cwt(sweep_sig,scales,'cmor2.0-1.5')

penalty=2.0

# CWT example
Energy,ridge_idx,_ = rt.extract_fridges(cwtmatr,scales,penalty,num_ridges=2,BW=25)
plt.figure()
visualize(sweep_sig, cwtmatr, ridge_idx)












