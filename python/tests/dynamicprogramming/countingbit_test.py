from src.dynamicprogramming.countingbit import CountingBit

class TestCountingBit:
    def test_countbit_3(self):
        cb = CountingBit()
        assert cb.countBits(3) == [0, 1, 1, 2]

    def test_climbstairs_5(self):
        cb = CountingBit()
        assert cb.countBits(5) == [0, 1, 1, 2, 1, 2]
