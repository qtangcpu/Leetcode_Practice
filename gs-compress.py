class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        n = len(chars)
        i = 0
        write = 0

        while i < n:
            j = i
            while j <n and chars[j] == chars[i]:
                j+=1
            chars[write] = chars[i]
            write +=1
            if j-i >1:
                for c in str(j-i):
                    chars[write] = c
                    write+=1
            i = j
        return write