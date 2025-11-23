class ClimbStairs:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        numberOfWaysToClimbFrom1 = 1
        numberOfWaysToClimbFrom2 = 2

        for _ in range(3, n + 1):
            numberOfWaysToClimb = numberOfWaysToClimbFrom1 + numberOfWaysToClimbFrom2
            numberOfWaysToClimbFrom1 = numberOfWaysToClimbFrom2
            numberOfWaysToClimbFrom2 = numberOfWaysToClimb

        return numberOfWaysToClimbFrom2
