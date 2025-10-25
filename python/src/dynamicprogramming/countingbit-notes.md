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
11 -> 1011 -> 3
12 -> 1100 -> 2
13 -> 1101 -> 3
14 -> 1110 -> 3
15 -> 1111 -> 4
16 -> 10000 -> 1

if log base 2 return integer -> 1
even -> odd => previous + 1
odd => even 
