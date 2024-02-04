def removeDuplicates(s: str) -> str:
    idx =0
    while(idx+1<len(s)):
        if(s[idx]==s[idx+1]):
            s= s[:idx]+s[idx+2:]
            if idx > 0:
                idx -= 1
        else:
            idx += 1
    return s

# Testing with the provided samples
test_cases = ["abbaca", "wzxxzy", "abcdeffedba", "aa"]
results = [removeDuplicates(case) for case in test_cases]
for case, result in zip(test_cases, results):
    print(f"removeDuplicates({case}) = {result}")

## Generating test cases
#from TestCaseHandler import TestCaseHandler
#test_cases = ["abcddcba", "bbbb", "lol", "abccb"]
#results = [removeDuplicates(case) for case in test_cases]
#handler = TestCaseHandler(4, test_cases, results)
#handler.write_to_files()