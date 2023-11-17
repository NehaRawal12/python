# a=['hello',2,5,8,10,5,8,20,8,20]
# b=[]
# for i in range (len(a)):
#     print(i)
#     for j in range(i+1,len(a)):
#         print(j)
#         if a[i]==a[j] and a[i]:
#             b.append (a[i])
# print(b)


# a=[2,3,4,2,5,7,8,3,9,5,6,7,9]
# d=set()
# b=[]
# for x in  (a):
#     if x not in d:
#         b.append (x)
#         d.add(x)
# print(d)

a=[2,6,8,3,2,3,7,9,1,9,5,4]
set_a=set(a)
u=list(set_a)
print(u)