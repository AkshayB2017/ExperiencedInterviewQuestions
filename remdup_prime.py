#Given an array of primes such that the range of primes is small. Remove duplicates from the array.
#Input: arr[] = {3, 5, 7, 2, 2, 5, 7, 7};
#Output: arr[] = {2, 3, 5, 7}
#All the duplicates are removed from 
#the array. The output can be printed in any order.


#Amazon Interview Questions- Experienced

#Approach One
def solution1(arr):
    #Complexity of O(n^2)- uses two loops to determine whether a particular number has been already marked in array
    #setting the index of the new array
    res_ind=1
    #Initializing first loop
    for i in range(1, len(arr)):
        j=0
        #from j=0 to i within second loop
        while(j<i):
            #when encountering a repeated element 
            if(arr[i]==arr[j]):
                break
            j+=1
        #if the element has not been found to be repeated, add it to new array.    
        if(j==i):
            arr[res_ind]=arr[i]
            res_ind+=1
    #only the unique elements will be present in array- no duplicates
    arr=arr[0:res_ind]
    #print the new array elements
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print("\n")

#This solution involves the use of sorting to simplify the process
def solution2(arr):
    #Get out of jail card- sort array immediately 
    arr.sort()
    first=0
    #Iterate through for loop and see if the elements are unique, if so add them to beginning of array
    for i in range(1, len(arr)):
        if arr[i]!=arr[i-1]:
            arr[first+1]=arr[i]
            first+=1
    #Now remove the extra items at end of array
    arr=arr[0:first+1]
    #print the new array elements
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print("\n")
#Hashing solution
def solution3(arr):
    #Create a set from elements
    hasharray=set(arr)
    #Add the sets back to array
    arr=hasharray 
    #print the new array elements
    for i in arr:
        print(i, end=" ")
    print("\n")

arr=[3,5,7,2,2,5,7,7]
print("Entering solution 1")
solution1(arr)
print("Entering solution 2")
solution2(arr)
print("Entering solution 3")
solution3(arr)
