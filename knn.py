# -*- coding: utf-8 -*-
"""
Created on Sat May  9 15:20:35 2020

@author: cychung
"""


from sklearn import datasets
from sklearn.model_selection import train_test_split
import time

k=5
num_class=3

def Euclidean_distance(data1,data2):
    sum=0
    for i in range(len(data1)):
        sum+=(data1[i]-data2[i])**2
    sum=sum**0.5
    return sum

def rN_classifier(train_data,test_data,train_label,r):
    result=[]
    for i in test_data:
        dataInCircle=[]
        for j in range(len(train_data)):
            distance=Euclidean_distance(i,train_data[j])
            if(distance<=r):
                dataInCircle.append(train_label[j])
        label_zero=0
        label_one=0
        label_two=0
        for k in range(len(dataInCircle)):
            if(dataInCircle[k]==0):
                label_zero+=1
            elif(dataInCircle[k]==1):
                label_one+=1
            else:
                label_two+=1

        maximum=label_zero
        m=0
        if(label_one>maximum):
           maximum=label_one
           m=1
        if(label_two>maximum):
            maximum=label_two
            m=2
        result.append(m)
    return result
    

    
def  knn_classifier(train_data,test_data,train_label,k,Num_class):
    result=[]
    for i in test_data:
        DAL={}                                                  ##DAL=DistanceAndLabel
        for j in range(len(train_data)):
            
            distance=Euclidean_distance(i,train_data[j])
            DAL[distance]=train_label[j]
            
        SDAL=sorted(DAL.items(),key=lambda x:x[0])              ##SDAL=SortedDistanceAndLabel    (將每個train data離 test data的距離由小到大排序)
        
        predict_label={}
        for i in range(Num_class):
            predict_label.update({i:0})
            
        KSDAL=SDAL[0:k]
        
        if(len(SDAL)<k):
            k=len(SDAL)
        
        for i in range(k):
            predict_label[(KSDAL[i])[1]]+=1

            
        SPL=sorted(predict_label.items(),key=lambda x:x[1],reverse=True)

        result.append(SPL[0][0])

    return result
    


if __name__ == '__main__':
    iris=datasets.load_wine()
    iris_data=iris.data
    iris_label=iris.target
    t1=time.time()
    false=0
    for i in range(10):
        train_data, test_data,  train_label,  test_label=train_test_split(iris_data,iris_label,test_size=0.2)
        print(len(test_data))
        #result=rN_classifier(train_data,test_data,train_label,0.7)
        result=knn_classifier(train_data, test_data, train_label, k,num_class)



        ##計算正確率
        correct=0
        for i in range(len(result)):
            if(result[i]==test_label[i]):
                correct+=1


        print(correct/len(test_data)*100)

        ##print(str(correct/len(result)*100)+"%")
    t2=time.time()


