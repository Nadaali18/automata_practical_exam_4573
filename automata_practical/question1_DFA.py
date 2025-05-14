def dfa1(string):
    state = 0
    for ch in string:
        if ch == "1":
            state = 1 - state
    return state == 0

def dfa2(string):
    count = 0
    for ch in string:
        if ch == "1":
            count += 1
    return count % 2 == 0

def check_equivalence():
    test_cases = ["", "0", "1", "11", "10", "101", "111", "1101", "1111"]
    for string in test_cases:
        if dfa1(string) != dfa2(string):
            return False
    return True
