# Rushproject
Rush Hour is een puzzelspel waarin de speler een rode auto uit een drukke parkeerplaats moet manoeuvreren. Het spelbord is een raster waarop verschillende voertuigen van verschillende lengtes in horizontale en verticale richtingen geparkeerd staan. De speler kan de voertuigen alleen vooruit of achteruit verplaatsen in de richting waarin ze georiënteerd zijn. Het doel is om de weg vrij te maken zodat de rode auto het bord kan verlaten via een uitgang. Het spel varieert in moeilijkheidsgraad met steeds complexere opstellingen naarmate de speler vordert.

## Aan de slag

### Vereisten
Deze codebase is volledig geschreven in Python 3.12.3.

### Gebruik
Een voorbeeldje kan gerund worden door aanroepen van:

```
python main.py
```

In de main.py kan men het gameboard en het algoritme wat gebruikt moet worden aanpassen. 


## Structuur
UML
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



