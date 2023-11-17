p=int(input('enter the number'))
q=int(input('rnter the number'))
n=20
i=1
s=0
while i<n:
    if i%p==0 and i%q!=0:
        s=s+i
    i=i+1
print(s)
