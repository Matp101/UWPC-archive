from typing import List

def letterCombinations(digits: str) -> List[str]:
    digits_d = {
        '0': [' '],
        '1': [''],
        '2': ['a', 'b', 'c'], 
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'], 
        '5': ['j', 'k', 'l'], 
        '6': ['m', 'n', 'o'], 
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }
    res = []

    def find_n(ind, sub):
        if len(sub) == len(digits):
            res.append(sub)
            return
        for i in digits_d[digits[ind]]:
            find_n(ind + 1, sub + i)

    if digits:
        find_n(0, "")

    return res

# Sample usage
test_cases = ["23", "", "2"]
results = [letterCombinations(case) for case in test_cases]
for case, result in zip(test_cases, results):
    print(f"letterCombinations({case}) = {result}")

# Generating test cases
from TestCaseHandler import TestCaseHandler
test_cases = [
    "35",
    "52",
    "4",
    "7",
    ""
]
results = [letterCombinations(case) for case in test_cases]
handler = TestCaseHandler(12, test_cases, results)
handler.write_to_files()