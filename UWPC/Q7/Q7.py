def elevator(input):
    floor = 0
    for c in input:
        floor += 1 if c == "(" else -1
    return floor

# Testing with the provided samples
test_cases = ["(())", "(((", "())))"]
results = [elevator(case) for case in test_cases]
for case, result in zip(test_cases, results):
    print(f"elevator[{case}] = {result}")

# Generating test cases
from TestCaseHandler import TestCaseHandler
test_cases = ["((((((((((", "((()", "))()"]
results = [elevator(case) for case in test_cases]
handler = TestCaseHandler(7, test_cases, results)
handler.write_to_files()