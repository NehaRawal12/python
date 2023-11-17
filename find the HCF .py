# x =int(input('enter the number'))
# y=int (input('entr the number'))
# if x>y:
#     smallar=y
# else:
#     smallar=x
# for i in range(1,smallar +1):
#     if (x%i==0 and y%i==0):
#         hcf=i
#     lcm=(x*y)/hcf
# print ('the hcf of',x,'and',y,'is',hcf)
# print('the lcm of',x,'and',y,'is',lcm)


a=int(input('enter the number'))
b=int(input('enter the number'))
if a%b!=0:
    rem=a%b
    a=b
    b=rem
print('hcf',b)
