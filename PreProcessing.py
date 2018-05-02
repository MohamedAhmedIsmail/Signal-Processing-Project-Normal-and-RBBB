from EnumClasses import TypeOfNormalization
#from scipy.signal import butter, lfilter
from ReadData import Read
import numpy as np
import math
class preProcessingData:
    def NormalizeData(self,Signal=None,Type=None):
        Normalized2dList=[]
        for i in range(len(Signal)):
            NormalizedSignalList=[]
            for j in range(len(Signal[i])):
                minimum=np.min(Signal[i])
                maximum=np.max(Signal[i])
            for k in range(len(Signal[i])):
                if Type == TypeOfNormalization.zeroToOne:
                    NormalizedSignalList.append((Signal[i][k]-minimum)/(maximum-minimum))
                else:
                    NormalizedSignalList.append((2*((Signal[i][k])-minimum)/(maximum-minimum))-1)
            Normalized2dList.append(NormalizedSignalList)
        normalNormalized=np.array(Normalized2dList)
        return normalNormalized
class preProcessingFilter:
    def __init__(self):
        self.choose=np.zeros(4)
    def CalculateN(self,stopBandattenuation=None,samplingFreq=None,transitionWidth=None):
        N=0
        if stopBandattenuation<32:
            N=(0.9*samplingFreq)/transitionWidth
            self.choose[0]=1
        elif stopBandattenuation>=32 and stopBandattenuation<44:
            N=(3.1*samplingFreq)/transitionWidth
            self.choose[1]=1
        elif stopBandattenuation<48 and stopBandattenuation>=44:
            N=(3.1*samplingFreq)/transitionWidth
            self.choose[1]=1
        elif stopBandattenuation>=48 and stopBandattenuation<=53:
            N=(3.3*samplingFreq)/transitionWidth
            self.choose[2]=1
        elif stopBandattenuation<60 and stopBandattenuation>53:
            N=(3.3*samplingFreq)/transitionWidth
            self.choose[2]=1
        elif stopBandattenuation>=60:
            N=(5.5*samplingFreq)/transitionWidth
            self.choose[3]=1
        return int(N),self.choose
    def WindowFunctions(self,choose=None,N=None,i=None):
        if choose[0]==1:
            window_map=1
        elif choose[1]==1:
            window_map=0.5 + 0.5*math.cos((2*math.pi*i)/N)
        elif choose[2]==1:
            window_map=0.54 + 0.46*math.cos((2*math.pi*i)/N)
        elif choose[3]==1:            
            window_map=0.42 + (0.5*math.cos((2*math.pi*i)/(N - 1))) + (0.08*math.cos((4*math.pi*i)/(N - 1)))
        return window_map
    def BandPassFilter(self,passBandEdge1=None,passBandEdge2=None,transitionWidth=None,stopBandattenuation=None,samplingFreq=None):
        fc1_dash=(passBandEdge1/samplingFreq)-(transitionWidth/(2*samplingFreq))
        fc2_dash=(passBandEdge2/samplingFreq)+(transitionWidth/(2*samplingFreq))
        hd_map={}
        window_map={}
        odd_N=0
        N,choose=self.CalculateN(stopBandattenuation,samplingFreq,transitionWidth)
        if N%2==0:
            odd_N=N + 1
        for i in range(int(-N/2),int(N/2)+1):
            if i ==0:
                hd_zero=2*(fc2_dash-fc1_dash)
                hd_map[i]=hd_zero
            if i!=0:
                hd_map[i]=((2*fc2_dash*math.sin(i*2*math.pi*fc2_dash))/(i*2*math.pi*fc2_dash)) - ((2*fc1_dash*math.sin(i*2*math.pi*fc1_dash))/(i*2*math.pi*fc1_dash))
            window_map[i]=self.WindowFunctions(choose,odd_N,i)
        coffecients_h={}
        coffecients_h={k:window_map[k]*hd_map[k] for k in window_map}
        return coffecients_h
    def DirectConvolutionSignal(self,FirstSignal=None,SecondSignal=None):
        N1=len(FirstSignal)
        N2=len(SecondSignal)
        convlutedSignal=[]
        for n in range(N1+N2 - 1):
            summation=0
            idx=0
            for k in range(N1):
                idx=n-k
                if idx<0:
                    break
                elif idx >= N2:
                    continue
                else:
                    summation+=float(FirstSignal[k])*float(SecondSignal[idx])
            convlutedSignal.append(summation)
        return convlutedSignal
def preProcessed():
    obj1=Read()
    obj2=preProcessingData()
    obj3=preProcessingFilter()
    data_normal=obj1.NormalData()
    data_RBBB=obj1.RBBBData()
    data=np.concatenate((data_normal,data_RBBB),axis=0)
    normalizedData=obj2.NormalizeData(data)
    res=[]
    coeffecients=obj3.BandPassFilter(0.5,40,50,60,300)
    mycoeff=[]
    for key , value in coeffecients.items():
        mycoeff.append(value)
    mycoeff=np.array(mycoeff)
    for i in range(len(data)):
        convolutedSignal=obj3.DirectConvolutionSignal(normalizedData[i],mycoeff)
        res.append(convolutedSignal)
    res=np.asarray(res)
    return res
