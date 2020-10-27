from spillbrett import Spillebrett


def main():
    spill = Spillebrett(int(input("Skriv inn rader: ")),
                        int(input("Skriv inn kolonner: ")))

    choice = ""
    while choice != "q":
        print(spill.tegnBrett())
        choice = input(
            "Press enter for å fortsette. Skriv r for å restarte. Skriv inn q og trykk enter for å avslutte: ")
        spill.oppdatering()

        if choice == "r":
            main()


main()  # starte hovedprogrammet
