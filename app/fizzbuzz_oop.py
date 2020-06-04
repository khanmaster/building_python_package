class Fizzbuzz:
    def __init__(self, start_of_range, end_of_range):
        self.fizzrange = range(start_of_range, end_of_range)
        self.fizzbuzz_list = []
        self.fizz_buzz = self.__fizzbuzz_iterator()

    def _divisible_by(self, num1, num2):
        if num1 % num2 == 0:
            return True
        else:
            return False

    def __fizzbuzz_iterator(self):
        for num in self.fizzrange:
            if self._divisible_by(num, 5) and self._divisible_by(num, 3):
                self.fizzbuzz_list.append("fizzbuzz")
            elif self._divisible_by(num, 5):
                    self.fizzbuzz_list.append("buzz...")
            elif self._divisible_by(num, 3):
                    self.fizzbuzz_list.append("fizzz..")
            else:
                self.fizzbuzz_list.append(num)

# num_1_to_100 = Fizzbuzz(1, 100)
#
# print(num_1_to_100.fizzbuzz_list)
# cLet's import this file in our program.py