def same_language(dfa1, dfa2):
    
    start = (dfa1['start'], dfa2['start'])
    visited = []
    queue = [start]

    while queue:
        current = queue.pop(0)
        s1, s2 = current

        if current in visited:
            continue
        visited.append(current)

        accepting1 = s1 in dfa1['accept']
        accepting2 = s2 in dfa2['accept']
        if accepting1 != accepting2:
            return False

        for symbol in dfa1['alphabet']:
            next1 = dfa1['transition'].get((s1, symbol))
            next2 = dfa2['transition'].get((s2, symbol))
            if next1 is not None and next2 is not None:
                queue.append((next1, next2))

    return True
