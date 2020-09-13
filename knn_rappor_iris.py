# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 15:35:07 2020

@author: 123
"""

import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from knn import knn_classifier

from bloomfilter import BloomFilter
import time


totalnum=256

f=0.1
p=0.15
q=0.85
maximum=150
precision=1

k=5
num_class=3

def rappor(n,f,p,q,m):
    n=str(n)
    bloom=BloomFilter()
    noisydata=bloom.add_data(n,m)
    
    
# Permanent randomized response  
    for i in range(len(noisydata)):
        choose=np.random.randint(0,totalnum)
        if noisydata[i]==1:
            if choose/totalnum<=f/2:
                noisydata[i]=0
        else:
            if choose/totalnum<=f/2:
                noisydata[i]=1

                
                    

                    
    # Instantaneous randomized response
    for i in range(len(noisydata)):
         choose=np.random.randint(0,totalnum)
         if noisydata[i]==1:
             if choose/totalnum<=1-q:
                 noisydata[i]=0
         else:
             if choose/totalnum<=p:
                 noisydata[i]=1
                 
    return noisydata

def create_table(table,f,p,q,m):
    for i in range(maximum):
        n=round(i/pow(10,precision),precision)  
        table[n]=rappor(n,f,p,q,m)
        
        
        
def compare(data1,data2):
    same=0
    for i in range(len(data1)):
        if(data1[i]==data2[i]):
            same+=1
    return (same/totalnum)*100


def guess(data):
    m=0
    r=0
    for i in range(maximum):
        n=round(i/pow(10,precision),precision)
        similarity=compare(data,table[n])
        if(similarity>m):
            m=similarity
            r=n
    return r
    


if __name__=='__main__':
    t1=time.time()
    
    
    iris=datasets.load_iris()
    iris_data=iris.data
    iris_label=iris.target


    times=1
    m=110
    
    for exp in range(1):
        
        
        
        table={}
        create_table(table,f,p,q,m)
        
        totalCorrectPosibility=1
        for t in range(times):
            train_data, test_data,  train_label,  test_label=train_test_split(iris_data,iris_label,test_size=0.3)
            


            testLength=len(test_data)
            
            Rappor_trainData=[]
            for i in range(len(train_data)):
                t=[]
                for j in range(len(train_data[i])):
                    t.append(rappor(train_data[i][j],f,p,q,m))
                Rappor_trainData.append(t)

            Rappor_testData=[]
            for i in range(len(test_data)):
                t=[]
                for j in range(len(test_data[i])):
                    t.append(rappor(test_data[i][j],f,p,q,m))
                Rappor_testData.append(t)
        
        
        
            ###server接到rappor後的資料 利用table查詢相似度###
            for i in range(len(Rappor_trainData)):
               for j in range(len(Rappor_trainData[i])):
                   Rappor_trainData[i][j]=guess(Rappor_trainData[i][j])
                   
                   

            for i in range(len(Rappor_testData)):
                for j in range(len(Rappor_testData[i])):
                    Rappor_testData[i][j]=guess(Rappor_testData[i][j])
                    






            result=knn_classifier(Rappor_trainData,Rappor_testData,train_label,k,num_class)
    
            
           # result2=knn_classifier(train_data,test_data,train_label,k,num_class)
            

        
            correct=0
            for i in range(len(result)):
                if(result[i]==test_label[i]):
                    correct+=1;
            
            print("原始結果",test_label.tolist())
            print("預測結果",result)
            print("正確率",correct/testLength*100,"%")
            print()

