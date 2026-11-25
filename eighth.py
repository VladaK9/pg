def bin_to_dec(binarni_cislo):
    # funkce spocita hodnotu predavaneho binarniho cisla (binarni_cislo muze byt str i int!!!)
    # 111 -> 7
    # "101" -> 5
    
    # Převedeme vstup na textový řetězec, abychom mohli projít jednotlivé číslice zleva doprava
    bin_str = str(binarni_cislo)
    
    vysledek = 0
    for cislice in bin_str:
        vysledek = vysledek * 2 + int(cislice)
        
    return vysledek


def test_bin_to_dec():
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128


if __name__ == "__main__":
    test_bin_to_dec()
    print("Všechny testy proběhly v pořádku!")
    print("10011101 ->", bin_to_dec("10011101"))
    print("10011101 (int) ->", bin_to_dec(10011101))