def min_moves(n,c=0):
    if n == 1 and c==0:
        return -1
    if n % 6 != 0 and n!=1:
        return min_moves(n*2,c+1)
    if n%6 ==0 and n!=1:
        return min_moves(n//6,c+1)
    if n==1 and c>0:
        return c