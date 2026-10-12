def cislo_text (cislo):

    hodnota = int(cislo)

    jednotky = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"]
    nact = ["deset", "jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"]
    desitky = ["", "", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]

    if hodnota ==100:
        return "sto"

    elif hodnota < 10:
        return jednotky[hodnota]

    elif hodnota < 20:
        return nact[hodnota -10]

    else:
        desitka = hodnota // 10
        jednotka = hodnota % 10

        if jednotka == 0:
            return desitky[desitka]
        else:
            return desitky[desitka] + " " + jednotky[jednotka]

if __name__ == "__main__":
    cislo = input ("zadej číslo: ")
    text = cislo_text (cislo)
    print (text)

