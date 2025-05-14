def build_transitions():
    return {
        # ----- المرحلة 1: التحقق من الأعداد الصغيرة -----
        ('q0', '1'): ('q1', '1', 'R'),  # بداية القراءة
        ('q0', 'B'): ('reject', 'B', 'S'),  # العدد 0 (مدخل فارغ)
        
        ('q1', '1'): ('q2', '1', 'R'),
        ('q1', 'B'): ('reject', 'B', 'S'),  # العدد 1
        
        ('q2', '1'): ('q3', '1', 'R'),
        ('q2', 'B'): ('accept', 'B', 'S'),  # العدد 2 (أولي)
        
        ('q3', '1'): ('q4', '1', 'R'),
        ('q3', 'B'): ('accept', 'B', 'S'),  # العدد 3 (أولي)
        
        # ----- المرحلة 2: التحقق من الأعداد الزوجية -----
        ('q4', '1'): ('q5', '1', 'R'),
        ('q4', 'B'): ('check_even', 'B', 'L'),  # نهاية الشريط
        
        ('q5', '1'): ('q4', '1', 'R'),
        ('q5', 'B'): ('check_even', 'B', 'L'),  # نهاية الشريط
        
        ('check_even', '1'): ('reject', '1', 'S'),  # عدد زوجي > 2
        ('check_even', 'B'): ('init_div', 'B', 'R'),  # عدد فردي
        
        # ----- المرحلة 3: التحقق من القواسم الفردية -----
        ('init_div', '1'): ('mark_first', 'X', 'R'),  # بداية المقسوم عليه
        ('init_div', 'X'): ('init_div', 'X', 'R'),
        
        ('mark_first', '1'): ('move_right', 'D', 'R'),  # وضع علامة على المقسوم عليه
        ('mark_first', 'X'): ('mark_first', 'X', 'R'),
        
        ('move_right', '1'): ('move_right', '1', 'R'),
        ('move_right', 'X'): ('move_right', 'X', 'R'),
        ('move_right', 'B'): ('find_divisor', 'B', 'L'),  # نهاية الشريط
        
        ('find_divisor', '1'): ('check_div', '1', 'L'),
        ('find_divisor', 'X'): ('find_divisor', 'X', 'L'),
        ('find_divisor', 'D'): ('next_divisor', 'D', 'R'),
        
        ('next_divisor', 'X'): ('next_divisor', 'X', 'R'),
        ('next_divisor', 'D'): ('next_divisor', 'D', 'R'),
        ('next_divisor', '1'): ('mark_first', 'X', 'R'),  # قاسم جديد
        ('next_divisor', 'B'): ('accept', 'B', 'S'),  # لم يتم إيجاد قاسم (عدد أولي)
        
        ('check_div', '1'): ('check_div', '1', 'L'),
        ('check_div', 'X'): ('check_div', 'X', 'L'),
        ('check_div', 'D'): ('verify_div', 'D', 'L'),
        
        ('verify_div', '1'): ('unmark', '1', 'L'),  # باقي قسمة ≠ 0
        ('verify_div', 'X'): ('verify_div', 'X', 'L'),
        ('verify_div', 'B'): ('reject', 'B', 'S'),  # باقي قسمة = 0 (ليس أولي)
        
        ('unmark', '1'): ('unmark', '1', 'L'),
        ('unmark', 'X'): ('unmark', '1', 'L'),  # إعادة تعليم الأرقام
        ('unmark', 'D'): ('reset_head', 'D', 'R'),
        
        ('reset_head', '1'): ('reset_head', '1', 'R'),
        ('reset_head', 'X'): ('reset_head', 'X', 'R'),
        ('reset_head', 'D'): ('mark_first', 'X', 'R')  # العودة للبداية
    }
