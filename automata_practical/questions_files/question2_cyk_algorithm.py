def cyk_algorithm(cfg, string):

    n = len(string) # بيحسب طول النص وبيخزنه في n يعني عدد الحروف اللي هنتعامل معاها
    variables = cfg['variables'] # بيطلع المتغيرات أو الرموز غير الطرفية من القواعد النحوية
    table = [[set() for _ in range(n)] for _ in range(n)] # هنا بيجهز جدول فارغ من نوع 2D
    # كل خانة في الجدول فيها مجموعة علشان يحتفظ بالمتغيرات اللي ممكن تولد substring معين
    #حجم الجدول n x n
    
    #بيمشي على كل حرف في النص
    #بيشوف إيه المتغيرات (القواعد) اللي ممكن تطلع الحرف ده مباشرة
    #بيضيف المتغير ده في table[i][i] يعني الجزء اللي بيحتوي على الحرف ده لوحده
    for i in range(n):
        for var in variables:
            if [string[i]] in cfg['productions'].get(var, []):
                table[i][i].add(var)

    #بيمشي على أطوال substrings
    for l in range(2, n + 1):  
        #بيحدد منين هيبدأ الـ substring
        for i in range(n - l + 1):  
            #نهاية الـ substring
            j = i + l - 1  
            #بيجرب يقسم substring لجزئين في كل مكان ممكن
            for k in range(i, j):  
                #بيشوف هل فيه إنتاج زي A → B C
                for var in variables:
                    for prod in cfg['productions'].get(var, []):
                        #لو B بتولد أول جزء، و C بتولد تاني جزء
                        #يبقى A ينفع يولد الكل، فبيضيف A في table[i][j]
                        if len(prod) == 2:
                            B, C = prod
                            if B in table[i][k] and C in table[k + 1][j]:
                                table[i][j].add(var)
        
    #بيرجع True لو المتغير الابتدائي (S مثلًا) موجود في الخانة اللي بتمثل الكلمة كلها
    #معناها إن القواعد دي فعلاً ممكن تولد الكلمة دي
    return cfg['start'] in table[0][n - 1]
