
s=int(input('enter the number'))
i=0
l=[s]
for i in range (s):
    a=int(input('enter the value number'))
    l.append(a)
k=4
l = 0
r = s-1
f = 0
while l <= r:
    mid = (l + r) // 2
    if l[mid] == k:
        f = 1
    elif l[mid] > k:
        r = mid - 1
    else:
        l=mid+1
if f==1:
    print(f"element{k} found at index {mid}.")
else:
    print(f"Element {k} not found in the list.")

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# k = 7
# left = 0
# right = len(list) - 1
# f= False
# while left <= right:
#     mid = (left + right) // 2
#     if list[mid] == k:
#         f = True
#         break
#     elif list[mid] < k:
#         left = mid + 1
#     else:
#         right = mid - 1
# if f is True:
#     print(f)
# else:
#     print('no')
