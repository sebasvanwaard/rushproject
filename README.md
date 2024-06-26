# Rushproject
Rush Hour is een puzzelspel waarin de speler een rode auto uit een drukke parkeerplaats moet manoeuvreren. Het spelbord is een raster waarop verschillende voertuigen van verschillende lengtes in horizontale en verticale richtingen geparkeerd staan. De speler kan de voertuigen alleen vooruit of achteruit verplaatsen in de richting waarin ze georiënteerd zijn. Het doel is om de weg vrij te maken zodat de rode auto het bord kan verlaten via een uitgang. Het spel varieert in moeilijkheidsgraad met steeds complexere opstellingen naarmate de speler vordert.

## Aan de slag

### Vereisten
Deze codebase is volledig geschreven in Python 3.12.3.

### Gebruik
Een voorbeeldje kan gerund worden door aanroepen van:

```
python main.py pad_naar_boardfile Algoritme
```

Bijvoorbeeld:

python main.py gameboards/Rushhour6x6_1.csv Breadth_first

Voor de algoritmes kan je kiezen uit: Breadth_first, Depth_first, Iterative_deepening, A_star, A_star_lukas, A_star_nn (let op! Hij is hoofdlettergevoelig)

en zou dan de volgende output moeten geven:

joepie
The solution to gameboards/Rushhour6x6_1.csv was found in 1.341097116470337 seconds, using the Breadth_first algorithm
The found solution: [('A', -1), ('C', -1), ('G', -1), ('G', -1), ('J', -1), ('I', 1), ('I', 1), ('H', 1), ('E', 1), ('D', -1), ('L', -1), ('L', -1), ('J', -1), ('J', -1), ('E', 1), ('E', 1), ('H', -1), ('I', -1), ('I', -1), ('I', -1), ('H', 1), ('E', -1), ('E', -1), ('J', 1), ('J', 1), ('J', 1), ('E', 1), ('L', 1), ('X', 1), ('X', 1), ('X', 1), ('G', 1), ('B', -1), ('I', -1), ('X', 1)]
This solution has 35 moves
In total 2895 states have been generated, of which 2305 where duplicates (and thus unused)
A total of 590 states were visited

In de main.py staan verder voor elk algoritme wat proef code klaar waar met meer controle de algoritmes kunnen worden gerund.


## Structuur
![alt text](https://github.com/sebasvanwaard/rushproject/blob/main/UML.png)



De lijst hieronder beschrijft de belangrijkste mappen en files in het project, en waar je ze kan vinden:

- **/src**: bevat alle code van dit project
  - **/src/algorithms**: bevat de code voor algoritmes
  - **/src/game**: bevat de twee benodigde classes; board en car
  - **/src/plots**: bevat de code voor de grafieken van de random algoritme resultaten en de state space, maar ook de code voor de visualisatie van de beweging van de auto's bij het runnen van een experiment
- **/experiments**: bevat de verschillende databestanden en plots om de resultaten van het random algoritme te visualiseren
  - **/experiments/data**: bevat de data voor de opgeloste gameboards met het random algoritme
  - **/experiments/plots**: bevat de plots van de data voor de opgeloste gameboards met het random algoritme  
- **/gameboards**: bevat de verschillende databestanden die de informatie bevatten hoe de auto's in de startsituatie staan. 

## Auteurs
- Lukas Kleijn
- Sebas van Waard
- Anouk de Vries



