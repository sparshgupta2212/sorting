def InsertionSortList(l):
    # with while loop
    for i in range(1,len(l)):
        key=l[i]
        j=i-1
        while j>-1 and l[j]<key:
            l[j+1]=l[j]
            j=j-1
        l[j+1]=key
        # with th for loop
        '''
        for i in range (1,len(l)):
            key=l[i]
            for j in range(1,-1,-1):
                if l[j]<key:
                    l[j+1]=l[j]
                    l[j]=key
        '''
    return l
l=[45,66,1,12,22,90,89,74,5,15]
print(InsertionSortList(l))