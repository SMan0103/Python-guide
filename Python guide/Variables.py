# Variabler er grundstene for programering 
# Variabler gemmer nemlig ting for dig som du kan klade på sendere som kan ses inde på print.py
# Der findes rigtig mange slags af variablerne men de alle har det samme til fældes. 
# De starter med et navn så = også den værdi. Som kan ses. 
sigHej = "Hej"

print(sigHej)
# Her vil den så printe Hej, fordi vi har sagt den skulle sige det der står inde i sigHej 
# Vi gemte det man kalder en string. En string er nemlig text men der findes også andre slag. 
# lige hurtig igenmen dem.

# String
text = "hej"
print(text)

# int
tal = 1
print(tal)

# Float
komatal = 1.
print(komatal)

# Bloolens
bool = 1 == 1
print(bool) 

# Som du kan se så er der 2 forsklige måde til at gemme tal. Int og Float.
# Int gemmer heletal, hvor imod Float gemmer komatal

# Bloolens siger hvis en ting er falsk eller rigtig. Det skal man nolge gange bruge hvis
# skal finde ud af hvis en kode skal videre eller stoppe der. 


# Hvis man gerne vil få computeren til at sige hvad for en slags variabel det er så kan man skrive koden 
print(type(bool))
# Den vil printe bool ikke fordi den hedder det men fordi at det er en bloolen


# Navngivning 
# Når man navngiver en variabel så er det lige gyldig hvis du vil have en der hedder hej eller Hej 
# python vil nemlig sige at det er to forskilige ting. Som kan ses nede udner 
hej = "Hej"
Hej = "Forvel"
print(hej, "og", Hej)
# Den printer Hej og Forvel fordi at vi har givet de to forskilige en lille forskel, som er et lille og et stor bogkstav.

