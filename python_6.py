list = [[1,2,3],[4,5,6]]
list2 = [[1,0,0],[0,1,0]]

def add(list1,list2):
    x=0
    y=0
    res=[]
    for i in list1:
        tempmat=[]
        for j in list1[x]:
            tempmat.append(0)
            y=y+1
        y=0
        res.append(tempmat)
        x=x+1
    x=0
    y=0
    for i in list1:

        for j in list1[x]:
            res[x][y]=list1[x][y]+list2[x][y] 
            y=y+1
        y=0
        x=x+1
    print("The sum of two matrix is :")
    print()
    display(res)
    return res

def display(list):
    j=0    
    for i in list:
       print(list[j])
       j=j+1
    print()

display(list)

display(list2)

res=add(list,list2)
