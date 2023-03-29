def time_taken(s, keyboard):
    """
    Strategy: map letter to key index. for each char in text, lookup char in map and get abs val diff
    to curr position, add to res. update curr position.
    """
    dic = {}
    for i in range(3):
        for j in range(3):
            dic[keyboard[i*3+j]] = [i,j]
    cur = s[0]
    ans = 0
    for letter in s[1:]:
        ans += max(abs(dic[cur][0]-dic[letter][0]), abs(dic[cur][1]-dic[letter][1]))
        cur = letter
    return ans

