def K_Sub(input_str, K):
    left = 0
    right = 0
    n = len(input_str)
    ans = []
    cur_count = 0
    while right <n:
        while cur_count <K:
            if input_str[right] == '1':
                cur_count +=1
            right +=1
            if right >=n:
                break

        while cur_count ==K:
            ans.append(input_str[left:right])

            if input_str[left] =='1':
                cur_count -=1
            left += 1
    print(ans)
    ans = sorted(ans, key = len)

    return ans[0]


