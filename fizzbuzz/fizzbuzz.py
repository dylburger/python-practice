def fizzbuzz_num(i):
    if i % 5 == 0 and i % 3 == 0:
        return 'FizzBuzz'
    elif i % 3 == 0:
        return 'Fizz'
    elif i % 5 == 0:
        return 'Buzz'
    else:
        return i


def run_fizzbuzz(n):
    for i in range(1, n + 1):
        print(fizzbuzz_num(i))


if __name__ == "__main__":
    run_fizzbuzz(100)
