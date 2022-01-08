def fibo_arr(n):
    if(n<=0):
        return 0
    arr=[1,1]
    for i in range(n-2):
        arr.append(arr[i]+arr[i+1])
    return arr[n-1]


print(fibo_arr(16))