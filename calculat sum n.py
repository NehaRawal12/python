# num=int(input('enter the number'))
# s=0
# sum=0
# print ('series are',end= " ")
# for i in range(0, num):
#     s=s*10+1
#     print(s,end= " ")
#     sum=sum+s
# print ()
# print ('series sum=' ,sum)

n=int(input('enter the number'))

x=5
p=5
s=0
i=1
while i<=n:
    s+=p
    p=p*10+x
    i+=1
print(s)

