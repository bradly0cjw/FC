def selectionsort(data):
    for wall in range(len(data)-1):
        m=10000000000
        for i in range(wall,len(data)):
            if data[i]<m:
                m=data[i];
                idx=i;
            data[wall],data[idx]=data[idx],idx[wall]
        return data
unsorted=[2,9,4,8,5,1,7,3,6];
sort=selectionsort(unsorted);
print(sort) 