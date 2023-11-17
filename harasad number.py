a=int(input('enter the number'))
sum=0
x=a
while (x>0):
    rem=x%10
    sum=sum+rem
    x=x//10
if a%sum==0:
    print(a,'harasad number')
else:
    print(a,'not harasad number')