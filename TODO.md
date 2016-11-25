# To Do
## Zet je naam erachter als je het gaat doen voor volgende week dinsdag!
- Grid in grid maken, maakt het mogelijk om "random" voor alle varianten te laten werken.(Tom)

- Sneller maken van algoritme. Aanmaken van het eerste grid(oplossing) mag lang duren! Het is namelijk zo dat als je gaat schuiven/ verplaatsen dat je meteen al een nieuwe variant hebt waardoor de oplossingen NA de eerste gevonden oplossing van een variant korter duurt. De score functie moet echter wel sneller, aangezien deze na elke mutatie moet worden gerund en deze nu best lang duurt. De duur komt wellicht door het herhaalde aanmaken van een deep copy. Dit kost veel geheugen.

- Waterfunctie aanpassen zodat deze 4 zo dun mogelijke watervlaktes maakt. Dit zal het plaatsen van water en huizen waarschijnlijk makkelijker maken en de score aanzienlijk doen verhogen. Mag nog wel worden uitgetest of dit ook daadwerkelijk het geval is! Gooi er wat statistiek tegenaan, staat mooi in het verslag.(Tom, deze is namelijk van belang voor grid in grid dus wacht er liever niet te lang op)

- Beginnen aan verslag, al is het maar alleen beslissingen noemen en het onderbouwen van beslissingen. Gewoon docs aanmaken en zelf punten toevoegen.(Iedereen)

- Kijken naar hill climbing en simulated annealing. Hierbij is het van essentie het schuiven en ruilen van locatie van huizen. Het idee is dat je verschillende strategies hebt, die alllemaal een andere kans hebben om geselecteerd te worden. Strategy 1 kan zijn het verwisselen van een klein met een groot huis, strategy 2 het schuiven van een willekeurig huis, strategy 3 het verwisselen van een klein met een medium huis en strategy 4 het verwisselen van een medium en een groot huis. Op basis van elke verplaatsing zijn toegevoegde waarde, moet je het een kans geven dat je het geeft dat je deze mutatie toevoegt! Sommige mutaties zijn namelijk onzinning om te blijven doen en die voegen dan niet zoveel/minder toe.

- Moeten besluiten of we het berekenen van de vrijstand en afstand(in score) behouden zoals deze is. Op het moment wordt vrijstand heel ruim berekend (Vierkant ipv afgeronde hoeken) wegens de kosten daaraan verbonden. De waarde (minimale afstand tussen huizen) wordt echter wel op het moment met pythagoras berekend, wat best een dure maar nauwkeurige handeling is. Hierbij kan worden afgewogen of we wellicht gaan kijken naar het gebruik van een newtonian distance. Deze is minder nauwkeurig, maar kost rekenkundig gezien veel minder.

