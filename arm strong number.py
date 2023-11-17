n=int(input('enter the number '))
r=n
sum=0
while n>0:
    sum=sum+(n%10)*(n%10)*(n%10)
    n=n//10
if r==sum:
    print("is aremstrong number")
else:
    print('is not armstrong number')
