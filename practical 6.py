n=int(input("Enter number of students\t"))
s=[]
for i in range(n):
    r=int(input(f"Enter roll numbers \t"))
    s.append(r)

def binarysearch(arr, x):
    low = 0
    high = len(arr)- 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low)// 2
        if arr[mid]<x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

def linearsearch(a, k):
  
    for i in range(n):
  
        if a[i]== k:
           return i
            
    return -1
  
    
def sentinelsearch(arr,k):
    arr.append(k)
    index = 0
 
    while True:
        if arr[index] == k: 
            break
        index = index+1
    return index


keyf=int(input("Enter the element to be found using Binary search "))
binary=binarysearch(s,keyf)
print("the element is found at",binary)
keyl=int(input("Enter the element to be found using linear "))
l=linearsearch(s,keyl)
print("The element is found at ",l)
k=int(input("Enter the element to be found using sentineal search "))
se=sentinelsearch(s,k)
print("The element is found at ",se)
s.sort()