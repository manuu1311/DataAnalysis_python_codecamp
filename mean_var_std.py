import numpy as np

def calculate(arr):
    if len(arr)!=9:
        raise ValueError('List must contain nine numbers.')
    
    arr=np.array(arr).reshape((3,3))
    ret={}
    m0=list(np.mean(arr,axis=0))
    m1=list(np.mean(arr,axis=1))
    m2=np.mean(arr)
    ret['mean']=[m0,m1,m2]

    var0=list(np.var(arr,axis=0))
    var1=list(np.var(arr,axis=1))
    var2=np.var(arr)
    ret['variance']=[var0,var1,var2]

    std0=list(np.std(arr,axis=0))
    std1=list(np.std(arr,axis=1))
    std2=np.std(arr)
    ret['standard deviation']=[std0,std1,std2]

    max0=list(np.max(arr,axis=0))
    max1=list(np.max(arr,axis=1))
    max2=np.max(arr)
    ret['max']=[max0,max1,max2]

    min0=list(np.min(arr,axis=0))
    min1=list(np.min(arr,axis=1))
    min2=np.min(arr)
    ret['min']=[min0,min1,min2]

    sum0=list(np.sum(arr,axis=0))
    sum1=list(np.sum(arr,axis=1))
    sum2=np.sum(arr)
    ret['sum']=[sum0,sum1,sum2]
    return ret
