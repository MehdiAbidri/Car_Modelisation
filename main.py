import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# Car modelisation project 
# Team : Zahra Mellakh & Mehdi Abidri 
# =============================================================================

# Constants: 
L  = 2.62 # Empattement     
Lf = 0.5 *L 
Lr = L - Lf

# Time :

startTime=0
endTime=39
stepTime=0.01
time = np.arange(start=startTime, stop=endTime, step=stepTime)
time = time.reshape(time.shape[0],1)

# Empty vectors : 

X = np.zeros_like(time) 
Y = np.zeros_like(time) 
Phi = np.zeros_like(time) 
Beta = np.zeros_like(time)
Delta = np.zeros_like(time)
v = np.zeros_like(time)
Z= np.zeros_like(time)   
R= np.zeros_like(time) 


# functions : 
# X point:

def x_point (phi,beta,v):
    return v*np.cos(phi+beta)

# Y point
def y_point (phi,beta,v):
    return v*np.sin(phi+beta)

# Phi point : 
def phi_point(delta,beta,v,Lf,Lr):
    return (v/(Lf+Lr))*np.cos(beta)*np.tan(delta)


# X function : 
def X_func(Xp_t,Xp_t_,t_,_t):
    return (Xp_t+Xp_t_)*(t_-_t)/2

# Y function : 
def Y_func(Yp_t,Yp_t_,t_,_t):
    return (Yp_t+Yp_t_)*(t_-_t)/2

# Phi function : 
def Phi_func(Phip_t,Phip_t_,t_,_t):
    return (Phip_t+Phip_t_)*(t_-_t)/2

# Beta :
def beta(delta,Lf,Lr):
    return np.arctan((Lr/(Lr+Lf))*np.tan(delta))

def main(Phi,Beta,Delta,v,Lf,Lr,Slip):
    
    for i in range(0,len(time),1) :
        
        t_ = time[i,0]
        _t = time[i-1,0]
        
        Phip_t= phi_point(Delta[i],Beta[i],v[i],Lf,Lr)
        Phip_t_= phi_point(Delta[i-1],Beta[i-1],v[i-1],Lf,Lr)
        
        if Slip == 1:
            print("Slip is taken into account")
            Beta[i]=beta(Delta[i],Lf,Lr)
        elif Slip == 0 : 
            print("Slip is not taken into account")
            Beta[i]=0
        
        Phi[i]= Phi_func(Phip_t,Phip_t_,t_,_t) + Phi[i-1]
        
        Xp_t = x_point (Phi[i],Beta[i],v[i])
        Xp_t_ = x_point (Phi[i-1],Beta[i-1],v[i-1])
        
        Yp_t = y_point (Phi[i],Beta[i],v[i])
        Yp_t_ = y_point (Phi[i-1],Beta[i-1],v[i-1])

        X[i]= X_func(Xp_t,Xp_t_,t_,_t) + X[i-1]
        Y[i]= Y_func(Yp_t,Yp_t_,t_,_t) + Y[i-1]
        
    return X,Y

  
        
        
v[:,0]=0.6
Delta[:,0]=np.pi/6 



X_wo_slip,Y_wo_slip = main(Phi,Beta,Delta,v,Lf,Lr,Slip=0)


v[:,0]=0.6
Delta[:,0]=np.pi/5 


plt.figure(1)
plt.subplot(2,2,1)

plt.plot(X_wo_slip,Y_wo_slip)

plt.axis('equal')

plt.subplot(2,2,2)
plt.plot(time,X_wo_slip)
plt.plot(time,Y_wo_slip)







    






