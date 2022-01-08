# a=[[1,2,3],[4,5,6]]
# c=[]
# for i in range(3):
#     x=int(input())
#     c.append(x)
# a.append(c)

# print(a)

# import math
# def SqRt(y):
#     assert y>=0,'Negative Number' #->assertion 'statement'      
#     z=math.sqrt(y)
#     return z


# a=float(input())
# print(format(SqRt(a)))



#  2---------------------------------------------------------------------------

# def outer():
#     var=100
#     def inner():
#         print("Var for inner function", var)  # eg of enclosing scope
#     inner()
#     print("Var from outer function", var)

# outer()





# 3-----------------------------------------------------------------------------

# def f():
#     # x=7
#     print(x)       | # LEGB rule  ==>    L->local,   E->encolsing scope,   G->global,   B->builtin scope(eg: len())  | 
#     g()            |                                  #  |                                                           |                
#                    |                              #for nested functions                                              |            
# def g():
#     x=9
#     print(x)
#     h()

# def h():
#     print(x)


# # eg of enclosing scope

# def p():
#     a=34
#     def q():
#         b=67
#         print(a)  #->encolsung scope  in nested function
#         print(b)
#     q()
#     print(a)


# x=19
# p()

# f()



# 4-------------------------------------------------------

# def add(name="default", lastname="solanki"):
#     return name+ ' '+lastname

# a=add("anuj")

# print(a)



# 5---------------------------------------------------------------------

# def func(x):   # "x" is a copy of "x" defined in main function so value of "x" will not change
#     x=6        #  integer is immutable
#     print(id(x))

# x=2
# print(id(x))
# func(x)
# print(x)


# 6--------------------------------------------------------------

# def func(x):                   # here address of arrag is passed to the function   but not fot integers  like in cpp/c
#     for i in range(len(x)):    # array is mutable
#         x[i]=x[i]*2

# x=[1,2,3,4]
# print(x)
# func(x)
# print(x)

# 7----------------------------------------------------------

# def double(x):
#     x=x*2

#     return x   # we have to return the new integer to change it

# x=5
# print(x)
# x = double(x)
# print(x)



# 8--------------------------------------------------------------
#    RECURSION ---------------------------------------------

# def fact(n):
#     if n<=1:
#         return 1
#     return n+fact(n-1)

# print(fact(3))


# 9---------------------------------------------------------
# def fibo(n):
#     arr=[1,1]
#     for i in range(2,n):
#         arr.append(arr[i-1]+arr[i-2])

#     print(arr[n-1])

# fibo(4) 


#  10--------------------------------------------------------


# a={1:"hello",2: "anuj"}
# print(a)
# # a[2]="noob"
# # print(a )

# b=a.get(2) + " solnaki "
# print(b)

# ------------------------------------------------------------------

# a="anuj solanki"
# print(a)
# l=a.split(" ")

# -----------------------------------------------------------



# def checkParan(s):
#     # Write your code here
#     arr=[]
#     idx=[]
#     a='('
#     b=')'
#     c='['
#     d=']'
#     for i in range(len(s)):
#         if(s[i]==a):
#             arr.append(a)
#             idx.append(i)
#         elif(s[i]==b):
#             if(len(arr)==0):
#                 return str(i)
#             elif(arr[len(arr)-1]==c):
#                 return str(idx[len(idx)-1])
#             elif(arr[len(arr)-1]!=a):
#                 return str(i)
            
#             arr.pop()
#             idx.pop()
#         elif(s[i]==c):
#             arr.append(c)
#             idx.append(i)
#         elif(s[i]==d):
#             if(len(arr)==0):
#                 return str(i)
#             if(arr[len(arr)-1]==a):
#                 return str(idx[len(idx)-1])

#             elif(arr[len(arr)-1]!=c):
#                 return str(i)
            
#             arr.pop()
#             idx.pop()
#     if(len(arr)==0):
#         return "match"
#     else:
#         for i in range(len(s)):
#             if(arr[len(arr)-1]==s[i]):
#                 return str(i)

# print(checkParan("([)]"))



#  11--------------------------------------------------------------------------
#   NUMPY



# import numpy as np
# from numpy.random.mtrand import rand
# np.random.seed(0)
# #           lower limit  upper limit
#                 #     |  |                  
# x1=np.random.randint(0,2,size=6)  #onr-D array
# x2=np.random.randint(10,size=(5,4))  #2-D array
# temp=np.random.randint(10,size=(5,4))  #2-D array
# x3=np.random.randint(10,size=(3,4,5))  #3-D array
# #                               |--->tupple 

# x4=np.eye(3)  #identitity of matrix 3 3
# print(x4)


# print(x1)
# x1=x1[::2]
# print(x1)


# x5=np.ones((2,2,4))  # 2 matrix of size 2,4 with only value 1
# print(x5)


# x6=np.arange(2,2.1,0.01)
# print(x6)

# x7=np.linspace(2,6,num=10)
# print(x7)


# list = [[1,2,3],[4,5,6]]
# print(list)

# print(x2)    #|-----> also TUPPLE
# print(x2[1,2])

# print(x1.all())  # checks for zero in numpy array return true and false


# x8=np.array([[1,2,3],[4,5,6]])
# print(x8)

# a=x8.copy()
# print(a)
# print(x2)

# x10,x11,x12=np.split(x2,(1,2))   # goes from index (0-1) then (1-2)  then (2-last)
# print(x10)
# print(x11)
# print(x12)


# print(x2)
# # x2=x2*2       #
# # print(x2)
# print(x1)
# x15=np.matmul(x2 , x3)  #  multiplication of two matrix
# print(x15)



# 12------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
# xticks=np.linspace(0,100,num=1000)

# xvalues=xticks
# yvalues=np.log(xvalues)
# # yvalues=np.log(xvalues)

# plt.plot(xticks,yvalues)
# plt.grid(True)
# plt.xlabel('pi x n',fontsize=24)
# plt.ylabel('Amplitude',fontsize=24)
# plt.show()
# print(xvalues,yvalues)

# --------HISTOGRAM----------------------------------------------


# data=np.random.randint(8,size=20)
# bin=range(0,8)
# hdata=plt.hist(data,bins=bin)
# plt.grid(True)

# print(data)
# print(hdata[0]) # array  sum of counts = total num of samples in array(20)
# print(hdata[1]) # bin is present at index 1 in hdata
# plt.show()

# ---------------------------------------------------------

