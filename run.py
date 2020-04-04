def issafe(arr,row,col,n,k,l,val):
    if val>n:
        val=0
        return arr
    r=[]
    row=row
    col=col
    row1=0
    while row1<n:
        r.append(arr[col][row1])
        row1+=1
    #print(val,arr[row],r)
    if val not in arr[row] and val not in r:
        arr[row][col]=val
        #print('$$$$$$$$$',arr[row][col])
        return True
    else:
        #print('QQQQQQQQ')
        issafe(arr,row,col,n,k,l,val+1)
def solve(arr,row,col,n,k,l,val):
    val=val
    if col>n:
        col=0
        return col 
    if val>n:
        val=0
        return val
    else:
        i=0
        j=0
        trace=0
        while i<n:
            trace+=arr[i][j]
            if trace==k:
                #print('wwwwwwww',arr)
                break
                return l
            i+=1
            j+=1
        #print('trace',trace)
        issafe(arr,row,col,n,k,l,val)
        for row in range(0,n):
            print(row,col)
            solve(arr,row,col+1,n,k,l,val+1)
arr=[]
for i in range(0,3):
    arr.append([0 for j in range(3)])
l=[]
print(arr)
solve(arr,0,0,3,6,[],1)
print(l)
