def sude_nebo_liche(cislo):

    if cislo % 2 == 0:
        print(f"Číslo {cislo} je sudé")
    else:
        print(f"Číslo {cislo} je liché")


if __name__ == "__main__":
    # Volání funkce podle zadání
    sude_nebo_liche(5)
    sude_nebo_liche(1000000)
