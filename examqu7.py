# x=int(input('enter the number'))
# y=int(input('enter the number'))
# if x>y:
#     smaller=y
# else:
#     smaler=x
# for i in range (1,smaller+1):
#     if (x%i==0 and y%i==0):
#         hcf=i
#     lcm=(x*y)/hcf
# print (hcf)
# print(lcm)
a=int(input('enter the number'))
b=int(input('enter the number'))
while a%b!=0:
    rem=a%b
    a=b
    b=rem
print('hcf is ',b)