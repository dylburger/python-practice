from fizzbuzz import fizzbuzz_num


def test_fizz():
    assert fizzbuzz_num(3) == "Fizz"


def test_buzz():
    assert fizzbuzz_num(5) == "Buzz"


def test_fizzbuzz():
    assert fizzbuzz_num(15) == "FizzBuzz"


def test_other_num():
    assert fizzbuzz_num(17) == 17
