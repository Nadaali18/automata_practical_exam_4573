grammar = {
    "S": [("A", "B")],
    "A": [("a",)],
    "B": [("b",)]
}

def cyk_parse(string):
    n = len(string)
    if n == 0:
        return False
    table = [[set() for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for variable, rules in grammar.items():
            for rule in rules:
                if len(rule) == 1 and rule[0] == string[i]:
                    table[i][i].add(variable)
    for length in range(2, n + 1):
        for start in range(n - length + 1):
            end = start + length - 1
            for split in range(start, end):
                for variable, rules in grammar.items():
                    for rule in rules:
                        if len(rule) == 2:
                            left, right = rule
                            if left in table[start][split] and right in table[split+1][end]:
                                table[start][end].add(variable)
    return "S" in table[0][n - 1]
