n=int(input("enter the number:"))
s=0
f=1
i=1
while i<=n:
    f=f/i
    s+=f
    i+=1
print(s)