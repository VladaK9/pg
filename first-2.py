
def sude_nebo_liche(cislo):
    if cislo % 2 == 0:
        print(f"cislo {cislo} je sude")
    else:
        print(f"cislo {cislo} je liche")

if __name__ == "__main__":
    sude_nebo_liche(5)
    sude_nebo_liche(1000000)
