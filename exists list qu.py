# a=[1,3,5,4,7,9,12,9]
# for i in range (5):

# b=int(input('enter the number'))
# for i in range (8):
#     if b==i:
#         print('yes')
#     else:
#         print('no')
    # x=len(a)
    # if i==list(a):
    #     print('yes')
    # else:
    #     print('no')
a=[1,2,3,4,5,6,7,8,12,9]
# # b=int(input('enter the number'))
# x=len(a)
# for i in range (x):
#     if i==9:
#         a=True
#     else:
#         False
# if a==True:
#     print('yes')
# else:
#     print('no')
n=int(input("enter the number:"))
i=0
while i<len(a):
    if n in a:         
        print("yes")
        break
    else:
        print("no")
        break
i+=1

# n=int(input("enter the number:"))
# i=0
# p=[]
# while i<n:
#     a=int(input("enter the number:"))
#     p.append(a)
#     i+=1
# j=0
# consecutive=True
# while j<len(p):
#     if p[j]!=p[j-1]+1:
#         consecutive=False
#         break
# if consecutive==True:
#     print("yes")
# else:
#     print("no")