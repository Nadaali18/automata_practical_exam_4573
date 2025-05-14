class TuringMachine:
    def __init__(self, tape):
        self.tape = list(tape) + ['_'] * 100  
        self.head = 0
        self.state = 'start'
        self.length = 0
        self.accept = False

    def move_head(self, direction):
        if direction == 'R':
            self.head += 1
        elif direction == 'L':
            self.head -= 1
        else:
            pass  # Stay

    def count_unary_length(self):
        self.length = 0
        while self.tape[self.head] == '1':
            self.length += 1
            self.head += 1
        self.head = 0

    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def run(self):
        if self.state == 'start':
            self.count_unary_length()
            if self.is_prime(self.length):
                self.accept = True
            else:
                self.accept = False

        return self.accept


