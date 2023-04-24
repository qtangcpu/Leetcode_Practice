class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        record = [0] * (n)
        record[0] = 1
        p2, p3, p5 = 0, 0, 0
        for i in range(1, n):
            num1, num2, num3 = record[p2] * 2, record[p3] * 3, record[p5] * 5
            record[i] = min(num1, num2, num3)
            if record[i] == num1:
                p2 += 1
            if record[i] == num2:
                p3 += 1
            if record[i] == num3:
                p5 += 1

        return record[-1]