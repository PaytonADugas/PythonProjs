import math

pos = []

def sws(arr, s):
    arr.sort()
    for i in range(len(arr)-1):
        sum = 0
        l = i
        for j in range(i, len(arr)):
            r = j
            sum += arr[j]
            if sum == s:
                pos.append(arr[l:r+1])
            elif sum > s:
                break

sws([1,2,3,4,5,6,7,8,9], 15)

pos = []

def sws_i(arr, s):
    l=0
    r=1
    sum = arr[l]
    while l < len(arr) and r < len(arr):
        if sum == s:
            pos.append(arr[l:r])
            sum-=arr[l]
            l+=1
        elif sum > s:
            sum-=arr[l]
            l+=1
        else:
            sum+=arr[r]
            r+=1


sws_i([10,6,3,7,9,0,7,5,6,3,2],16)

print(pos)
