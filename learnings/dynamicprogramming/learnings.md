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

## greedy problem

- https://leetcode.com/problems/longest-palindrome/description/

## problem with 2 dp array


# Questions and Answers
- what is dynamic programming?
  - Dynamic programming is a method for solving complex problems by breaking them down into simpler subproblems. It is applicable when the subproblems overlap and optimal substructure exists.
- what is greedy algorithm?
  - A greedy algorithm is an algorithmic paradigm that builds up a solution piece by piece, always choosing the next piece that offers the most "immediate"/best benefit. Greedy algorithms do not always produce optimal solutions for all problems.
  - we make the greedy choice at each step with the hope of finding the global optimum.
  - it has subproblem but they do not have optimal sub-structure
- what does it mean to have optimal sub-structure?
  - A problem exhibits optimal substructure if an optimal solution to the problem can be constructed efficiently from optimal solutions of its subproblems.