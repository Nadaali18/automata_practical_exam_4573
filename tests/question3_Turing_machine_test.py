from automata_practical.question3_Turing_machine import turing_machine

def test_prime():
    assert turing_machine("111") == True  # length 3

def test_non_prime():
    assert turing_machine("1111") == False  # length 4
