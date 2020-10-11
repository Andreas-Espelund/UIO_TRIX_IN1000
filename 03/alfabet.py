'''
I denne oppgaven skal du manipulere en liste med hele det engelske alfabete.

alfabet = ["O","U","P","H","Q","T","Z","Y","E","S","F","C",
"R","V","J","L","X","A","M","G","D","I","B","W","K","N"]
Bruk de innebygde metodene i lister for å sortere listen. Du skal deretter
printe det første tegnet i listen, men det skal være en liten bokstav.
(Hint lower())
'''

alfabet = ["O","U","P","H","Q","T","Z","Y","E","S","F","C",
"R","V","J","L","X","A","M","G","D","I","B","W","K","N"]

alfabet.sort(reverse=False)

print(alfabet[0].lower())
