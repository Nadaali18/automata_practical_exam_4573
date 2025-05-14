def cyk_algorithm(cfg, string):

    n = len(string)
    variables = cfg['variables']
    table = [[set() for _ in range(n)] for _ in range(n)]

    # ملء الطبقة الأولى بناءً على الإنتاجات الطرفية
    for i in range(n):
        for var in variables:
            if [string[i]] in cfg['productions'].get(var, []):
                table[i][i].add(var)

    # ملء باقي الجدول
    for l in range(2, n + 1):  # length of substring
        for i in range(n - l + 1):  # start index
            j = i + l - 1  # end index
            for k in range(i, j):  # split point
                for var in variables:
                    for prod in cfg['productions'].get(var, []):
                        if len(prod) == 2:
                            B, C = prod
                            if B in table[i][k] and C in table[k + 1][j]:
                                table[i][j].add(var)

    # هل المتغير الابتدائي في الركن الأعلى الأيسر؟
    return cfg['start'] in table[0][n - 1]
