def analyze_array(test_case):
    results = []
    num_cases = int(test_case[0])
    i = 1
    while num_cases > 0:
        i += 1
        array = [int(x) for x in test_case[i].split()]
        i += 1
        if all(array[j] > array[j-1] for j in range(1, len(array))):
            results.append("+")
        elif all(array[j] < array[j-1] for j in range(1, len(array))):
            results.append("-")
        else:
            results.append("0")
        num_cases -= 1
    return results

# Testing with the provided samples
test_cases = [
    ["4", "4", "-8 5 6 9", "3", "1 0 -1", "2", "7 7", "5", "1 3 7 4 5"],
    ["3", "4", "1 2 3 4", "4", "4 3 2 1", "3", "1 2 1"]
]
results = [analyze_array(case) for case in test_cases]
for case, result in zip(test_cases, results):
    print(f"analyze_array({case}) = {result}")

# Generating test cases
from TestCaseHandler import TestCaseHandler
test_cases = [
    ["1", "2", "1 2"], 
    ["2", "2", "1 2", "2", "2 1"], 
    ["4", "3", "-3 0 3", "3", "3 0 -3", "2", "1 10", "4", "1 2 3 4"],
    ["3", "3", "-3 -2 -1", "3", "-1 -2 -3", "3", "-1 1 3"],
]
results = [analyze_array(case) for case in test_cases]
handler = TestCaseHandler(10, test_cases, results)
handler.write_to_files()