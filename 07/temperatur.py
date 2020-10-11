'''
Lag en klasse navnet Temperatur som tar et flyttall inn i konstruktøren som representerer
temperatur i grader Celsius.

Lag tre hent-metoder: hent_celsius, hent_fahrenheit og hent_kelvin som beregner temperaturen
i hver enhet. (Hint: Kelvin = Celsius + 273,15 og Fahrenheit = (Celcius * 9/5) + 23)

Endre konstruktøren slik at den mottar et flyttall og en streng. Hvis strengen er «Celsius»
bare lagre temperaturen som vi gjorde før. Hvis strengen er «Fahrenheit» eller «Kelvin» konvertere
temperaturen til Celsius og lagre den.

Be brukeren om en temperatur og en enhet, lag en Temperatur objekt, og skriv ut temperaturen
i alle de tre enhetene.
'''

class Temperatur:
    def __init__(self,temperatur,enhet):
        if enhet.lower() == "celcius":
            self._tempCels = temperatur
        elif enhet.lower() == "farenheit":
            self._tempFare = (temperatur*9/5)+23
        elif enhet.lower()="kelvin":
            self._tempKelv = temperatur + 273.15


    def hent_celsius(self):
        return self._tempCels

    def hent_kelvin(self):
        return self._tempKelv

    def hent_fahrenheit(self):
        return self._tempFare
