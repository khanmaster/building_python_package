from app.fizzbuzz_oop import Fizzbuzz

num_1_to_100 = Fizzbuzz(1, 100)

#print(num_1_to_100.fizzbuzz_list)
list_fizz_buzz = num_1_to_100.fizzbuzz_list
for result in list_fizz_buzz:
    print(result)