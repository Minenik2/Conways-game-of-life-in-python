class Celle:
    def __init__(self):
        self._status = "død"  # kan bruke en boolean men ser ut til at obligen vil ha string
        self._naboer = []  # nabo

    def settDoed(self):
        self._status = "død"

    def settLevende(self):
        self._status = "levende"

    def erLevende(self):
        return self._status == "levende"

    def hentStatusTegn(self):
        if self._status == "levende":
            return "O"  # hvis levende
        return "."  # hvis dø

    def leggTilNabo(self, nabo):
        self._naboer.append(nabo)

    def hentNaboer(self):
        return self._naboer
