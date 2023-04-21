class Solution:
    def diffWaysToCompute(self, expression):
        if len(expression) <= 2:
            return [int(expression)]

        ret = []
        for i in range(len(expression)):
            if not expression[i].isdigit():
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])
                for l in left:
                    for r in right:
                        if expression[i] == "+":
                            ret.append(l + r)
                        elif expression[i] == "-":
                            ret.append(l - r)
                        else:
                            ret.append(l * r)
        return ret