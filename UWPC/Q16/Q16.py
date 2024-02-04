def lengthOfLongestSubstring(s: str) -> int:
    seen = {}
    l = 0
    output = 0
    for r in range(len(s)):
        if s[r] not in seen:
            output = max(output, r - l + 1)
        else:
            if seen[s[r]] < l:
                output = max(output, r - l + 1)
            else:
                l = seen[s[r]] + 1
        seen[s[r]] = r
    return output

# Testing with the provided samples
test_cases = ["abcabcbb", "bbbbb", "pwwkew"]
results = [lengthOfLongestSubstring(case) for case in test_cases]
for case, result in zip(test_cases, results):
    print(f"lengthOfLongestSubstring({case}) = {result}")

# Generating test cases
from TestCaseHandler import TestCaseHandler
test_cases = ["aab", "dvdf", " ", "au", "dvdf", "tmmzuxt", "abcabcbb"]
results = [lengthOfLongestSubstring(case) for case in test_cases]
handler = TestCaseHandler(16, test_cases, results)
handler.write_to_files()