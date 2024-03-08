#1

def prov_medelvärde():
    prov1 = int(input("Mata in resultatet på prov 1"))
    prov2 = int(input("Mata in resultatet på prov 2"))
    prov3 = int(input("Mata in resultatet på prov 3"))

    medel = prov1 + prov2 + prov3 / 3
    print(f"Medelvärde på alla 3 proven: {medel}")
    if medel > 90:
        print("Bra jobbar!")




