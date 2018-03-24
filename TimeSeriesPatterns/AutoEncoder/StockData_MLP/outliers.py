## Cleaning the outliers ## 
def outliers(A,nTh,pTh):  ## MrD is threshhold
    List=[]
    for i in range(len(A)):
        for j in range(len(A[i])):
            if nTh<=A[i][j]<=pTh:
                continue 
            else:
                print (j,A[i][j])
                List.append((i,j))
#    return List 
    for (x,y) in List:
        for i in range(len(A)):
            A[i][y]=(A[i][y-1]+A[i][y+1])/2.0
#    return 
