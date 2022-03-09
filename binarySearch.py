import math


#
#
#
#
# def binarySearch(list, n):
#     left = 0
#     right = len(list)-1
#     while left < right:
#         middle = math.floor((right + left)/2)
#         print('middle'+str(middle))
#         if n > list[middle]:
#             left = middle+1
#             print("left"+str(left))
#         else:
#             right = middle
#             print("right"+str(right))
#     list.insert(left+1 if left==len(list)-1 else left, n)
#     return list
#
#
#
# testArr = [1,2,4]
# testN = 5
#
# print(binarySearch(testArr, testN))





d = dict()

def findPairs(list):
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            s = list[i]+list[j]
            arr = [list[i],list[j]]
            if d.__contains__(s):
                temp = d.get(s)
                temp.append(arr)
                d.update({s:temp})
            else:
                d.update({s:[arr]})
    for n in list:
        if d.__contains__(n):
            for l in d.get(n):
                l.insert(0,n)
                print(l)


test = [1,2,3,4,5,6,7,8,9]

findPairs(test)
