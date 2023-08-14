class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_l = len(s) - 1
        t_l = len(t) - 1
        skip_s = skip_t = 0

        while s_l >= 0 or t_l >= 0:
            while s_l >= 0:
                if s[s_l] == "#":
                    skip_s += 1
                    s_l -= 1
                elif skip_s > 0:
                    skip_s -= 1
                    s_l -= 1
                else:
                    break

            while t_l >= 0:
                if t[t_l] == "#":
                    skip_t += 1
                    t_l -= 1
                elif skip_t > 0:
                    skip_t -= 1
                    t_l -= 1
                else:
                    break
            if s_l >= 0 and t_l >= 0:
                if s[s_l] != t[t_l]:
                    return False
            elif s_l >= 0 or t_l >= 0:
                return False
            s_l -= 1
            t_l -= 1

        return True