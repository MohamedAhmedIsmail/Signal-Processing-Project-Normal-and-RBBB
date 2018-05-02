import numpy as np
trainNormal_path="C:\\Users\\mohamed ismail\\Desktop\\Normal&RBBB\\Normal_Train.txt"
testNormal_path="C:\\Users\\mohamed ismail\\Desktop\\Normal&RBBB\\Normal_Test.txt"
trainRBBB_path="C:\\Users\\mohamed ismail\\Desktop\\Normal&RBBB\\RBBB_Train.txt"
testRBBB_path="C:\\Users\\mohamed ismail\\Desktop\\Normal&RBBB\\RBBB_Test.txt"
class Read:
    def __init__(self):
        pass
    def ReadData(self,path=None):
        file=open(path,'r')
        content=file.readlines()
        lst1=[]
        lst2=[]
        final_lst=[]
        for i in range(len(content)):
            lst2=[]
            for j in range(len(content[i])):
                if content[i][j] =='|':
                    mystr=''.join(map(str,lst1))
                    fltnum=float(mystr)
                    lst2.append(fltnum)
                    lst1=[]
                if content[i][j] !='|':    
                    lst1.append(content[i][j])
            final_lst.append(lst2)
        return final_lst
    def NormalData(self):
        trainNormal_list=self.ReadData(trainNormal_path)
        testNormal_list=self.ReadData(testNormal_path)
        Normal=np.concatenate((trainNormal_list,testNormal_list),axis=0)
        return Normal
    def RBBBData(self):
        trainRBBB_list=self.ReadData(trainRBBB_path)
        testRBBB_list=self.ReadData(testRBBB_path)
        RBBB=np.concatenate((trainRBBB_list,testRBBB_list),axis=0)
        return RBBB