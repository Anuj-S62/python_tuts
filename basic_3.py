# const=5;

# x = int(input('enter the value: '))

# if(x>const):
#     print("input is greater than "+ str(const))

# elif (x==const):
#     print("equal to "+ str(const))

# else:
#     print("less than "+ const)
    

def convertor(min):
    hour=(min/60)*100
    return hour

 
min = int(input('enter the minutes: '))
if(min>=60):
    print("Error")

elif(min<0):
    print("ERROR")

else:
    hour = convertor(min)
    print(str(hour)+ "% of an hour")


