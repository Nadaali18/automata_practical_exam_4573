# ده تعريف دالة اسمها same_language بتاخد اتنين DFA
#  علشان تقارن بينهم وتشوف هل الاتنين بيعبروا عن نفس اللغة ولا لا
def same_language(dfa1, dfa2):
    
    start = (dfa1['start'], dfa2['start']) # السطر ده بيعمل نقطة بداية موحدةعبارة عن زوج من حالة البداية بتاعت الـ DFA الأول والتاني.
    visited = [] # ده ليسته هنحط فيها الأزواج الحالات اللي زورناها قبل كده علشان منرجعش نزورهم تاني
    queue = [start] # هنستخدمه علشان نمشي على كل الحالات اللي محتاجين نفحصهاوبنبدأ بحالة البداية
       
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

#كل مرة بتطلع حالة من الطابور (queue):
# وبتسميها current وبتكون عبارة عن حالتين (واحدة من DFA1 وواحدة من DFA2)

# لو الحالة دي اتفحصت قبل كده بتعديها
# علشان متشتغلش على نفس الحاجة مرتين

# بتضيفها لقائمة الزيارات (visited) علشان تفتكر إنك شفتها

# بتقارن بين حالة القبول هنا وهناك:
# لو واحدة حالة قبول والتانية مش يبقى الـ DFA مش زي بعض وبتقول False

# لو لسه متساويين بتشوف كل حرف في الأبجدية
# وبتشوف الـ DFA1 هينتقل لفين وDFA2 هينتقل لفين بنفس الحرف

# لو الاتنين عندهم انتقالات سليمة بتضيف الحالات الجاية للطابور
# علشان تفحصهم بعدين في الدورة الجاية

# لو خلصت كل الحالات ومفيش أي فرق بينهم بتقول True
