import pywt
import numpy as np
from PreProcessing import preProcessed 
class ExtractFeatures:
    def __init__(self):
        pass
    def waveletTransform(self,a=None,wavelet=None,Level=None):
      if Level>4:
          Level=1
      mylst=[]
      coeffs = pywt.wavedec(a, wavelet, level=Level)
      if Level ==1:
          cA1,cD1=coeffs
          cA1=np.array(cA1)
          cD1=np.array(cD1)
          for i in range(len(cA1)):
              if cA1[i]>=0.5 and cA1[i]<=40:
                  mylst.append(cA1[i])
              if cD1[i]>=0.5 and cD1[i]<=40:
                  mylst.append(cD1[i])
      if Level==2:
          cA2, cD2, cD1 = coeffs
          cA2=np.array(cA2)
          cD2=np.array(cD2)
          cD1=np.array(cD1)    
          for i in range(len(cA2)):
              if cA2[i]>=0.5 and cA2[i]<=40:
                  mylst.append(cA2[i])
              if cD2[i]>=0.5 and cD2[i]<=40:
                  mylst.append(cD2[i])
          for i in range(len(cD1)):
              if cD1[i]>=0.5 and cD1[i]<=40:
                  mylst.append(cD1[i])
      if Level==3:
          cA3, cD3, cD2,cD1 = coeffs
          cA3=np.array(cA3)
          cD3=np.array(cD3)
          cD2=np.array(cD2)
          cD1=np.array(cD1)
          for i in range(len(cA3)):
              if cA3[i]>=0.5 and cA3[i]<=40:
                  mylst.append(cA3[i])
              if cD3[i]>=0.5 and cD3[i]<=40:
                  mylst.append(cD3[i])
          for i in range(len(cD2)):
              if cD2[i]>=0.5 and cD2[i]<=40:
                  mylst.append(cD2[i])
          for i in range(len(cD1)):
              if cD1[i]>=0.5 and cD1[i]<=40:
                  mylst.append(cD1[i])
      if Level==4:
          cA4, cD4,cD3, cD2,cD1 = coeffs
          cA4=np.array(cA4)
          cD4=np.array(cD4)
          cD3=np.array(cD3)
          cD2=np.array(cD2)
          cD1=np.array(cD1)
          for i in range(len(cA4)):
              if cA4[i]>=0.5 and cA4[i]<=40:
                  mylst.append(cA4[i])
              if cD4[i]>=0.5 and cD4[i]<=40:
                  mylst.append(cD4[i])
          for i in range(len(cD3)):
              if cD3[i]>=0.5 and cD3[i]<=40:
                  mylst.append(cD3[i])
          for i in range(len(cD2)):
              if cD2[i]>=0.5 and cD2[i]<=40:
                  mylst.append(cD2[i])
          for i in range(len(cD1)):
              if cD1[i]>=0.5 and cD1[i]<=40:
                  mylst.append(cD1[i])
      return mylst
def Features(wavelet=None,Level=None):    
    preProcessedData=preProcessed()
    Obj=ExtractFeatures()
    res=[]   
    for i in range(len(preProcessedData)):
        wavelet2=Obj.waveletTransform(preProcessedData[i],wavelet,Level)
        res.append(wavelet2)
    maxi=-1e9
    for i in range(len(res)):
        if len(res[i])>maxi:
            maxi=len(res[i])
    for i in range(len(res)):
        mini=len(res[i])
        for j in range(mini,maxi):
            res[i].append(0)
    return res