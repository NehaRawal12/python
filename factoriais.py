# fec=int(input('enter the number'))
# s=1
# i=1
# s1=0
# while i<=fec:
#     s=s*i
#     s1+=s
#     
#     i+=1
# print(s1)
n=int(input('enter the number'))
fec=1
for i in range(1,n+1):
    fec=fec*i
    print(n,'is', fec)