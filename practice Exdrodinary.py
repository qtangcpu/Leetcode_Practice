def func(input_str):
    n = len(input_str)
    dic = {'a':1,'b':1,'c':2,'d':2,'e':2,'f':3,'g':3,'h':3,'i':4,'j':4,'k':4,'l':5,'m':5,'n':5,'o':6,'p':6,'q':6,'r':7,'s':7,'t':7,'u':8,'v':8,'w':8,'x':9,'y':9,'z':9}
    matrix = [[0]*n for i in range(n)]
    ans = n
    for i in range(n):
        matrix[i][i] = dic[input_str[i]]
    for length in range(1,n):
        for r in range(n):
            c = r+length
            if c >= n:
                continue
            matrix[r][c] = matrix[r][c-1] + dic[input_str[c]]
            if matrix[r][c] % (length+1) == 0:
                ans +=1
    return ans
