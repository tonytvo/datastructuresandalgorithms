leetcode $: 338
class Solution:
    def countBits(self, n: int) -> List[int]:
        
0 -> 0
1 -> 1
2 -> 10 -> 1
3 -> 11 -> 2
4 -> 100 -> 1
5 -> 101 -> 2
6 -> 110 -> 2
7 -> 111 -> 3
8 -> 1000 -> 1
9 -> 1001 -> 2
10 -> 1010 -> 2
11 -> 1011 -> 3 -> 8 + 3 -> countbigs(8) + countbits(3)
12 -> 1100 -> 2
13 -> 1101 -> 3
14 -> 1110 -> 3
15 -> 1111 -> 4
16 -> 10000 -> 1

if log base 2 return integer -> 1
even -> odd => previous + 1
odd => even 

class Solution:
    def countBits(self, n: int) -> List[int]:
        # after writing out a few examples on paper
        # between powers of 2 the previous pattern is repeated plus the previous pattern + 1
        # 0 1
        # [1 2]
        # [1 2] [2 3]
        # [1 2 2 3] [2 3 3 4]
        # [1 2 2 3 2 3 3 4] [2 3 3 4 3 4 4 5]

        # since we already know
        ans = [0,1,1,2,1,2,2,3]
        
        if n < len(ans):
            return ans[:n+1]       
        
        # start with
        current = [1,2,2,3]
        
        # initiate i to last index + 1 of ans
        i = len(ans)
        while i <= n:
            t = [c + 1 for c in current]
            current += t
            ans += current
            i = len(ans)
        
        return ans[:n+1]

class Solution:
    
    def countBits(self, n: int) -> List[int]:
        # initially precompute bits from 1 to 8
        # from 9 to n
        # use previous power of 2 + bitcount of i
        # (that we have already found) 
        # where i runs from 1 to ... reset i
        # when you hit the next power of 2
        
        ans = [0, 1, 1, 2, 1, 2, 2, 3, 1]
        
        if n <= 8:
            return ans[0:n+1]
        count = 1
        previous = 8 # (8 but index 7)
        previousPower2 = 8
        for k in range(9, n+1):            
            # if power of 2, reset
            if k % previousPower2 == 0:
                count = 1
                previous = k
                previousPower2 = k
                ans.append(1)
            else:
                ans.append( ans[previous] + ans[count])
                count += 1
        
        return ans


class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        sub = 1

        for i in range(1, n + 1):
            if sub * 2 == i:
                sub = i
            
            dp[i] = dp[i - sub] + 1
        
        return dp
