from automata_practical.questions_files.question3_turing_machine import TuringMachine
def test_turing_machine():
    test_cases = {
        "": False,          # length 0
        "1": False,         # length 1 (not prime)
        "11": True,         # length 2 (prime)
        "111": True,        # length 3 (prime)
        "1111": False,      # length 4
        "11111": True,      # length 5 (prime)
        "111111": False,    # length 6
        "1111111": True,    # length 7 (prime)
        "11111111": False,  # length 8
        "111111111": False, # length 9
        "1111111111": False,# length 10
        "11111111111": True,# length 11
    }

    for inp, expected in test_cases.items():
        tm = TuringMachine(inp)
        result = tm.run()
        print(f"Input: '{inp}' Length: {len(inp)} => {'ACCEPT' if result else 'REJECT'} (Expected: {'ACCEPT' if expected else 'REJECT'})")


if __name__ == "__main__":
    test_turing_machine()