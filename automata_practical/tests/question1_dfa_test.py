from automata_practical.questions_files.question1_dfa import same_language
dfa1 = {
    'states': ['q0', 'q1'],
    'alphabet': ['a', 'b'],
    'transition': {
        ('q0', 'a'): 'q1',
        ('q0', 'b'): 'q0',
        ('q1', 'a'): 'q1',
        ('q1', 'b'): 'q1'
    },
    'start': 'q0',
    'accept': ['q1']
}

dfa2 = {
    'states': ['s0', 's1'],
    'alphabet': ['a', 'b'],
    'transition': {
        ('s0', 'a'): 's1',
        ('s0', 'b'): 's0',
        ('s1', 'a'): 's1',
        ('s1', 'b'): 's1'
    },
    'start': 's0',
    'accept': ['s1']
}

print('Are both Dfa Accept same language? ',same_language(dfa1, dfa2))  
