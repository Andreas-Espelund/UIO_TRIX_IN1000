'''
Lag en funksjon som returnerer True eller False og tar inn 2 strenger som argument.
Funksjonen skal se om alle tegnene i den første strengen også er i den andre.
Om alle tegnene I den første strengen er i den andre strengen skal funksjonen returnere
True, ellers skal den returnere False. Et tegn telles bare en gang, så om et tegn er i stringEn
2 ganger må det være i stringTo to minst to ganger.

Hvordan løste du oppgaven?
'''

def sammenling(stringEn,stringTo):

    returstreng = ''
    for bokstav1 in stringEn:
        for bokstav2 in stringTo:
            if bokstav1 == bokstav2:
                stringTo = stringTo.replace(bokstav2,'',1)
                returstreng += bokstav1
                break
    return returstreng == stringTo


str1 = input(" ")
str2 = input(" ")
print(sammenling(st1,str2))
