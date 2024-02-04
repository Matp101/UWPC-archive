def isSameTree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

# Testing with the provided samples
test_cases = [
    ["1 2 3", "1 2 3"],
    ["1 2", "1 null 2"],
    ["1 2 1", "1 1 2"]
]

for case in test_cases:
    p_tree = build_tree(case[0].split())
    q_tree = build_tree(case[1].split())
    result = isSameTree(p_tree, q_tree)
    print(f"isSameTree({case}) = {result}")


## Generating test cases
#from TestCaseHandler import TestCaseHandler
#test_cases = [
#    ["mathew", "mathew", "mathew", "mathew", "mathew", "mathew"], 
#    ["hepkp", "halna", "relgs", "pylrd", "hewlf", "hejuu", "ggglo", "kvklo"], 
#    ["warcd", "abced", "wcbad", "boelw", "dlrow", "fffff", "horrr", "qpfld"],
#    ["paaa", "pbbb", "cocc", "dodd", "eeoe", "ffof", "gggp", "gggp"],
#]
#results = [correct_signal_error(case) for case in test_cases]
#handler = TestCaseHandler(8, test_cases, results)
#handler.write_to_files()