from automata_practical.questions_files.question2_cyk_algorithm import cyk_algorithm
cfg = {
    'variables': ['S', 'A', 'B'],
    'terminals': ['a', 'b'],
    'start': 'S',
    'productions': {
        'S': [['A', 'B']],
        'A': [['a']],
        'B': [['b']]
    }
}

print('If String belong to CFG In CNF?')
print('ab: ',cyk_algorithm(cfg, ['a', 'b']))    # True
print('aa: ',cyk_algorithm(cfg, ['a', 'a']))    # False
print('ba: ',cyk_algorithm(cfg, ['b', 'a']))    # False
print('a: ',cyk_algorithm(cfg, ['a']))         # False
print('aba: ',cyk_algorithm(cfg, ['a', 'b','a']))  # False
