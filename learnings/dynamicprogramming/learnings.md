- what's the programming paradigm?
  - understand the various patterns? (like 20 patterns

# approach
- if the problem can be broken down into smaller sub problem and problem has optimal sub-structure
- if you can solve the sub problem optimally, that it is guaranteed that you can solve the overall problems optimally using the solution of sub problems
- greedy problem also has subproblem, but greed problem does not have optimal sub-structure

- first need to figure out the recurrance patterns
- how can I change that recurrance patterns into bottom up approach (iterative solution)
- basically in bottom up approach, we use array (or temp variables) to keep track of the recurrance values

- in this specific case, we have 2 temp variables, a and b to keep track of previous solved climbStairs

# patterns

## problem with only 2 variables for bottom up

- climbing stairs (leetcode 70)[https://leetcode.com/problems/climbing-stairs/]

## problem with 1 dp array

- counting bits (leetcode 338)[https://leetcode.com/problems/counting-bits/description/]

## problem with 2 dp array