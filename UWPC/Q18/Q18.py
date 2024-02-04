def pow(x, n):
    result = x ** n
    return f"{result:.5f}"

test_cases = [
    (2.00000, 10),
    (2.10000, 3),
    (2.00000, -2)
]
results = [pow(case[0], case[1]) for case in test_cases]
for case, result in zip(test_cases, results):
    print(f"pow({case}) = {result}")

# Generating test cases
from TestCaseHandler import TestCaseHandler
test_cases = [
    [5.00000, 2],
    [3.12500, 5],
    [1.23456, 7],
    [10.00000, -3],
]
results = [pow(*case) for case in test_cases]
handler = TestCaseHandler(18, test_cases, results)
handler.write_to_files()