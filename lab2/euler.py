class Euler:
    @staticmethod
    def compute_euler_value(n, p, k):
        """
        Compute the euler value for a given number n.
        When the algorithm reaches this step, n is of form p^k
        :param n: the initial number in shape of p^k
        :param p: the base
        :param k: the power
        :return: the euler function's value
        """
        if k == 1:
            return p - 1

        return n * (p - 1) // p

    @staticmethod
    def find_euler_value(n):
        """
        Computes the value of a natural number, based on its factorization.
        :param n: the initial number
        :return: the value of the euler function
        """
        euler_value = 1
        power_counter = 0

        if n % 2 == 0:
            while n % 2 == 0:
                n = n // 2
                power_counter += 1

            euler_value *= Euler.compute_euler_value(2, 2, power_counter)

        power = 3

        while n != 1:
            power_counter = 0
            while n % power == 0:
                n = n // power
                power_counter += 1

            if power_counter >= 1:
                euler_value *= Euler.compute_euler_value(pow(power, power_counter), power, power_counter)
            power += 2

        return euler_value
