#Given a binary search tree and a target node K. The task is to find the node with minimum absolute difference with given target value K.
#Amazon Experienced Interview Question
#Define class new node to initalize the node
#Sys is used to set INT_MAX
import sys

#Class to create objects of nodes of binary tree- with node with data and pointer to left and right side
class newnode:
    def __init__(self,data):
        self.key=data 
        self.left=None 
        self.right=None 

#Helper function to perform the traversal of the tree in order
def inOrder(root,aux_arr):
    if root:
        inOrder(root.left, aux_arr)
        aux_arr.append(root.key)
        inOrder(root.right,aux_arr)

#Approach 1- store in auxillary array by traversing array in order and taking absolute difference of each element and
#choose node with minimal difference with k.
def maxDiffApp1(root,k):
    #Initialize auxillary array
    aux_arr=[]
    #Run an inorder-traversal of binary tree
    inOrder(root,aux_arr)
    #print(aux_arr)
    #set initial values of absolute difference and value of node as INT_MAX
    abs_diff=sys.maxsize
    ans_node=sys.maxsize
    #Traverse through newly formed array and check if the absolute difference of i-k is less than the current value, update abs_diff and ans_node if so
    for i in aux_arr:
        if(abs(i-k)<abs_diff):
            abs_diff=abs(i-k) 
            ans_node=i
    #we have answer, print it        
        
    print(ans_node,"is the node that is closest to ", k)
#Function that implements maxDiffApp2
def maxDiff(root,k,min_diff,min_diff_key):
    #If empty
    if root==None:
        return
    #If root element is the exact same as k
    if root.key==k:
        min_diff_key[0]=k
        return
    #updating the value in case the absolute value of difference between element and k is less than previous value
    if min_diff > abs(root.key-k):
        min_diff=abs(root.key-k)
        min_diff_key[0]=root.key
    #If element is on left hand side
    if k<root.key:
        maxDiff(root.left,k,min_diff,min_diff_key)
    #If element is on right hand side
    else:
        maxDiff(root.right,k,min_diff,min_diff_key)
#Acts as wrapper around max_diff
def maxDiffApp2(root,k):
    min_diff, min_diff_key= sys.maxsize, [-1]
    maxDiff(root,k,min_diff,min_diff_key)
    print(min_diff_key,"is the node that is closest to ", k)


if __name__ == '__main__': 
    #Tree construction
    root = newnode(9)  
    root.left = newnode(4)  
    root.right = newnode(17) 
    root.left.left = newnode(3)  
    root.left.right = newnode(6) 
    root.left.right.left = newnode(5)  
    root.left.right.right = newnode(7)  
    root.right.right = newnode(22) 
    root.right.right.left = newnode(20)
    #Target node defined  
    k = 18
    maxDiffApp1(root, k)
    maxDiffApp2(root,k) 