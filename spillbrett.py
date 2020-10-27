from random import randint
from celle import Celle


class Spillebrett:
    def __init__(self, rader, kolonner):
        self._rader = rader
        self._kolonner = kolonner
        self._rutenett = []
        self._generasjonsnummer = 0  # vi er programører så vi teller fra 0 :^)
        # mens vi lager objektene så setter vi naboen til objektet til venste, opp venste, opp høyre og opp midten, og vice versa
        # sånn får hver objekt naboene sine i en liste, listen refererer til objektes naboer og man kan enkelt finne ut om de er i livet eller ikke
        for i in range(kolonner):
            self._rutenett.append([])
            for j in range(rader):
                self._rutenett[i].append(Celle())
                if j > 0:
                    self._rutenett[i][j - 1].leggTilNabo(self._rutenett[i][j])
                    self._rutenett[i][j].leggTilNabo(self._rutenett[i][j - 1])

                    if i > 0:
                        self._rutenett[i-1][j-1].leggTilNabo(
                            self._rutenett[i][j])
                        self._rutenett[i][j].leggTilNabo(
                            self._rutenett[i-1][j-1])

                if i > 0:
                    self._rutenett[i-1][j].leggTilNabo(self._rutenett[i][j])
                    self._rutenett[i][j].leggTilNabo(self._rutenett[i-1][j])

                    if j < rader - 1:
                        self._rutenett[i-1][j+1].leggTilNabo(
                            self._rutenett[i][j])
                        self._rutenett[i][j].leggTilNabo(
                            self._rutenett[i-1][j+1])
        ##
        self._generer()

    def tegnBrett(self):
        for i in range(10):
            print("")  # “tømmer” terminalvinduet mellom hver utskrift

        msg = ""
        for y in self._rutenett:
            for x in y:
                msg += x.hentStatusTegn()
            msg += "\n"

        return msg + f"Generasjon: {self._generasjonsnummer} - Antall levende celler: {self.finnAntallLevende()}"

    def oppdatering(self):
        dødListe = []  # alle levende celler som dør
        leveListe = []  # alle døe celler som skal leve
        for i in range(self._kolonner):
            for j in range(self._rader):
                levendeNabo = 0
                for x in self._rutenett[i][j].hentNaboer():
                    if x.erLevende():
                        levendeNabo += 1
                # hvis objektet er i livet og det ikke har nokk naboer dø
                if self._rutenett[i][j].erLevende() and (levendeNabo < 2 or levendeNabo > 3):
                    dødListe.append(self._rutenett[i][j])
                # hvis objektet er dø og det har nokk naboer lev
                elif not(self._rutenett[i][j].erLevende()) and levendeNabo == 3:
                    leveListe.append(self._rutenett[i][j])
        for x in dødListe:
            x.settDoed()
        for x in leveListe:
            x.settLevende()

        self._generasjonsnummer += 1

    def finnAntallLevende(self):
        antallLevende = 0
        for i in range(self._kolonner):
            for j in range(self._rader):
                if self._rutenett[i][j].erLevende():
                    antallLevende += 1
        return antallLevende

    def _generer(self):
        for y in self._rutenett:
            for x in y:
                chance = randint(0, 2)
                if chance == 0:
                    x.settLevende()

    def finnNabo(self, rad, kolonne):
        return self._rutenett[kolonne][rad].hentNaboer()
