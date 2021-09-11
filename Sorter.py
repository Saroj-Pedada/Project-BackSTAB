def sortByRow(mat, n, ascending):
    for i in range(n):
        if (ascending):    
            mat[i].sort()
        else:
            mat[i].sort(reverse=True)
    return mat