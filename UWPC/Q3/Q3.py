import math
def reverse(x: int) -> int:
    MAX_INT = 2 ** 31 - 1 # 2,147,483,647
    MIN_INT = -2 ** 31    #-2,147,483,648
    reverse = 0
    while x != 0:
        if reverse > MAX_INT / 10 or reverse < MIN_INT / 10:
            return 0
        digit = x % 10 if x > 0 else x % -10
        reverse = reverse * 10 + digit
        x = math.trunc(x / 10)
    return reverse

# Testing with the provided samples
test_cases = [123, -123, 120, 2147483647]
results = [reverse(case) for case in test_cases]
for case, result in zip(test_cases, results):
    print(f"reverse({case}) = {result}")

## Generating test cases
#from TestCaseHandler import TestCaseHandler
#test_cases = [12345, 0, 9999999999]
#results = [reverse(case) for case in test_cases]
#handler = TestCaseHandler(3, test_cases, results)
#handler.write_to_files()