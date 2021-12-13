import math

# better nonrecursive binary search
def binarySearch(list, n):
    left = 0
    right = len(list)-1
    while left < right:
        middle = math.ceil((left + right)/2)
        if n >= list[middle]:
            left = middle+1
        else:
            right = middle-1
    return left

# recursive binary search
def r_binarySearch(left, right, list, n):
        middle = math.ceil((left + right)/2)
        if left >= right:
            return left
        elif n >= list[middle]:
            left = middle+1
            return r_binarySearch(left, right, list , n)
        else:
            right = middle-1
            return r_binarySearch(left, right, list, n)

testArr = [2,3,5,7,8]
testN = 7

testArr.insert(r_binarySearch(0, len(testArr)-1, testArr, testN), testN)

print(testArr)

testArr = [2,3,5,7,8]
testN = 7

testArr.insert(binarySearch(testArr, testN), testN)

print(testArr)
