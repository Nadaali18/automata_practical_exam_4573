from automata_practical.question2_CYK_algorithm import cyk_parse

def test_cyk_valid():
    assert cyk_parse("ab") == True

def test_cyk_invalid():
    assert cyk_parse("aab") == False
