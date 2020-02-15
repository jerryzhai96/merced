import numpy as np 
import matplotlib.pyplot as plt 
import json
unit_dict = {
    'imperial':{
        'length':'in',
        'force':'kip',
        'time':'sec'},
        'g': 386
    }
class Spectrum:
    def __init__(self,units='imperial'):
        self.units = unit_dict[units]

    def Psa(self,opt,domain=None):
        if opt=='design':
            ts = self.sd1/self.sds
            Sa1 = [self.sds,self.sds]
            Sa2 = self.sd1

        if opt.lower()=='mcer':
            ts = self.s1/self.ss
            Sa1 = [self.ss,self.ss]
            Sa2 = self.s1

        if opt.lower()=='disp':
            ts = self.s1/self.ss
            Sa1 = [self.ss,self.ss]
            Sa2 = self.s1

        t1 = [0,ts]
        tl = min(self.tl,domain[1])
        t2 = np.linspace(ts,tl,50)
        t = np.append(t1,t2)
        Sa = np.append(Sa1,Sa2/t2)

        return (t,Sa)

    def Psv(self,opt):
        t, Sa = self.Psa(opt)
        Sv = Sa*t/(2*np.pi)
        return t,Sv
    
    def displ(self,opt):
        t, Sa = self.Psv(opt)
        Sd = Sa*t/(2*np.pi)
        return t,Sd

    def plot(self,level,opt='Psa',domain=None):
        if opt == 'Psa':
            x,y = self.Psa(level,domain)
        
        if opt == 'Psa':
            t,Sa = self.Psa(level,domain)
        # if domain is None:
        #     domain = [0,10]

        # if opt=='design':
        #     ts = self.sd1/self.sds
        #     Sa1 = [self.sds,self.sds]
        #     Sa2 = self.sd1

        # if opt.lower()=='mcer':
        #     ts = self.s1/self.ss
        #     Sa1 = [self.ss,self.ss]
        #     Sa2 = self.s1

        # if opt.lower()=='disp':
        #     ts = self.s1/self.ss
        #     Sa1 = [self.ss,self.ss]
        #     Sa2 = self.s1

        # t1 = [0,ts]
        # tl = min(self.tl,domain[1])
        # t2 = np.linspace(ts,tl,50)
        # t = np.append(t1,t2)
        # Sa = np.append(Sa1,Sa2/t2)

        fix, ax = plt.subplots()
        ax.plot(x,y)
        return ax





#     # (C11.4-1)
#     Fa = np.exp(-0.727*np.log(Vs30/760)-0.2298*np.exp(−0.00638*(min(Vs30, 760)) - 360))
#     -np.exp(−0.00638 x 400)*np.log((Ss/2.3 + 0.1)/0.1))
# Fv = np.exp(-1.03 np.ln(Vs30/760 - 0.118*np.exp(-0.00756*min(Vs30, 760) -360))-
# np.exp(-0.00756 * 400))*np.log((S1/0.7+ 0.1)/0.1)
