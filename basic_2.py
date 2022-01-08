# def hello():
#     name='hello'#it is str type
#     age=12# it is a int type
#     school='iit'#it is str type
#     print(name+' '  + str(age) + " "+ school)
# hello()


# def hello1():
#     name='hello ramu'#it is str type
#     age=12673547# it is a int type
#     school='nit'#it is str type
#     print(name+' '  + str(age) + " "+ school)
# hello1()

# b='a'-20
# print(b)



# def stringOp(inpstr):
#     # Write your code here
#     if(len(inpstr)%2!=0):
#         print(inpstr+'*'+inpstr+'*'+inpstr)
#     else:
#         print("#"+inpstr+inpstr+"#")
# # if __name__ == '__main__':
# #     fptr = open(os.environ['OUTPUT_PATH'], 'w')

# #     inpstr = input()

# #     result = stringOp(inpstr)

# #     fptr.write(result + '\n')

# #     fptr.close()

# stringOp("hello")


# a="a"
# b=a.upper()
# print(b)


# def title_case(inputstr):
#     # Write yourcode here
#     a=inputstr[0]
#     a=a.upper()
#     inputstr[0]=a
#     for i in range(1,len(inputstr)-1):
#         if(inputstr[i-1]==" "):
#             b=inputstr[i]
#             b=b.upper()
#             inputstr[i]=b
#     return inputstr


# a=title_case("hello world")
# print(a)


# s="hello world"
# if(s[5]==" "):
    

# # print(s)
# def sumTrace(x, y):
#     # Write your code here
#     a=0
#     b=0
#     o1=int(len(x)**0.5)
#     o2=int(len(y)**0.5)
#     k=0
#     l=0
#     for i in range(o1):
#         a=a+x[k]
#         k=k+o1+1
#     for i in range(o2):
#         b=b+y[l]
#         l=l+o2+1
#     return a+b

# a=sumTrace([1,2,3,4],[1,2,3,4])
# print(a)



# def listop(data, z):
    # Write your code here
#     if z<0:
#         i=0
#         sum=0
#         while(data[i]!=0):
#             i+=1
#         for j in range(len(data)-i-1):
#             i=i+1
#             sum=sum+data[i]
#         return sum
#     elif z>0:
#         i=0 
#         sum=0
#         while(data[i]!=0):
#             sum=sum+data[i]
#             print(sum)
#             i+=1
#             if(i==len(data)-1):
#                 break
#         sum=sum+data
#         return sum   
    
#     elif(z==0):
#         return 0

# a=listop([1,2,3,3,4,5,5],5)
# print(a)


# inp="hello"
# inp=inp.replace(inp[0],'5')
# print(inp)


n=int(input())
arr=[]
for i in range(n):
    x=str(input())
    arr.append(x)
print(arr)
arr2=[]

count=1
# for i in range(n):
#     for j in range(n):
#         if(arr[i]==arr[j] and i==j):
#             arr2.append(arr[i])

for i in range(n):
    c=1
    for j in range(i):
        if(arr[i]==arr[j]):
            c+=1
    if(c<=1):
        count+=1
print(count-1)
    
# print(arr2)
# z=0
# for i in arr2:
#     print(z)
#     z+=1 
# print(z)