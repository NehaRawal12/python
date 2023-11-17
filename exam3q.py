
'qustion number 3'
gender=input('enter the name')
age=int(input('enter the number'))
day=int(input('enter the number'))
salary=int(input('enter the number'))
totel=day*salary
print(totel)

if  gender=='m' and age>=18 and age<30:
    print(700)
elif  gender=='f' and age>=18 and age<30:
    print(750)
elif gender=='m' and age>=30 and age<=40:
    print(800)
elif gender=='f'and age>=30 and age<=40:
    print(850)


'qustion number 1 '
a=int(input('enter the number'))
b=int(input('enter the number'))
c=a%b
d=a-c
print(d)


'qustion number 2'
year =int(input('enter the number'))
if year%400==0:
    print('yes')
    if year%4==0:
        if year%100!=0:
            print('yes')
    
        
    else:
        print('no')
else:
    print('no')



'qustion number 7'
n=int(input('enter the number'))
count=0
i=1
while i<=n:
    if n%i==0 and i%2!=0:
        print(i)
    i=i+1
if n%i==0:
    print('prime number')
else:
    print('no')

    
'qustion number 5'
x=int(input('enter the number'))
n=int(input('enter the number'))
i=5
while i<n:
    c=2-(x*x*x)/3+(x*x*x*x*x)/5-(x*x*x*x*x*x*x)/7+(x*x*x*x*x*x*x*x*x)/9-(x*x*x*x*x*x*x*x*x*x*x)/11
    print(c)
    i=i+1
