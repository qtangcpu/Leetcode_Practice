class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def isValid(string):
            if string == "0":
                return True

            if string[0] == "0":
                return False

            if 0 < int(string) <= 255:
                return True

            return False

        def backtrack(track, string, count):
            if count == 3:
                if isValid(string):
                    track.append(string)
                    res.append(".".join(track))
                    track.pop()

                return

            for i in range(1, len(string)):
                if isValid(string[:i]):
                    track.append(string[:i])
                    backtrack(track, string[i:], count + 1)
                    track.pop()
                else:
                    return

        res = []
        backtrack([], s, 0)
        return res