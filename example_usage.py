from automata_practical import dfa1, dfa2, check_equivalence, cyk_parse, turing_machine

print("DFA1 accepts '1010':", dfa1('1010'))
print("DFA2 accepts '1010':", dfa2('1010'))
print("Are DFA1 and DFA2 equivalent?", check_equivalence())

print("CYK accepts 'ab':", cyk_parse('ab'))
print("CYK accepts 'aab':", cyk_parse('aab'))

print("Turing machine accepts '1111' (length 4 - not prime)?", turing_machine('1111'))
print("Turing machine accepts '11111' (length 5 - prime)?", turing_machine('11111'))
