def count_paths(F):
    '''
    Input:  F | size-n direct access array of size-n direct access arrays
              | each F[i][j] is either 't', 'm', or 'x'
              | for tree, mushroom, empty respectively
    Output: p | the number of distinct optimal paths in F
              | starting from (0,0) and ending at (n-1,n-1)
    '''
    p = 0
    n = len(F)
    M = [[float('-inf')]*(n+1)]*(n+1)
    P = [[0]*(n+1)]*(n+1)
    for i in range(1,n+1):
        for j in range(1,n+1):
            if F[i-1][j-1]=='t':
                M[i][j]=float('-inf')
                P[i][j]=0
            if i==1 and j==1:
                M[i][j]=0
                P[i][j]=1
            if F[i-1][j-1]=='m':
                M[i][j]=max(M[i-1][j],M[i][j-1])+1
                if M[i][j]==M[i-1][j]+1:
                    P[i][j]=P[i][j]+P[i-1][j]
                if M[i][j]==M[i][j-1]+1:
                    P[i][j]=P[i][j]+P[i][j-1]
                else:
                    P[i][j]=0
            if F[i-1][j-1]=='x':
                M[i][j]=max(M[i-1][j],M[i][j-1])
                if M[i][j]==M[i-1][j]:
                    P[i][j]=P[i][j]+P[i-1][j]
                if M[i][j]==M[i][j-1]:
                    P[i][j]=P[i][j]+P[i][j-1]
                else:
                    P[i][j]=0
    print(P)
    print(M)
    return P[n][n]