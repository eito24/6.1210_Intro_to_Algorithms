##################################################
##  Problem 3.c. Find the Missing Number 2
##################################################

# Given n integers in the range [0,N] where n <= N, find an integer
# in the range [0,N] that is missing. If there are multiple missing numbers,
# return any of them. There is at least one number in the range that is missing.
def find_missing_int(arr, N): # O(n)
    '''
    Inputs:
        arr     (list(int)) | List of unsorted, unique positive integer order id's
        N       (int)       | A positive integer larger than len(arr)
    Output:
        -       (int)       | An integer in the range [0,N] not present in arr
    '''
    n = len(arr) # O(n)
    hasharr = [None]*(n+1) # O(n)
    for elem in arr:                # O(n)
        hashval = elem%(n+1)        # O(1)
        hasharr[hashval]=elem    # O(1)
    for i in range(n+1):    # O(n)
        if hasharr[i] is None:      # O(1)
            return i
    pass