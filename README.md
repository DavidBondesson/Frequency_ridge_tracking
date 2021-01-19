# Frequency_ridge_tracking
Ridge tracking extracts the N most prominent frequency ridges from a Time-frequency representation. 

The method is based on a forward-backward greedy algorithm that penalises frequency jumps similar to the MATLAB function 'tfridge' (https://de.mathworks.com/help/signal/ref/tfridge.html). 

Further information about algorithm as well as limitations and comparisson to other ridge extraction schemes can be found in the following publication:
 'On the extraction of instantaneous frequencies fromridges in time-frequency representations of signals",D. Iatsenko, P. V. E. McClintock, A. Stefanovska, https://arxiv.org/pdf/1310.7276.pdf



### Example 1: Two constant frequency signals

```python

    
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



```

![signal_1](/imgs/signal_1.png)
![cwt_ridge_signal_1](/imgs/cwt_signal_1_ridge.png)


### Example 2: Two chirp signals with linear and quadratic frequrncy variation

```python

    
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



```

![signal_2](/imgs/signal_2.png)
![cwt_ridge_signal_2](/imgs/cwt_signal_2_ridge.png)

### Example 3: One sweep signal and one constant frequency signal

```python

    
p1 = np.poly1d([0.025, -0.36, 1.25, 2.0])

sweep_sig = sweep_poly(t_vec, p1)+signal_1

scales=np.exp(np.linspace(np.log(1.51),np.log(622.207),nbr_scales))
cwtmatr, freqs = pywt.cwt(sweep_sig,scales,'cmor2.0-1.5')

penalty=2.0

# CWT example
Energy,ridge_idx,_ = rt.extract_fridges(cwtmatr,scales,penalty,num_ridges=2,BW=25)
plt.figure()
visualize(sweep_sig, cwtmatr, ridge_idx)



```

![signal_3](/imgs/signal_1.png)
![cwt_ridge_signal_3](/imgs/cwt_signal_3_ridge.png)
