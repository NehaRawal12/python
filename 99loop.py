a=int(input('enter the number'))
b=int(input('enter the number'))
p=a*b
while b>0:
    r=a%b
    a=b
    b=r
    hcf=a
    lcm=p//hcf
    print(hcf,lcm)