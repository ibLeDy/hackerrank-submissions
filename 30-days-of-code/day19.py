class Calculator(AdvancedArithmetic):  # noqa
    def divisorSum(self, n):
        return sum(factors(n))


def factors(x):
    factor_list = []

    for i in range(1, x + 1):
        if x % i == 0:
            factor_list.append(i)

    return factor_list
