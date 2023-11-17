# s=int(input('enter size of list'))
# a=[]
# for i in range (s):
#     val=int(input('enter value number'))
#     a.append (val)
#     k=int(input('enter the sarch value)



# def binary (a,s,k):
#     i=0
#     j=s-1
#     t=0
#     while i<j:
#           mid=i+j//2
#           if a[mid]==k:
#               f=1
#               x=mid+1
#           if a[mid]>k:
#                 r=mid-1
#           if a[mid]<k:
#               i=mid+1
# if t==1:
#     print(x)
# else:
#     print('no')
# s=int(input('enter the number'))
# a=[]
# for i in range (s):
#      v=int(input('enter the number'))
#      a.append(v)
#      k=int(input('enter the sarch value'))



l=[1,2,3,4,5,6,7,8,9]
target =0
left= 0
right=len(1)-1
while left<= right:
    mid=(left+right)//2
    if l[mid]==target:
        print('eleme found')
        break
    elif l[mid]<target:
        left=mid+1
    else:
        right=mid-1
else:
    print('element not found')


