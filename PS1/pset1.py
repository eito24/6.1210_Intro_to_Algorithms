##################################################
##  Problem 3.4. Find order
##################################################

# Given a list of positive integers and the starting integer s, return x such that x is the smallest value greater than
# or equal to s that's not present in the list

def find_first_missing_element(arr, s):
    '''
    Inputs: 
        arr        (list(int)) | List of sorted, unique positive integer order id's
        s          (int)       | Positive integer
    Output: 
        -          (int)       | The smallest integer greater than or equal to s that's not present in arr
    '''
    ##################
    # YOUR CODE HERE #
    ##################
    def bin_search(A,s):
        n = len(A)
        if n == 0:
            return False
        if n == 1:
            if A[0] == s:
                return True
            else: return False
        if n == 2:
            m = 1
        elif n % 2 == 0:
            m = int(n/2)-1
        else: m = int((n+1)/2)-1
        if A[m] == s:
            return True
        elif A[m] > s:
            return bin_search(A[:m],s)
        else: return bin_search(A[m:],s)
    def larger_than_s(A,s):
        n = len(A)
        if n == 1:
            if A[0]>s: return A[0]+1
            else: return s+1 
        if n == 2:
            m = 1
        elif n % 2 == 0:
            m = int(n/2)-1
        else: m = int((n+1)/2)-1
        if A[m] <= s:
            return larger_than_s(A[m:],s)
        else:
            if A[0]<=s:
                x = A[m]
                d = x-s
                i = m-d
                if i<0:
                    return larger_than_s(A[:m],s)
                if A[i]==s:
                    return larger_than_s(A[m:],s)
                else:
                    return larger_than_s(A[:m],s)
            else:
                x = A[m]
                d = x-A[0]
                i = m-d
                if i<0:
                    return larger_than_s(A[:m],s)
                if A[i]==A[0]:
                    return larger_than_s(A[m:],s)
                else:
                    return larger_than_s(A[:m],s)
    s_in_A = bin_search(arr,s)
    if not s_in_A: return s
    else: return larger_than_s(arr,s)