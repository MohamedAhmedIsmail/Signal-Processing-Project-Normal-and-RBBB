from FeaturesExtraction import Features
from sklearn import svm
from sklearn.model_selection import train_test_split
from neupy import algorithms
import numpy as np
class Classify:
    def y_label(self):
        y_normal=np.ones(400)
        y_RBBB=np.zeros(400)
        y=np.concatenate((y_normal,y_RBBB))
        return y
    def prepareData(self):
        X=Features("db1",4)
        y=self.y_label()
        return X,y
    def SVM(self):
        X,y=self.prepareData()
        X_train,X_test,y_train,y_test=train_test_split(X, y, test_size=0.2,random_state=1)
        X_train=np.array(X_train,dtype=np.float32)
        X_test=np.array(X_test,dtype=np.float32)
        y_test=np.array(y_test,dtype=np.int32)
        clf = svm.SVC()
        clf.fit(X_train, y_train)
        y_predict = clf.predict(X_test)
        return y_predict,y_test
    def PNN(self):
        X,y=self.prepareData()
        X_train,X_test,y_train,y_test=train_test_split(X, y, test_size=0.2,random_state=1)
        X_train=np.array(X_train,dtype=np.float32)
        X_test=np.array(X_test,dtype=np.float32)
        y_test=np.array(y_test,dtype=np.int32)
        pnn=algorithms.PNN(std=10,verbose=False)
        pnn.train(X_train,y_train)
        y_predict=pnn.predict(X_test)
        return y_predict,y_test
    def Accuracy(self,y_predict,y_test):
        count = 0
        for i in range(len(y_predict)):
            if y_predict[i] == y_test[i]:
                count += 1
        Accuracy = (count / len(y_predict))*100
        return Accuracy
obj=Classify()
y_predict,y_test=obj.SVM()
y_predict2,y_test2=obj.PNN()
Accuracy1=obj.Accuracy(y_predict,y_test)
Accuracy2=obj.Accuracy(y_predict2,y_test2)
print()
print("SVM Accuracy= ",Accuracy1,"%")
print("PNN Accuracy= ",Accuracy2,"%")
