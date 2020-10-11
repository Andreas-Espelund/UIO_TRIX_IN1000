class EspressoMaskin:
    def __init__(self):
        self._vannmengde = 1000

    # Lag espresso dersom det er nok vann
    def lagEspresso(self):
        if self._vannmengde > 40:
            print("Lager Espresso!")
            self._vannmengde -= 40
        else:
            print("Ikke nok vann, fyll på tanken.")

    # Lag lungo dersom det er nok vann
    def lagLungo(self):
        if self._vannmengde > 110:
            print("Lager Lungo!")
            self._vannmengde -= 110
        else:
            print("Ikke nok vann, fyll på tanken.")

    # Fyll paa et gitt antall milliliter vann, dersom det er plass
    def fyllVann(self, ml):
        if (1000-self._vannmengde) > ml:
            self._vannmengde+=ml

    # Les av tilgjengelig vann i ml
    def hentVannmengde(self):
        rest = self._vannmengde
        print(f'Det er {rest}ml vann i tanken.')
