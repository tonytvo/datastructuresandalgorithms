from src.dynamicprogramming.climbstairs import ClimbStairs

class TestClimbStairs:
    def test_climbstairs_3(self):
        cs = ClimbStairs()
        assert cs.climbStairs(3) == 3

    def test_climbstairs_5(self):
        cs = ClimbStairs()
        assert cs.climbStairs(5) == 8

    def test_fibonacci_50(self):
        cs = ClimbStairs()
        assert cs.climbStairs(50) == 20365011074
