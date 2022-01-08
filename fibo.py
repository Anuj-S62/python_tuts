#FIBONACCI

# def fib(n):
#     if(n<=0):
#         return 0
#     elif(n<=2):
#         return 1
#     return fib(n-1)+fib(n-2)

# print(fib(6))



# # CHECK:-EVEN/ODD

# def check(a):
#     if(a%2==0):
#         print("EVEN")
#     else:
#         print("ODD")

# check(64)


# def multiple(a):
#     if(a%4==0):
#         print("muliple of 4")
#     elif a%6==0:
#         print("muliple of 6")
#     else:
#         print("not multiple of 4 and 6")


# multiple(int(input("enter num:")))

## --------- factorial using recursion-------------------



# def factorial(a):
#     if(a<0):
#         return 0
#     elif(a==0):
#         return 1;
#     return a*factorial(a-1);

# print(factorial(1000))



## ----------------factorial using loop-------------------

# def factorial(n):
#     if(n<0):
#         return 1
#     else:
#         fact=1
#         for i in range(n):
#             fact=fact*(i+1)
#         return fact
        
# print(factorial(1000))