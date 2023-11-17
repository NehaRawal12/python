# write a function which accepts a 2d list and rturns the transpose of it input=
# [1,3,7]
# [4,2,8]
# [11,8,9]
# output=[1,4,11]
# [3,2,8]
# [6,5,9]

def my_fun(arr):
    newarr=[]
    i=0 
    while i<len(arr):
        demo=[]
        j=0
        while j<len(arr):
            if j==i:
                j+=1
        
        i+=1
my_fun([[1,3,7],[4,2,8],[11,8,9]])
