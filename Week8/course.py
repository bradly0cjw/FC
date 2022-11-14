def selectionsort(data):
    for wall in range(len(data)-1):
        m=10000000000
        for i in range(wall,len(data)):
            if data[i]<m:
                m=data[i]
                idx=i
            data[wall],data[idx]=data[idx],data[wall]
        return data
unsorted=[2,9,4,8,5,1,7,3,6]
sort=selectionsort(unsorted)
print(sort) 

def bubblesort(data):
    for wall in range(len(data)-1):
        for i in range(len(data)-1,wall+1,-1):
            if data[i]<data[i-1]:
                data[i],data[i-1]=data[i-1],data[i]
    return data    
unsorted=[2,9,4,8,5,1,7,3,6]
sort=bubblesort(unsorted)
print(sort)

def insertionsort(data):
    for wall in range(1,len(data)):
        for i in range(wall+1,0,-1):
            if data[i]<data[i-1]:
                data[i],data[i-1]=data[i-1],data[i]
            else:
                break    
    return data    
unsorted=[2,9,4,8,5,1,7,3,6]
sort=insertionsort(unsorted)
print(sort)

def binarySearch4sqrt(N,f,l):
    m=(f+l)/2
    if abs(m*m-N)<0.000001:
        return m
    else:
        if m*m>N:
            return binarySearch4sqrt(N,f,m)
        else:
            return binarySearch4sqrt(N,m,l)   
print(binarySearch4sqrt(2,1,2))             