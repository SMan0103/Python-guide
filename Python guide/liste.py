
# Man laver en liste ved [] også skal man tælle 0.1.2 her også hvis man gøre det baglæs så er det -1.-2.-3
liste = ["Mor", "Far", "Søster", "Bror"]
print(liste[2])
print(liste[-3])
# Når man skal have data fra mitten eller andre sted i listen
# Så skal man lave [] inde i print() funktionen også skal man skrive fra hvor til slut 
# starten er med sluten er ikke med. 
print(liste[1:3])
# Man kan også stoppe den fra et punkt. 
# Eller omvent så man kan starte fra et punkt.
print(liste[:2])
print(liste[2:])


# Vil du gerne vide hvad der er i en liste så kan du nemt finde ud af det hvis du bruger funktionen nede udner.
# Funktion tager listen også laver du en if statment som siger hvis den er så skal den da sige jeg
# Hvis det ikke er i listen så vil den sige at det ikke er der 
denneListe = ["bog", "tog", "mur", "cykel"]
if "bog" in denneListe:
    print(" bog er på din liste")
else:
    print("Nej bog er der ikke ")
