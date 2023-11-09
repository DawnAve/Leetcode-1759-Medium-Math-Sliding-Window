import math
class Solution:
    def countHomogenous(self, s: str) -> int:
        def choose2(num):
            numerator = math.factorial(num)
            denominator = (math.factorial(2) * math.factorial(num-2))
            return int(numerator/denominator)
        MOD = 10**9+7
        length = [1]
        index = 0
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                length[index]+=1
            else:
                index+=1
                length.append(1)
        ret = 0
        for i in length:
            if i == 1:
                ret +=1
                continue
            ret = ret + choose2(i+1)
        return ret % MOD
