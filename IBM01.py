def betterCompression(S):
    d = {}
    cur_num = 0
    cur_char = ''
    for i in range(len(S)):
        #zimu
        if S[i] in 'abcdefghijklmnopqrstuvwxyz':
            cur_char = S[i]
        #shuzi
        else:
            cur_num = cur_num*10+int(S[i])
            if i+1 >= len(S) or S[i+1] in 'abcdefghijklmnopqrstuvwxyz':
                if cur_char in d:
                    d[cur_char] += cur_num
                    cur_num = 0
                else:
                    d[cur_char] = cur_num
                    cur_num = 0
    ans = ''
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char in d:
            print('yes')
            ans+=char
            ans+=str(d[char])
    print(ans)
    return ans
betterCompression('a12b56c1')

