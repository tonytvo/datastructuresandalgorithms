class Fibonacci:
    computedFibonacci = {}

    def calc_iter(self, n: int) -> int:
        if n < 2:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    def calc(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1

        if n in self.computedFibonacci:
            return self.computedFibonacci[n]

        result = self.calc(n - 1) + self.calc(n - 2)
        self.computedFibonacci[n] = result
        return result