from src.dynamicprogramming.fibonaccii import Fibonacci

class TestBubbleSort:
    def test_fibonacci_5(self):
        fib = Fibonacci()
        assert fib.calc(5) == 5

    def test_fibonacci_30(self):
        fib = Fibonacci()
        assert fib.calc(50) == 12586269025
